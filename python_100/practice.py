'''
a,b,c = 1,22,333
print(a,b,c,sep='@',end='/')
'''

'''
sites = ["Baidu","Tencent","Huawei","ZTE"]
for x in sites:
    if x == "Baidu":
        print("This company is Baidu")
        break
    elif x == "Tencent":
        print("This company is Tencent")
print("over")
'''

'''
import sys

list = [1,2,3,4]
it = iter(list)
for x in range(100):
    print(x)


list = [2,3,4,5]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''

'''
import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

for x in f:
        print(x, end=" ")
'''

'''
import math
def hello():
    print("hello")

hello()

def area(radius):
    return math.pi*radius**2

print(area(2))
'''

def sayHello(name):
    print("Welcome",name)

sayHello("zyk")




