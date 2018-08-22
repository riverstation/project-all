# myList = [
#     ('a',''),
#     ('b',''),
# ]

# for k,v in myList:
#     print(k,v)

# myDict = {'a':'','b':''}
# for k,v in myDict.items():
#     print(k,v)

# print(dict(myList))

class A:
    password_hash = 0

    @property
    def password(self):
        # return self.password_hash
        raise AttributeError('属性不存在')
    @password.setter
    def password(self, password):
        self.password_hash = password
# a = A()
# print(a._A__abc)
# print(A._A__abc)
# print(a.get_age())
# print(a.age)
# print(A.__dict__)
# '_A__abc': 'abs'



# 1 什么是私有属性
# 2 为什么要使用 装饰器
# 3 把这个例子 改成我们要使用的password加密的过程（不是加密）
# 4 这俩个的相似处


# class A:
#     # __slots__ =
#     __abc = ''
#     @property
#     def abc(self):
#         pass
#     @abc.setter
#     def abc(self,val):
#         pass

# a = A()
# a.set_abc('xxx')


import os

print(os.path.split('/home/xlg/1.jpg'))




























