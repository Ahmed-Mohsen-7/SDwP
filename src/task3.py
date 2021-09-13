import time,contextlib,io
from inspect import signature,getsource

rank={}
class decorator_3:
    def __init__(self,func):
        
        self.func= func
        self.count= 0
        
    def __call__(self,*args,**argw):
        global rank
        self.count+= 1
        frame = inspect.currentframe()
        arg, _, _, values = inspect.getargvalues(frame)        
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            self.func(*args,**argw)
        rank[self.func.__name__]=time.time()-start    
        output = f.getvalue()
        
        with open('output.txt','a') as n:
            n.write('{} call {} in {} sec\n'.format(self.func.__name__,self.count,time.time()-start))        
            n.write('Name:\t{}\n'.format(self.func.__name__))  
            n.write('Type:\t{}\n'.format(type(self.func)))
            n.write('Sign:\t{}\n'.format(inspect.signature(self.func)))        
            n.write('Args:\t positional: {} \n\t Keyworded:{}\n'.format(values['args'],values['argw']))        
            n.write('Doc:\t{}\n'.format(self.func.__doc__))     
            print('Source:\t', inspect.getsource(self.func))
            n.write('Output:\t {}\n\n\n'.format(output))        
        if len(rank)==4:   #This condition to print the table once all 4 functions are called
            les=sorted(rank.items(),key = lambda x: (x[1],x[0]))
            print("PROGRAM  |  RANK  |  TIME ELAPSED")
            for i in range(len(les)):
                print (les[i][0], '       ',i+1,'      ',les[i][1])            
            
        
