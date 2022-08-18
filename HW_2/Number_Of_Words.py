import re
import sys
dic={}

if not (sys.argv):
  string1= input('Digite la primera palabra:')
  string2 = input('Digite la segunda palabra:')

if(sys.argv):
  string1 = sys.argv[1]
  string2 = sys.argv[2]


with open('romeo.txt') as file:
  for line in file:
    line = re.sub(r'[^\w\s]',' ',line)
    for word in line.split():
      if(word.lower()==string1.lower() or word.lower()==string2.lower() ):    
          dic.setdefault(word.lower(), 0)
          dic[word.lower()] += 1

print(dic)
if not (dic.get(string1)):
    print('Palabra 1 no encontrada')
if not(dic.get(string2)):
    print('Palabra 2 no encontrada')