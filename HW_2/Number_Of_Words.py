import re
import sys
dic={}

if (len(sys.argv)==1):
  string1= input('Type the first word to search:')
  string2 = input('Type the second word to search:')

if(len(sys.argv)==2):
  string1 = sys.argv[1]
  string2= ''
else:
  if (len(sys.argv)==3):
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
    print('First word not found')
if not(dic.get(string2)):
    print('Second word not found')