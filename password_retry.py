password = '123456'
x = 3
while True:
	pwd = input('please entry your password: ')
	if pwd == password:
		print('sign in suceesfully')
		break
	else:
		x = x - 1
		print('please try again!You have',x , 'more chance')
		if x == 0:
			break
