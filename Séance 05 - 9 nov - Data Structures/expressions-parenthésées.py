expression = input()

L=[]


for i in expression:
    if not i in "(){}[]":continue
    L.append(i)
    if len(L)<2:continue
    currentString = L[-2]+L[-1]
    
    if currentString=="[]":
            L.pop()
            L.pop()
            continue
    elif currentString=="{}":
            L.pop()
            L.pop()
            continue
    elif currentString=="()":
            L.pop()
            L.pop()
            continue

if len(L)>0:
    print("false")
else:
    print("true")
