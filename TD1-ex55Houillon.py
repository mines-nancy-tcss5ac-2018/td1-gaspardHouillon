def palyndrome(m):
    l=list(str(m))
    for i in range(len(l)//2):
        if l[i]!=l[-(i+1)]:
            return False
    return True

def Tychel(p):
    while not palyndrome(p):
        
    