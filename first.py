from math import *
from random import *
from time import sleep
import pyautogui

print('uyfjyg')
sifat = 22
#print(sifat)
sifat = 'biriani khay'
print(sifat)
num = 10
while num>=1 :
    print(num)
    num = num - 1

age = 23
if age == 23 :
    print("Oyea")
arr = [100,200,300]
for i in arr :
    print(i)
for i in range(10) :
    print(i)


def sum(num1,num2) :
    res = num1+num2
    return res

total = sum(10,10)

print('Ans is',total)


def id(*args):#like array
    print(args)
    for i in args :
        print(i)

id(12,13,14)

def buy(item,price):
    print('balance ',price)
    print(f'Balance after {item}',price)
buy('sunglass',1000)


#Built in
maximum = max(10,20,30,40,50)
print(maximum)

count = len([10,15])
print(count)

array = [10,20,30,40,50,60,70,80,90]
array.append(100)
print(array[0:9])
print(array[0:9:2])
print(array[9:0:-1])
print(array[:])
print(array[::-1])

if 10 in array:
    array.remove(10)
print(array[:])


index = array.index(40)
print(index)

def solve(a, b):
    return a**b
    
def puchi():
    print("Hiiiiii")
puchi()
result = solve(2, 4)
print(result)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_person(Name="Amir Khan", Age="45")

x = int(input())
y = int(input())
print(x+y)

name1 = 'sifat bs'
name2 = "sifat bs"
name3 = """SIFAT IS 
        THE KING 
        HEHE BOIS 
        I'M THE ONLYONE"""

print(name3)

for char in name2 :
    print(char)

if 'bs' in name2 :
    print("yes")

#tuple
toys = ('car','bike')
print(toys)
print(type(toys))
print(type(name2))

tuple2 = ([1,2,3],[4,5,6])
print(tuple2[1])

#set
numbers = [12, 56 , 98, 78, 56 , 12 , 6, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(12)
numbers_set.add(12)
numbers_set.add(12)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)

for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B)
print( A | B) #AUB

#dictionary
numbers = [12, 56 , 98, 78, 56, 12, 26, 98]
person1 = ['Kala Chan', 'kalipur', 23, 'student']
person = {'name': 'Kala Pakhi', 'address': 'Kaliapur', 'age': 23, 'job': 'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada pakhi'
value = person.get("job")
print(value)
person.pop('address')
print(person)
del person['age']
print(person)
for key, value in person.items():# special dictionary looping
    print(f'{key}: {value}')


#list with index
numbers3 = [12, 56 , 98, 78, 56 , 12 , 6, 98]
for i, num in enumerate(numbers):
    print(i, num)

# result = ceil(4.00001)
result = floor(4.9999)
print(result)
print(random())
print(randint(1,100))
sleep(4)
print(choice(['sakib', 'mash', 'mush', 'rid', 'musta']))

# lambda

# def doubled(x):
#     return x*2

doubled = lambda num : num * 2
squared = lambda num : num * num
result = doubled(44)
output = squared(9)
# print(result, output)

add = lambda x, y : x + y
sum = add(11,33)
# print(sum)
numbers = [12, 56 , 98, 78, 56 , 12 , 6, 98]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x: x*2, numbers)
squared_nums = map(lambda x: x*x, numbers)
print(numbers)
# print(list(doubled_nums))
print(list(squared_nums))

actors = [
    {'name': 'sabana', 'age': 65 },
    {'name': 'sabnoor', 'age': 45 },
    {'name': 'sabila noor', 'age': 30 },
    {'name': 'srabonti', 'age': 38 },
    {'name': 'shaon', 'age': 47 },
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
Fivers = filter(lambda actor : actor['age'] %5==0, actors)
# print(list(juniors))
print(list(Fivers))

cnt = {}
i = 1
if i not in cnt:
    cnt[i] = 1
else:
    cnt[i] += 1

print(cnt)