
def out_func(var):
    def inner_func():
        print(var)
    return inner_func

func = out_func("hello world")
func()