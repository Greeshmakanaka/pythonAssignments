def outer_func(n):                      
    def dec_func(func):              
        def wrapper(*args, **kwargs): 
            for i in range(n):
                print(func(*args,**kwargs))
        return wrapper
    return dec_func

@outer_func(3)
def add(x,y):
    return x+y
@outer_func(2)
def mul(x,y):
    return x*y
@outer_func(4)
def sub(x,y):
    return x-y
add(4,8)
mul(5,6)
sub(8,3)