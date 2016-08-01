
import time
from datetime import timedelta

try:
    from HTMLParser import HTMLParser
    from urlparse import urljoin, urldefrag

except ImportError:
    from html.parser import HTMLParser
    from urllib.parse import urljoin, urldefrag

from tornado import httpclient, gen, ioloop, queues

base_url = 'http://www.tornadoweb.org/en/stable/'
concurrency = 10


@gen.coroutine
def getlinkx_from_url(url):
    """Download the page at `url` and parse it for links.
    Returned links have had the fragment after `#` removed, and have been made
    absolute so, e.g. the URL 'gen.html#tornado.gen.coroutine' becomes
    'http://www.tornadoweb.org/en/stable/gen.html'.
    """
    try:
        response = yield httpclient.AsyncHTTPClient().fetch(url)
        print('fetched %s ' % url)

        html = response.body if isinstance(response.body, str) else response.body.decode()
        urls = [urljoin(url, remove_fragment(new_url)) for new_url in get_links(html)]

    except Exception as e:
        print('Exceptio:%s %s' % (e, url))
        raise gen.Return([])

    raise gen.Return(urls)


def remove_fragment(url):
    pure_url, frag = urldefrag(url)
    return pure_url


def get_links(html):

    class URLSeeker(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.urls = []

        def handle_starttag(self, tag, attrs):
            href = dict(attrs).get('href')
            if href and tag == 'a':
                self.urls.append(href)

    url_seeker = URLSeeker()
    url_seeker.feed(html)
    return url_seeker.urls


@gen.coroutine
def main():
    q = queues.Queue()
    start = time.time()  # 记录开始时间
    fetching, fetched = set(), set()

    @gen.coroutine
    def fetch_url():
        current_url = yield q.get()
        try:
            if current_url in fetching:
                return
            print('fetching %s' % current_url)
            fetching.add(current_url)
            urls = yield getlinkx_from_url(current_url)
            fetched.add(current_url)

            for new_url in urls:
                if new_url.startswith(base_url):
                    yield q.put(new_url)

        finally:
            q.task_done()

    @gen.coroutine
    def worker():
        while True:
            yield fetch_url()

    q.put(base_url)  # put 是添加 计数  task_done 是减少引用计数

    for _ in range(concurrency):
        worker()
    yield q.join(timeout=timedelta(seconds=300))
    assert fetching == fetched
    print('Done in %d seconds, getched %s URLs.' % (time.time() - start, len(fetched)))


if __name__ == '__main__':

    import logging
    logging.basicConfig()
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)









