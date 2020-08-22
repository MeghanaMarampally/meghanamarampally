import string
def pangram(str):
    letters="abcdefghijklmnopqrstuvwxyz"
    for char in letters:
        if char not in str.lower():
            return False
        else:
            return True
string="the five boxing wizards jump quickly"
if(pangram(string)==True):
    print("the entered string is a pangram")
else:
    print("not a pangram")

    
        
