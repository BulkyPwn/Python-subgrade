# -*- coding=utf-8 -*-

'''
结论：
1.wrapper里的func为定义好的func本身(与其上方行装饰器无关)引用了同一个地址
2.outer内层中定义的函数被"隐藏"
3.outer中的func和刚进入inner时的func地址是相同的
Questions:
Q1：若结论3正确，outer中的func和刚进入inner时的func地址是相同的，可否说两个作用域中的func指向了同一地址？
Q1:是否函数内定义的函数的作用域只在此函数内？还是当此函数在局部中找到了对应函数即不会继续去全局中查找？
Q2:即使不加functools.wraps(f)，此程序中f的__name__也不会改变，为何有些程序中此值会改变？
'''


def outer(a):    #outer将在其内定义的内层函数全部隐藏;作用域
    print('outer_h')

    def inner(func):
        print('inner_h')

        print(func)
        print(func.__name__)

        from functools import wraps
        @wraps(func)                  #不加functools.wraps(f)此程序中f的__name__也不会改变，为何有些程序中此值会改变
        def wrapper1(*args,**kwargs):
            print("func()前地址信息为：{},name为{}".format(func,func.__name__))
            #print('outer_h')
            r = func(*args,**kwargs)
            #print('outer_t')
            print("func()后地址信息为：{},name为{}".format(func,func.__name__))
            #return r

        print('inner_t')
        return wrapper1

    def inner1():
        print('UNX')

    print('outer_t')
    return inner

@outer(a=None)
def max_x_y(x,y):
    s = lambda x,y:x if x>y else y
    print(s)
    print(s(x,y))

def main():

    max_x_y(8,9)
    #print(s) s存储上述函数中lambda表达式的地址
    print(max_x_y)
    #print(max_x_y(8,9))

    max_x_y(8,101)

    print()
    print("外层max_x_y实际地址信息为{}".format(max_x_y))
    print()
    print(outer)

    #print(inner)
    '''
    console log:
    Traceback (most recent call last):
      File "D:/Python Projects/venv/share/decorater_func_return_myth.py", line 69, in <module>
        main()
      File "D:/Python Projects/venv/share/decorater_func_return_myth.py", line 49, in main
        print(inner)
    NameError: name 'inner' is not defined
        '''

    #print(outer.inner)
    '''
    console log : 
    outer_h
    Traceback (most recent call last):
      File "D:/Python Projects/venv/share/decorater_func_return_myth.py", line 57, in <module>
        main()
    outer_t
    inner_h
      File "D:/Python Projects/venv/share/decorater_func_return_myth.py", line 50, in main
        print(outer.inner)
    AttributeError: 'function' object has no attribute 'inner'
    <function max_x_y at 0x0000021545692E18>
    inner_t
    '''

if __name__ == '__main__':
    print('main()执行：')
    main()
else:  #调用此模块的模块 名称
    print(__name__)

