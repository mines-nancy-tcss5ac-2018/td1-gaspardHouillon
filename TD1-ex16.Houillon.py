#Exo 16
def solve(n):
    s=0
    nb=2**n
    L=list(str(nb))  #Je d�coupe ma liste digit par digit (transform� en chaine de caract�re)
    for i in range(len(L)):
        L[i]=int(L[i]) #Conversion str en int
        s+=L[i] #Je somme les digits
    
    return s
assert(solve(15)==26)
print(solve(10000))