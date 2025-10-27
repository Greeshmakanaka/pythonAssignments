def dec_func(func):
    def wrapper(*args, **kwargs):
        print("before dec_func wrapper")
        result = func(*args, **kwargs)
        print("after dec_func wrapper")
        return result
    return wrapper

def android_3(func):
    def wrapper(*args, **kwargs):
        print("before android_3 wrapper")
        result = func(*args, **kwargs)
        print("after android_3 wrapper")
        return result
    return wrapper

def android_4(func):
    def wrapper(*args, **kwargs):
        print("before android_4 wrapper")
        result = func(*args, **kwargs)
        print("after android_4 wrapper")
        return result
    return wrapper

@android_4
@android_3
@dec_func
def add(x, y):
    print("add function")
    return x + y

print(add(5, 3))
