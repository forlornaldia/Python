import random
print('''                                                  
      888888888888  88888888888  ad88888ba  888888888888  
           88       88          d8"     "8b      88       
           88       88          Y8,              88       
,adPPYba,  88       88aaaaa     `Y8aaaaa,        88       
I8[    ""  88       88"""""       `"""""8b,      88       
 `"Y8ba,   88       88                  `8b      88       
aa    ]8I  88       88          Y8a     a8P      88       
`"YbbdP"'  88       88888888888  "Y88888P"       88                                                                                                                                                                
''')

#sTEST

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','_','+','=','~','`']
cha = ''
ba=[]
for item in characters:
  cha+=item
password = input("Enter a four digit password. ").lower()
pulsing = True
x=0
q = 11
w=11
e=11
r=11
tens = 0
ones =1 
hundreds = 0
thousands = 0
while pulsing:
    
  x+=1
  if r == 63:
    e+=1
    r=11
  if e == 63:
    w+=1
    e=11
  if w == 63:
    q+=1
    w=11
    
  pulse =''
  a = characters[q-11]
  b = characters[w-11]
  c = characters[e-11]
  d = characters[r-11]
  pulse +=a
  pulse+=b
  pulse+=c
  pulse+=d
    
    
    
  if pulse == password:
    print("Pulse "+str(x))
    print("Pulse: "+pulse)
    break
  else:
    print("Pulse: "+pulse)
      
  r+=1