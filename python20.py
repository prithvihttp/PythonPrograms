'''a=input("")
b=input("")
c=a+b
print('{} plus {} equal {}'.format(a,b,c))

#comparsion operator
str1==str2
str1>str2

str1="Hello"
str2="hello"
print(str1==str2)
print(str1>str2)

...
S=''
for i in range(0,5):
    n=input()
    S+=' '+n
print(S.split())
c="TCS, infosys,google, hcl, linux"
c.split(",")
for i in c:
    print(end="")
print(c)'''
a=str(input("a: "))
print(a.isalnum())
print(a.isalpha())
print(a.islower())
print(a.isupper())
print(a.isdigit())
print(a.isspace())
print(a.endswith("o"))
print(a.startswith("h"))#startswith(str strl)
print(a.find("f"))#int find(str strl)lowest index where string strl strats in the
#string or return -1
print(a.rfind("1"))#int rfind: highest index
print(a.count("1"))#count-->return the number of occurances of the string
print(a.capitalize())
print(a.lower())
print(a.upper())
print(a.title())


