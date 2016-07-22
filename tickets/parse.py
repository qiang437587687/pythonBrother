# coding: utf-8

import re

from pprint import pprint

with open("stations.html") as f:
    text = f.read()
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text)
    pprint(dict(stations), indent=4)


