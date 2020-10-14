import time
import random
import base64
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" 
}

chrome_options = Options()
# chrome_options.add_argument("--headless")  
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

browser = webdriver.chrome.webdriver.WebDriver(executable_path='./chromedriver', chrome_options=chrome_options)

time.sleep(random.randrange(1,2))

browser.get("https://www.google.com/search?q=celebrity+with+eyeglasses&sxsrf=ALeKk02c-tNSICRR_ezaabExnZX1ShHNZQ:1602526294550&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi5lp7U06_sAhXrkYsKHYHFBWAQ_AUoAXoECBUQAw&biw=1869&bih=921")

time.sleep(4)

print(len(browser.find_elements_by_css_selector('img')))

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(4)
print(len(browser.find_elements_by_css_selector('img')))
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(4)
print(len(browser.find_elements_by_css_selector('img')))


has_glasses_items = browser.find_elements_by_css_selector('img')

for i in range(len(has_glasses_items)):
    item = has_glasses_items[i]
    src = str(item.get_attribute('src'))
    if src == 'None':
        print('sdfsdfsdfsdf')
    if src is not None:
        print(i)
        filename = str(i) + '-1.jpg'
        directory = './01/'
        if src.startswith('data'):
            src = src.replace('data:image/jpeg;base64,', '')
            imgdata = base64.b64decode(src)
            with open(directory + filename, 'wb') as f:
                f.write(imgdata)
        elif src.startswith('https://encrypted'):
            r = requests.get(src, allow_redirects=True)
            with open(directory + filename, 'wb') as f:
                f.write(r.content)

time.sleep(2)

browser.stop_client()
browser.close()
browser.quit()


# class Parser():

#     auth_page:str = ''
#     auth_username:str = ''
#     auth_password:str = ''

#     chrome_driver_path = ''
#     options = None
#     browser = None 

#     def parse_category(self, category):
#         try:
#             self.browser.get(category['url'])

#             items = self.browser.find_elements_by_css_selector('[itemtype="http://schema.org/Product"]')

#             result_items = []

#             for i in range(len(items)):
#                 element = items[i]
#                 i = {
#                     'id': '',
#                     'title': '',
#                     'price': '',
#                     'url': ''
#                 }

#                 try:
#                     item_id = element.get_attribute('data-marker').replace('item-wrapper(', '').replace(')', '')
#                     title = element.find_element_by_css_selector('[data-marker="item/link"]').text.lower()
#                     url = element.find_element_by_css_selector('[data-marker="item/link"]').get_attribute('href')
#                     price_text = element.find_element_by_css_selector('[data-marker="item/price"]').text.lower()

#                     price = int(price_text.replace(' ', '').replace('₽', ''))

#                     i['id'] = item_id
#                     i['title'] = title
#                     i['url'] = url
#                     i['price'] = price

#                     result_items.append(i)

#                 except Exception as ex:
#                     print(ex)
#                     continue

#             return result_items

#         except Exception as e:
#             print(e)
#             return []
