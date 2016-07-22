
# coding: utf-8

"""Train tickets query via command-line.

Usage:
    ticket.py [-gdtkz] <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达

Example:

    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01

"""

from docopt import docopt
from stations import stations
import requests


def cli():

    arguments = docopt(__doc__)
    print(arguments)    # 1.神奇的提取参数并且解析成json

    from_staion = stations.get(arguments['<from>']) # 2. 能这么提取参数 上面写好的形式
    to_station = stations.get(arguments['<to>'])
    date = arguments["<date>"]

    # 3. 原来还能这么处理 python 里面的 字符串.
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date, from_staion, to_station)
    print("请求的url : " + url)

    r = requests.get(url, verify=False)
    print(r.json())


if __name__ == "__main__":
    cli()



