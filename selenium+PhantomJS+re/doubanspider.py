
from selenium import webdriver
import time
from lxml import etree

url = 'https://movie.douban.com/'

driver = webdriver.Firefox()
# driver = webdriver.PhantomJS()


driver.get(url)

time.sleep(0.2)

js1 = "var q=document.documentElement.scrollTop=1000"

driver.execute_script(js1)

driver.find_element_by_xpath('//*[@id="gaia_frm"]/div[1]/div[1]/label[4]').click()

time.sleep(0.2)

clickItem = driver.find_element_by_xpath('//*[@id="gaia"]/div[4]/a')

for _ in range(1, 10):
    clickItem.click()
    time.sleep(0.5)

selector = etree.HTML(driver.page_source)

content = selector.xpath('/html/body/div[3]/div[1]/div/div[2]/div[4]/div[4]/div/a')

for each in content:
    print(each.xpath('p/text()')[0].strip() + '------> 分数:' + each.xpath('p/strong/text()')[0] + '\n')


# /html/body/div[3]/div[1]/div/div[2]/div[4]/div[4]/div/a

time.sleep(30)

driver.quit()


