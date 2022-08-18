dic={}

with open('words.txt') as file:
  for line in file:
    for word in line.split():
      dic.setdefault(word.lower(), 0)
      for key,value in dic.items():
        if(key.lower()==word.lower()):
          dic[key.lower()] += 1

aux=0
key_repeated=''
for key, value in dic.items():
  if (value>aux):
    key_repeated=key
    aux=value
print('La palabra que más se repite es "', key_repeated , '" y se repite:', dic.get(key_repeated), 'veces.')