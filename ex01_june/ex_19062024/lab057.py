def outer_func():
    var1=30
    def inner_func():
        print(var1)
    inner_func()
outer_func()