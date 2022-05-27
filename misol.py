def katta_son(x,y,z):
  if x>y and x>z :
    print(x)
  elif y>x and y>z:
    print(y)
  else:
    print(z)
katta_son(7,10,7)

def dic_matn(dic):
   while True:
     for x in  dic:
       x.title()
   return x
    
Avto={
  'nomi':'gm',
  "model":"malibu"
}
y = Avto.values()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

z= car.values()

def sonlar(list):
  new_list=[]
  for num in list:
    if num/2==0:
      new_list+=[num]
  return new_list  

sigir= [7,8,6,5,9,1,7,3,2,5,45,44,]
print(sigir)
print(sonlar(sigir))