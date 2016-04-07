import webbrowser as web

# web.open_new_tab('http://www.baidu.com')

url = 'http://www.baidu.com'

print(web.get())  # 返回一个浏览器对象 默认浏览器

w = web.get('Firefox')

print(w)  # 返回一个浏览器对象 指定对象的 get
# print(web.get('Firefoxxxxxx'))  # 出错

'''
这个方法是在默认的浏览器中显示url, 如果new = 0, 那么url会在同一个浏览器窗口下打开，
如果new = 1, 会打开一个新的窗口，如果new = 2, 会打开一个新的tab, 如果autoraise ＝ true, 窗口会自动增长。

def open(self, url, new=0, autoraise=True):
'''

# w.open_new_tab('http://www.baidu.com')
# w.open_new('http:www.163.com')
w.open(url, new=0)  # 这里试验一下咋没感觉呢.









