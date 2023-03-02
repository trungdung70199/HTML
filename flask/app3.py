id = input('IDを入力してください')
print(id)

pwd =  input('パスワードを入力してください')
print(pwd)

file = open('aloha.txt', 'r')
data = file.read()
file.close()

if id in data and pwd in data:
    print('IDとパスワードがデータの中にありました')



