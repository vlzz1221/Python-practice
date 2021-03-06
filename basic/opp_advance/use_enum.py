# -*- coding: utf-8 -*-
from enum import Enum, unique

# Month =  Enum('Month', ('One', 'two'))

# print(Month)
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1


# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender


# # 测试:
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

# print(day1)
# print(Weekday.Tue)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(day1 == Weekday.Mon)
# print(day1 == Weekday.Tue)
# print(Weekday(1))
# print(day1 == Weekday(1))
# print(Weekday(7))

for name, day in Weekday.__members__.items():
    print(' %s ===> %s ' % (name, day))