from queue import PriorityQueue
import re
import requests as req

kkk = input()
url = 'https://api.agify.io/?name={}'.format(kkk)

response = req.get(url).json()

print(type(response))
name = response['name']
age = response['age']
count = response['count']


print('이름이', name , '인 사람의 나이는' , age , '입니다.')
