password_file = open('SecretPasswordFile.txt')
secret_password = password_file.read()
print('Enter your password.')
typed_password = input()
if typed_password == secret_password:
    print('Access granted')
elif typed_password =='12345':
    print('That password is one that an idiot puts on ther luggage.')
else:
    print('Access denied')
