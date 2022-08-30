from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username=browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password=browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_submit=browser.find_element_by_id('login-btn')
elem_submit.click()

elem_name = browser.find_element_by_id('name')
print(elem_name.text)

elem_company = browser.find_element_by_id('company')
print(elem_company.text)

elem_birthday = browser.find_element_by_id('birthday')
print(elem_birthday.text)

elem_come_from = browser.find_element_by_id('come_from')
print(elem_come_from.text)

elem_hobby = browser.find_element_by_id('hobby')
print(elem_hobby.text.replace('\n',','))