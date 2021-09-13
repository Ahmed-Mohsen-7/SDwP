import time,io
import inspect
import contextlib

def decorator_2(fun):
    def wrapper(*args,**argw):
        wrapper.count+=1
        frame = inspect.currentframe()
        arg, _, _, values = inspect.getargvalues(frame)
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            fun(*args,**argw)
        output = f.getvalue()
        print('{} call {} in {} sec'.format(fun.__name__,wrapper.count,time.time()-start))
        print('Name:\t',fun.__name__)
        print('Type:\t',type(fun))
        print('Sign:\t',inspect.signature(fun))
        print('Args:\t positional: {} \n\t Keyworded:{}'.format(values['args'],values['argw']))
        print('Doc:\t',fun.__doc__)
        print('Source:\t', inspect.getsource(s))      #This method may result in an error, it has something to do with python itself not the code
        print('Output:\t {}'.format(output)) 
        
    wrapper.count=0
    return wrapper

