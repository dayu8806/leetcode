x = 10               # 全局变量

def outer():
    y = 5           # 外层函数作用域变量

    def inner_read():    
        # 只读 x、y，不赋值，可以直接访问
        print(x, y)

    def inner_write_y():
        # 想修改 y，就必须加 nonlocal
        nonlocal y  
        y += 1

    def inner_write_x():
        # 想修改 x，就要加 global
        global x    
        x += 1

    inner_read()
    inner_write_y()
    inner_read()
    inner_write_x()
    print(x)

outer()
