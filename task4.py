import time
def decorator_4(fun):
    def wrapper(*args,**argw):
        start = time.time()
        try:
            fun(*args,**argw)
        except Exception as error:
            print('see log file for detials')
            with open('log.txt','a') as n:
                n.write(str(error)+'\n')                             
                n.write(time.strftime("%r-%m-%d %H:%M:%S")+'\n')             
        
    return wrapper

