
'''def discount(age, isMember, isResident):
    if age<12 or age>=65 or isMember==True or isResident==True:
        print("qualified")
    else: print("unqualified")
discount(11, isMember=False, isResident=False)'''
""" x=3
y=float(3)
print(x,y) """
""" values = [1,2.23,5,7,2,30,15,12]
print(values[7])
for i in values:
    print(i) """
""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """


'''def discount(age, ismember, isresident):
    if age>=65 or age<12 or ismember==True or isresident==True: 
        print("qualified")
    else:
        print("unqualified")
discount(12, False, False)'''
'''x = 3
y = float(3)
print(x,y)
'''
'''values = [1,2.23,5,7,2,30,15,12]
print(values)
for i in values:
    print(i)
print(values[7])'''
'''def hh(x):              
    sentence=x
    ff=sentence.split()
    cou=0
    for i in ff: 
        cou+=1
    print(cou)
ask=input("print sentence")
hh(ask)'''
'''number=56
if number % 2 == 0:
    print("even")
else: 
    print("odd")'''
'''bill=float(input('Subtotal'))
Quality=input('Service quality')
x="tippercentage"
if Quality=="bad":
    print(x)
elif Quality=="okay":
    print(x)
    x=.15*bill
elif Quality=="Good":
    print(x)
    x=.2*bill
elif Quality=="Great":
    print(x)
    x=.25*(bill)
Total=bill+x
Quality="Great"
print(Total)'''

'''def factors(x):
   print(x)
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

Number=int(input("What is your number"))
factors(Number)'''


GCF = 0
Num1 = int(input("1st number:"))
Num2 = int(input("2nd number:"))

for i in range(1, Num1+1):
    if Num1 % i == 0 and Num2 % i == 0:
        GCF = i
print({GCF})