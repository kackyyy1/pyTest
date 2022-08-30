from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username=browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password=browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_submit=browser.find_element_by_id('login-btn')
elem_submit.click()

#thタグの全ての要素を取り出す
elems_th = browser.find_elements_by_tag_name('th')

#elemsはlist型
print(elems_th[1].text +"←配列に[1]を選択")

#listの要素を取り出すだけなら... xはWebElement型
for x in elems_th:
    print(x.text)

#tdタグの全ての要素を取り出す
elems_td = browser.find_elements_by_tag_name('td')

#listの要素を取り出すだけなら... xはWebElement型

for x in elems_td:
    print(x.text)

#for文の入れ子で文字連結
#sep引数＝区切り文字を指定できる。要素間は,で区切る。これで文字整形可能
for x in elems_th:
    for y in elems_td:
        print(x.text,y.text, sep='=')

#end引数＝末尾に出力するものを指定。これでcsv化できる
for x in elems_th:
    print(x.text,end=",")

print()
for y in elems_td:
    print(y.text.replace("\n"," "), end=",")        
        

