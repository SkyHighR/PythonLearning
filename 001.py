import math

print('test')
print('1'+'2')
print('Hel\nl0')
print('''yyyyyyyy
yyyyyyyy
yyyyyyyy
yyyyyyyy
yyyyyyyy''')
print('let\'s go')
#变量
test0 = 'hello,are you ok'
test1 = '你好吗'
print(test0+'tao')
print(test0+'zheng')
print(test1 + 'tao')
print(test1 + 'zheng')

#+-*/
calcure0 = math.sin(1)
calcure1 = math.cos(1)
calcure2 = math.log2(91)
print(calcure0)
print(calcure1)
print(calcure2)
a = -1
b = -2
c = 3
calcure3 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
calcure4 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(calcure3)
print(calcure4)


# 字符类型
my_wife = 'nbfnbfnfnbfibnfibnfbfbfb'
print(len(my_wife))
print(my_wife[1])

bi = True
bi1 = False

# 空值
none = None
print(type(none))
print(type(bi))
print(type(5.1515110))
print(type(5))