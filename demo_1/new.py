name ="baby"
age=29
city="chennai"

def Check_palindrome(mystr):
    newstr=''

    for each in mystr:
     if each.isalpha():
        newstr=newstr+each.lower()
    print(newstr)

    if newstr == newstr[::-1]:
      return True                #return call,reuseable many time
    else:
      return False
    

def remove_duplicate(a):
     b=[]
     for x in a:
      if x not in b:
        b.append(x)
     return b