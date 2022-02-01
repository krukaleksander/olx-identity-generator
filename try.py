from selenium import webdriver
from time import sleep
cookies_list = []
number_of_identity = 2

def getCookies():
    driver = webdriver.Chrome()
    driver.get("https://www.olx.pl/oferta/praca/sprzedawca-sklep-CID4-IDHBgxd.html#8569bd12c5;promoted")
    sleep(10)
    auth_cookie = driver.get_cookie('a_access_token')
    device_id = driver.get_cookie('deviceGUID')
    cookie_object = {"auth": f'Bearer {auth_cookie["value"]}', "deviceId": f'{device_id["value"]}'}
    cookies_list.append(cookie_object)
    driver.delete_all_cookies()
    driver.close()

[getCookies() for _ in range(number_of_identity)]

print(cookies_list)
# console.log({
#     auth: `Bearer ${cookieObj.a_access_token}`,
#     deviceId: cookieObj.deviceGUID
# })

