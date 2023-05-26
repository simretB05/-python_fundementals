num=400
string='string'
boolean=True
var1=['string1','string2','string3','string4']
var2= [1,2,3,4,5]
print(num)
print(string)
print(boolean)

if(num > 10):
    print('number is larger than 10')
else:
    print('number is less than 10')

if(num<0 and  boolean==True):
    print('negative and True')
elif(num>0 and boolean ==False):
    print('positive and False')
elif(num>100 or boolean ==True):
    print('large and true')
else:
    print("I don't know")

for name in var1:
    print(name)
for number in var2:
    print('look at this', number)

def static_greeting():
    print('Simret')

static_greeting()

def dynamic_greeting(arg1):
    print('hello',arg1)
dynamic_greeting('simret')
dynamic_greeting('lula')
dynamic_greeting('lu')












    





