def mystrip(s):
    space=[' ','\t','\n','\r']
    start=0
    for i in range(len(s)):
      if s[i] not in space:
        start=i
        break
    else:
      return ""
    end=len(s)-1
    for i in range(len(s)-1,-1,-1):
      if s[i] not in space:
        end=i
        break
    return s[start:end+1]

text=input("please enter your text:")
class_srip= mystrip(text)
print("remove extra spaces:", class_srip)
    
    