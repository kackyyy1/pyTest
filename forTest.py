from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username=browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password=browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_submit=browser.find_element_by_id('login-btn')
elem_submit.click()

#thタグの一番最初の一要素のみ取り出される
elem_th = browser.find_element_by_tag_name('th')
print(elem_th.text +"←これは一要素")

#thタグの全ての要素を取り出す
elems_th = browser.find_elements_by_tag_name('th')

#elemsはlist型
print(elems_th[1].text +"←配列に[1]を選択")

#listの要素を取り出すだけなら... xはWebElement型
for x in elems_th:
    print(x.text)

#for文の繰り返し回数を明示. yはint型
#rangeは1から起算し、要素0番目から取り出す
for y in range(5):
    print(elems_th[y].text)
    print(str(y)+"番目")

#for文で変数に格納
#ガラの配列を作成する.
keys = []

#for文で変数に格納
for z in elems_th:
    key = z.text
    keys.append(z)

for a in keys:
    print(a.text)