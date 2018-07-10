import sys

def threeIdiot(number):
    if int(number)% 3 == 0 and '3' in str(number):
        result = 'dump'
    elif '3' in str(number):
        result = 'stupid'
    elif int(number)% 3 == 0:
        result = 'idiot'
    else:
        result = 'smart'
    return result

if __name__ == '__main__':
    for i in sys.argv[1:]:
        if i.isdigit():
            print(threeIdiot(i))
        else:
            print('invalid')
