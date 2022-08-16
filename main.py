dic={}

with open('words.txt') as file:
  for line in file:
    for word in line.split():
      dic.setdefault(word.lower(), 0)
      for clave,valor in dic.items():
        if(clave.lower()==word.lower()):
          dic[clave.lower()] += 1

mayor=0
clavemayor=''
for clave, valor in dic.items():
  if (valor>mayor):
    clavemayor=clave
    mayor=valor
print('La palabra que más se repite es "', clavemayor , '" y se repite:', dic.get(clavemayor), 'veces.')