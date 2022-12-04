def emp(name, age):#positiona Arguments
    print("NAme=", Name, "AGe=",Age)
emp("harry")

#keyword argument: an alternative to positional arguments

def emp(Name, Age):
    print("Name=", NAme, "Age=",Age)
emp(Age=25, Name="harry")

#parameter with default values:
def emp(name, msg="welcome"):
    print("Hello",name,msg)
emp("harry")
