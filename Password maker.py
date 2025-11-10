name=input("Enter full name: ").replace(" ","")
age=(input("Enter your age: "))
dob=(input("In which year you were born: "))
s1={"@","#","!","*","&","%","$"}
a=(name[0:3])
b=(age[1])
c=(dob[0:2])
d=(name[-7:-2])
s2=s1.pop()

print(f"Your password is: {a}{b}{c}{s2}{d}")
