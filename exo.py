'''def table_mutiplicate(n,min=1,max=12):
    if min > max:
        print("ERROR: la valeur min est superior à la valeur max")
        return
    for i in range(min, max+1):
        print(i, "x" ,n ,"=" ,i*n)
table_mutiplicate(7)        
table_mutiplicate(50,-36,48)**Exercice 9 :**<jupyter_code># Ex
def questinnaire ():
    print ("Quel est la capitale du Bénin ? ")
    a= print("a=Togo")
    b=print("b=Lokossa")
    c=print("c=Cotonou")
    d=print("d=Porto-Novo")
    R=input("choisissez la bonne reponse:")
    if R=="d" :
        print ("Vous aviez choisi la bonne reponse")
    else:
        print("ERROR: Mauvaise reponse" ,"vous venez de signer votre arret de mort")
questinnaire()
    
'''


'''def questinnaire(question,r1,r2,r3,r4,choix_rep):
    
    print("Question",question)
    print("a",r1)
    print("b",r2)
    print("c",r3)
    print("d",r4)
    
    R=input("choisissez la bonne reponse:")
    if R==choix_rep:
        print ("Vous aviez choisi la bonne reponse")
    else:
        print("ERROR: Mauvaise reponse" ,"vous venez de signer votre arret de mort")
questinnaire ("Quel est la capitale du Bénin ? ","Togo","Lokossa","Cotonou","Porto-Novo","d")
'''
Noms_distances=[("toto",1.4),("rory",1.5),("ryry",0.5)]
Noms_distances_min=Noms_distances[0][1]
for i in range(len(Noms_distances)):
    if Noms_distances [i][1]< Noms_distances_min:
        Noms_distances_min=Noms_distances[i][1]
        print( Noms_distances[i][1])
        print( Noms_distances[i][0])