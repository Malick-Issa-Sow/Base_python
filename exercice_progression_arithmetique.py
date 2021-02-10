print("Progression Arithmetique")
#preparation du traitement
print("taper dans l'ordre le premier termes,la raison,le nbs de termes")
p,r,nt= int(input("premiere terme :")),int(input("raison :")),int(input("nbs terme :"))
#traitement
dt= (p+(nt-1))*r
s=(nt*(2*p+(nt-1)*r))/2
#edition du resultat
print("la progression arithmetique de ",nt,"termes ,de premiere termes ",p,"de raison",r,"a pour derniere termes ",dt,"et pour somme",s)
