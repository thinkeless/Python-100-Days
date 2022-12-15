'''
用户身份验证

Version: 0.1
Author: Thinkless
'''
username = input('请输入用户名: ')
password = input('请输入密码: ')
if username == 'admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败')
