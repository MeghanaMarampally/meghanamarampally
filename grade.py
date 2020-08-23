s1=eval(input("enter the marks in first subject:"))
s2=eval(input("enter the marks in second subject:"))
s3=eval(input("enter the marks in third subject:"))
s4=eval(input("enter the marks in fourth subject:"))
s5=eval(input("enter the marks in fifth subject:"))
s6=eval(input("enter the marks in sixth subject:"))
p=((s1+s2+s3+s4+s5+s6)/800)*100
if(p>=75):
    print('grade = A+')
if(p>=60 and p<75):
    print('grade = A')
if(p>=50 and p<60):
    print('grade = B')
if(p>=40 and p<50):
    print('grade = C')
if(p<40):
    print('grade = FAIL')
