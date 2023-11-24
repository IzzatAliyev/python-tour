'''
# becoming exception
string = 'hello'
num = int(string)
print(num)
'''
'''
try:
    inputValue = input('Enter the number: ')
    num = int(inputValue)
    print(num ** 2)
except: # it's catching all exceptions
    print('exception!!!')
finally:
    print('code end here')
'''

# BaseException is main exception class
# Exception is mostly use for creating own exception class

'''
try: 
    inputValue = input('Enter the number: ')
    num = int(inputValue)
    print(num**2)
except ValueError as ex:
    print('Value exception : ', str(ex))
except (ZeroDivisionError, OSError) as ex:
    print("Other exceptions : ", str(ex))
except BaseException as ex:
    print('Caught an exception : '. str(ex))
finally:
    print('Code End Here')
'''

'''
try:
    inputValue = input('Enter the number: ')
    num = int(inputValue)
    if num == 0:
        raise Exception('num is 0')      # throw the exception
    print(num**2)
except ValueError as ex:
    print('Value exception : ', str(ex))
except Exception as ex:
    print('Exception : ', str(ex))
finally:
    print("Program end")
'''