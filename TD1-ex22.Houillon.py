def nom(prenom):
    sc=0
    for j in range(1,len(prenom)-1):  #On ne lit pas la premi�re lettre ni la derni�re car se sont des guillemets
        
        sc+=ord(prenom[j].lower())-96    #On utilise le code ascii auquel on retranche le "d�calage" pour attribuer � nchaque lettre son nombre
    return sc


def solve():
    f=open('names.txt','r')
    L=[]
    for ligne in f:
        ligne=ligne.split(',')
        ligne.sort()   #On trie le fichier
    sco=0  
    st=0
    for i in range(len(ligne)):
        sco=nom(ligne[i]) #On applique nom
        st=st+sco*(i+1)  #On multiplie par le rang !!! D�cal� de 1
    return st
            
assert(nom('"Colin"')==53)
print(solve())