id = input('IDを入力してください')
print(id)

pwd =  input('パスワードを入力してください')
print(pwd)

file = open('aloha.txt', 'r')
for line in file:
    if id in line and pwd in line:
        flag = 1
        break
    else:
        flag = 0
    
if flag==1:
    print('ID or password: OK!')
else:
    print('ID or password wrong')
file.close()





