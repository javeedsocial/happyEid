import random

eid_strings = ['happy eid', 'congrats', 'happy days', 'god bles you']


for i in range(1,10):
  name = input('write a name: ')
  if name == 'followers':
    print ("wish you all good", name)
  else:
    print (random.choice(eid_strings), name)
  


