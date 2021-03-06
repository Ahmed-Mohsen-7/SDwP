import time,contextlib,io
def decorator_1(fun):
    def wrapper(*args,**argw):
        wrapper.count+=1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            fun(*args,**argw)
        end = time.time()
        print('{} call {} in {} sec'.format(fun.__name__,wrapper.count,end-start))
    wrapper.count=0
    return wrapper

