# inout
username = input('Please input your name: ')
user_age = input('Please input your age: ')
print('Hello,' + username + ',you are ' + user_age + ' years old.')

# BMI
height = float(input('Please input your height: '))
weight = float(input('Please input your weight: '))
BMI = weight / (height ** 2)
print('Your BMI is: ', BMI)

# if
if BMI < 18.5:
    print('You are too thin.')
elif BMI < 25:
    print('You are normal.')
elif BMI < 28:
    print('You are a little fat.')
elif BMI < 32:
    print('You are fat.')
else:
    print('You are too fat.')

happy = float(input('Please input your happy point: '))
if happy > 100:
    print('You are too happy.')
    print('^_^')
else:
    print('You are not happy enough.')

# double if
if happy > 100:
    if BMI < 20:
        print('You are too happy and too thin.')
    else:
        print('You are too happy.')
else:
    if BMI < 20:
        print('You are too thin.')
    else:
        print('You are normal.')
    















