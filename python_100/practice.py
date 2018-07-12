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

'''
def sayHello(name):
    print("Welcome",name)

sayHello("zyk")
'''

#可变参数
'''
def changeme(mylist):
    "修改已有列表"
    mylist.append([1,2,3,4])
    print("函数内",mylist)
    return

list = [12,23,34]
changeme(list)
print("函数外",list)
'''

#指定参数
'''
def jiacheng(a,b,c):
    print("a",a)
    print("b",b)
    print("c",c)

a = "aaa"
b = "bbb"
c = "ccc"

jiacheng(a,b,c)
jiacheng(a=b,b=c,c=a)
'''


#缺省函数
def showInfo(name,age=23):
    print("name",name)
    print("age",age)

name1 = "jack"
age1 = 34

name2 = "Bob"
showInfo(name1,age1)
showInfo(name2)



