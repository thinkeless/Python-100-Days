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

'''
判断输入的边长能否组成三角形，如果能请计算出三角形的周长和面积

Version: 0.1
Author: Thinkless
'''
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('周长为:{0}'.format(a + b + c))
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b ) * (s - c)) ** 0.5
    print('面积为：{0}'.format(area))
else:
    print('不能构成三角形')

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')