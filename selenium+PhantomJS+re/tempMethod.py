from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 使用组个操作按键
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import os


diver = webdriver.Firefox()
# diver1 = webdriver.PhantomJS()
# diver.get('http://www.baidu.com')
diver.get('http://v.qq.com/cover/e/e7hi6lep1yc51ca.html?vid=h0018p9ihom')  # 腾讯视频琅琊榜


# 浏览器最大化

# diver.maximize_window()
#
# time.sleep(15)
# # diver.implicitly_wait(20)  # 智能等待中 这个不能是准确的 20秒
#
# diver.quit()


# 设置浏览器的宽高
# diver.get('http://m.mail.10086.cn')
#
# time.sleep(2)
#
# diver.set_window_size(480, 800)
#
# time.sleep(3)
#
# diver.quit()


# 找到对应的元素并且操作相应的按钮

# diver.find_element_by_id('kw').send_keys('selenium')
#
# diver.find_element_by_id('su').click()
#
# time.sleep(3)
#
# diver.quit()


# 前进后退操作


# first_url = 'http://www.baidu.com'
# second_url = 'http://www.handabao.com'
#
# diver.get(first_url)
# time.sleep(2)
#
# diver.get(second_url)
# time.sleep(3)
#
# diver.back()
# time.sleep(1)
#
# diver.forward()
# time.sleep(1)
#
# diver.quit()


# 键盘组合操作

# diver.get('http://www.baidu.com')
#
# diver.find_element_by_id('kw').send_keys('selenium')
#
# time.sleep(3)
#
# diver.find_element_by_id('kw').send_keys(Keys.COMMAND, 'a')
#
# time.sleep(3)
#
# diver.find_element_by_id('kw').send_keys(Keys.COMMAND, 'x')
#
# time.sleep(3)
#
# diver.quit()



# 鼠标右键操作

# diver.get('http://www.baidu.com')
#
# qqq = diver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[5]')
# qqq = diver.find_element_by_id('kw')
#
# ActionChains(diver).context_click(qqq).perform()
#
# diver.quit()


# 双击

# diver.get('http://www.baidu.com')
#
# qqq = diver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[5]')
#
# # qqq = diver.find_element_by_id('kw')
#
# ActionChains(diver).double_click(qqq).perform()
#
# diver.quit()


# 拖动

# element = diver.find_element_by_id('lg')
#
# target = diver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[7]')
#
# ActionChains(diver).drag_and_drop(element, target).perform()
#
# time.sleep(5)
#
# diver.quit()



# 找到一组 然后勾选上

# dr = webdriver.Firefox()
#
# file_path = 'file:///' + os.path.abspath('checkbox.html')
#
# dr.get(file_path)
# # 选择所有的 checkbox 并全部勾上
#
# checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')  # 注意这个方法是elements
# for checkbox in checkboxes:
#     checkbox.click()
#
# time.sleep(2)
# # 把页面上最后1个 checkbox 的勾给去掉
#
# dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()  # pop()方法能找到最后一个元素
#
# time.sleep(2)




# 如果html 中嵌套了 html 文件那么就需要 用如下两个方法来转换对应的 frame 或者是windows 后来操作

''' 嵌套的frame  windows 同样的道理
<iframe id="f1" src="inner.html" width="800",height="600"></iframe>

    <iframe id="f2" src="http://www.baidu.com" width="700"height="500"></iframe>

'''

# driver.switch_to_frame('f1')
# driver.switch_to_window()
# 同上 如果是二级菜单那么还是需要先定位 父类 然后再定位 到相应的元素. 具体看相应的 pdf吧.




# 执行js脚本

#格式 diver.execute_script(script, *args)

js1 = "var q=document.documentElement.scrollTop=1000"
js2 = "var q=document.documentElement.scrollTop=2000"
js3 = "var q=document.documentElement.scrollTop=3000"
js4 = "var q=document.documentElement.scrollTop=5000"
js5 = "var q=document.documentElement.scrollTop=5000"
js6 = "var q=document.documentElement.scrollTop=6000"

diver.execute_script(js1)
time.sleep(3)

diver.execute_script(js2)
time.sleep(3)

diver.execute_script(js3)
time.sleep(3)

diver.execute_script(js4)
time.sleep(3)

diver.execute_script(js5)
time.sleep(3)

diver.execute_script(js6)
time.sleep(3)

# print(diver.page_source)

# comments = diver.find_element_by_xpath('//*[@id="commentIframe1"]')

diver.switch_to.frame('commentIframe1')  # 这一句太太关键.马的!!!好久没弄出来就是因为这个.

# print(diver.page_source)

diver.find_element_by_xpath('//*[@id="loadMore"]').click()
time.sleep(2)

diver.find_element_by_xpath('//*[@id="loadMore"]').click()
time.sleep(2)

diver.find_element_by_xpath('//*[@id="loadMore"]').click()
time.sleep(2)
#
#
print(diver.page_source)


# print(comments)

# print(diver.page_source)
diver.quit()

#--------------------------------#



# print(type(diver.page_source))

# print(diver.page_source)

# js = "var q=document.documentElement.scrollTop=5000"

# diver.execute_script(js)

# html = diver.page_source

# print(html)

# print(diver.title)

# tr = r'<div class="content">(.*?)<!'
#
# chinese = re.findall(tr, html, re.S)
#
# print(len(chinese))
#
# for each in chinese:
#     print(each)
#
# # fw = open('/Users/zhangxianqiang/Desktop/qiushi.txt')
#
# with open('/Users/zhangxianqiang/Desktop/qiushi.txt', 'w') as fw:
#     for each in chinese:
#         fw.write(each)