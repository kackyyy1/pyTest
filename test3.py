import pandas as pd
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username=browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password=browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_submit=browser.find_element_by_id('login-btn')
elem_submit.click()

#thタグの全ての要素を取り出す(List型)
elems_th = browser.find_elements_by_tag_name('th')

#tdタグの全ての要素を取り出す(List型)
elems_td = browser.find_elements_by_tag_name('td')

#空のDataframeを定義（pandasモジュールのインスタンスを使用する）
df = pd.DataFrame()

#空の配列を作成する.　これはListの要素をstrに変換し格納する用
keys = []
values = []

#各要素をstingで配列にぶちこみ直す
for x in elems_th:
    key = x.text
    keys.append(key)

for y in elems_td:
    value = y.text.replace("\n","、")
    values.append(value)

#要素がちゃんとstrで標準出力されることを確認する
print(keys,values)

#DataFrameのカラムを定義する
df["項目"] = keys
df["値"] = values

#定義したDataFrameイメージを標準出力してみる
print(df)

#csvに書き出し. indexは項番（１～）
df.to_csv('講師情報.csv', index=False)

#行でcsvに書き出したいよね...そんなときはインスタンス.Tで行と列を入れ替えることができる！！
print(df.T)
df.T.to_csv('講師情報＿行単位.csv', index=False)


###おまけ###
###課題：[]内を消してcsv化する方法
#”項目”とか”値”とかいらなくね？ってときは、[]内を空白にすればよさげ
df_noTitle = pd.DataFrame()
#DataFrameのカラムを定義する
df_noTitle[""] = keys
df_noTitle[""] = values

#定義したDataFrameイメージを標準出力してみる
print(df_noTitle)

#csvに書き出し. indexは項番（１～）
df_noTitle.to_csv('講師情報_notitle.csv', index=False)

#行でcsvに書き出したいよね...そんなときはインスタンス.Tで行と列を入れ替えることができる！！
print(df_noTitle.T)
df_noTitle.T.to_csv('講師情報＿行単位_notitle.csv', index=False)