import time
# decorator
def timer(func):
    def innerfunc():
        print('start')
        start = time.time()
        func() #main func
        print('end')
        end = time.time()
        print(f'result is {end-start}')
    return innerfunc

@timer
def looper():
    for i in range(100):
        print(i)
    print('end')
    
@timer
def whiler():
    i=0
    while i < 100:
        print(i)
        i+=1
    print('end')
    
looper()
print('************************')
whiler()