from faker import Faker

myfake = Faker() 
print(myfake.name() )
print(myfake.address() )
print(myfake.text() )
print(myfake.state()) # 미국의 주이름 
print(myfake.sentence()) # 문장 
print(myfake.random_number())

## Korean
myfake2 = Faker('ko_KR') 
print(myfake2.name()) 
print(myfake2.address()) 
print(myfake2.text()) 
# print(myfake2.state())  #안됨
print(myfake2.sentence()) 
print(myfake2.random_number())

## 하나 계속 유지
myfake3 = Faker() 
myfake3.seed(1) 
print(myfake3.name()) 
print(myfake3.address()) 
print(myfake3.text()) 
print(myfake3.state()) 
print(myfake3.sentence()) 
print(myfake3.random_number())


