#Partie Entree

#Saisie du type de PL
print("Votre PL est une maximisation ou une minimisation ?")
while True:                                                                
    print("Choisissez entre 1 et 2 : ")
    x=int(input("1. Min \n 2. Max \n").strip())          
    if x==1:
        type="min"                                                                                              #la variable type contient le type du pb: min ou max
        break
    if x==2:
        type="max"
        break
    else:
        print("veuillez saisir 1 ou 2 \n ")
                                                                            

#saisie de la fct obj

c=[]                                                                        #liste des coefficient Ci                                                
while True:                                                               
    n=int(input(" nombre de variables de decisions : "))              
    if n>0:                                                             #n contient le nbr de VD
        break
    else:
        print("Veuillez saisir un nombre positif \n")
                                                                            

for i in range(n):                                                                                                                                                                                              
        variable1=float(input(f" le coeff {i+1} de la fonction objectif \n"))
        c.append(variable1)

#saisie des contraintes

while True:                                                                                           
    m=int(input(" le nombre de contraintes : \n"))                # m contient le nombre de contraintes                             
    if m>0:
        break
    else:
        print("veuillez saisir un nombre positif\n")
                                                                        


b=[]                                                                     #b[] les valeurs de bj
a=[]                                                                     #a[] conient les valeurs des coefficients aij
operateur=[]                                                             #operateur[] contient l'operateur de chaque contrainte 
for j in range(m):                                                       
    l=[]                                                             
    for i in range(n):
            variable2=float(input(f" le coeff {i+1} de la contrainte {j+1} \n"))      
            l.append(variable2)
    
    a.append(l)
    
    while True:         
        variable3=input(f"le signe de la contrainte {j+1} : \n").strip()       
        if variable3 in ["=",">=","<="]:
            operateur.append(variable3)
            break
        else:
            print("Veuillez saisir un operateurerateur entre <= = et >= \n")

    while True:                                                                                                                                
        variable4=float(input(f"la constante de la contrainte {j+1} : \n"))               
        if variable4>=0:
            b.append(variable4)
            break
        else:
            print("veuillez saisir une valeur positive \n")                                        


#Affichage

print(f"\n PL:")

print(f"\n {type}    z= ",end="")
for i in range(0,n):
    if c[i]!=0:
        print(f"{c[i]}*x{i+1}",end="")
        if i<n-1:
            print(" + ",end="")

print("\n \n ")
for j in range(0,m):
    for i in range(0,n):
        if a[j][i] != 0:
            print(f" {a[j][i]}*x{i+1} ",end="")
            if i<n-1 and a[j][i+1]!=0:
                print("+ ",end="")

    print(f" {operateur[j]} {b[j]} ")

def simplexe():
    
    print(f"\n Votre PL canonique:")
    print(f"\n {type}    z= ",end="")
    for i in range(0,n):
        if c[i]!=0:
            print(f"{c[i]}*x{i+1}",end="")
            if i<n-1:
                print(" + ",end="")

    print("\n Les contraintes : ")
    for j in range(0,m):
        for i in range(0,n):
            if a[j][i] != 0:
                print(f" {a[j][i]}*x{i+1} ",end="")
                if i<n-1 and a[j][i+1]!=0:
                    print("+ ",end="")
 
        print(f"+ e{j+1} = {b[j]} ")                        

    #1ere solution de base

    sb=[0]*n+b                                        #sb contient la solution de base 

    tab=[]                                      #tab est le tableau simplexe
    l1=["Base"]+[f"x{i+1}" for i in range(n)]+[f"e{j+1}" for j in range(m)]+["sm"]             
    tab.append(l1)

    for j in range(m):                                                                             
        l=[f"e{j+1}"]+a[j]+[1 if j==i else 0 for i in range(m)]+[b[j]]
        tab.append(l)

    lz=["-z"]+c+[0]*m+[0]                                                                      
    tab.append(lz)

    k=0                                                                                             
    print(f"\n k={k}")

    print(f"\n solution de base : X({k})=(",end="")
    for i in range(n+m):
        print(f"{sb[i]}",end="")
        if i<n+m-1:
            print(",",end="")
        else:
            print(")")

    print("\n Tableau initial : ")
    for l in tab:
            print(" / ".join(str(e) for e in l )) 
    
    k=1
    while True:
        if type=="min":
            mv=0                                           #mv contient la valeur minimale des Cj                                             
            for j in range(1,m+n+1):                           
                if tab[m+1][j]<mv:             
                    mv=tab[m+1][j]
                    cp=j                                  #cp est l'indice de la colonne de pivot

            if mv==0:                                          
                print("\n critere d'optimalite atteint")
                break                                           
            
            Test=[]                                              #Test conteint les valeurs de la colonne Test
            ls=[]                                            
            for i in range(1,m+1):                              
                variable5=tab[i][n+m+1]/tab[i][cp]
                if variable5>0:                                       
                    Test.append(variable5)
                    ls.append(i)

            if not Test:                                         
                print("\n Pas de solutions")
                break

            mval=min(Test)                                    #mval contient la valeur la plus petite de Test
            lp=ls[Test.index(mval)]                       #lp contient l'indice de la ligne pivot

            pivot=tab[lp][cp]                        #pivot contient le pivot de l'iteration k

            #Affichage du pivot
            print(f"\n VBnew ={tab[0][cp]}")
            print(f"\n VHBnew = {tab[lp][0]}")
            print(f"\n pivot= {tab[lp][cp]}")

            tab[lp][0]=tab[0][cp]        
            for j in range(1,m+n+2):
                tab[lp][j]/=pivot

            for i in range(1,m+2):                             
                if i!=lp:
                    var=tab[i][cp]              #var contient le pivot de la li
                    for j in range(1,m+n+2):
                        tab[i][j]-=var*tab[lp][j]

            sb=[0]*(n+m)

            for i in range(1,m+1):                              
                if tab[i][0].startswith("x"):
                    ind=int(tab[i][0][1:])-1        #la variable ind extrait l'indice de la VB
                    sb[ind]=tab[i][n+m+1]
                elif tab[i][0].startswith("e"):     
                    ind=n+int(tab[i][0][1:])-1
                    sb[ind]=tab[i][n+m+1]

            print(f"\n k={k}")
            print(f"\n X({k})=(",end="")
            
            for i in range(n+m):
                print(f"{sb[i]}",end="")
                if i<n+m-1:
                    print(",",end="")
                else:
                    print(")")

            print(f"\n Tableau a l'iteration {k} : ")
            for l in tab:
                print(" / ".join(str(elem) for elem in l ))

            k+=1

        elif type=="max":
            mv=0                                                           # mv contient la valeur maximale des Cj
            cp=-1                                                               #cp represente l'indice de la colonne de pivot
            for j in range(1,m+n+1):                                            
                if tab[m+1][j]>mv:                             
                    mv=tab[m+1][j]
                    cp=j

            if mv==0:                                                         
                print("\n critere d'optimalite atteint")
                break
                                   
            Test=[]                                              #test contient les valeur de la colonne Test
            ls=[]                                            
            for i in range(1,m+1):                              
                variable5=tab[i][n+m+1]/tab[i][cp]
                if variable5>0:
                    Test.append(variable5)
                    ls.append(i)

            if not Test:                                            
                print("\n pas de solutions")
                break

            mval=min(Test)                                       #la variable mval contient la valeur la plus petite de sm/cp
            lp=ls[Test.index(mval)]                          #la variable lp contient l'indice de la ligne du pivot

            print(f"\n VBnew ={tab[0][cp]}")
            print(f"\n VHBnew = {tab[lp][0]}")
            print(f"\n pivot= {tab[lp][cp]}")

            pivot=[lp][cp]

            tab[lp][0]=tab[0][cp]                
            for j in range(1,m+n+2):
                tab[lp][j]/=pivot

            for i in range(1,m+2):                                       
                if i!=lp:
                    var=tab[i][cp]                       #var contient le pivot de li
                    for j in range(1,m+n+2):
                        tab[i][j]-=var*tab[lp][j]

            sb=[0]*(n+m)

            for i in range(1,m+1):                                          
                if tab[i][0].startswith("x"):
                    ind=int(tab[i][0][1:])-1                    #la variable ind indique l'indice de la VB
                    sb[ind]=tab[i][n+m+1]
                elif tab[i][0].startswith("e"):
                    ind=n+int(tab[i][0][1:])-1
                    sb[ind]=tab[i][n+m+1]

            print(f"\n k={k}")

            print(f"\n  X({k})=(",end="")
            
            for i in range(n+m):
                print(f"{sb[i]}",end="")
                if i<n+m-1:
                    print(",",end="")
                else:
                    print(")")

            print(f"\n Tableau a l'iteration {k} : ")
            for l in tab:
                print(" / ".join(str(e) for e in l ))

            k+=1

    print("\n X*=(",end="")
    for i in range(n+m):
                print(f"{sb[i]}",end="")
                if i<n+m-1:
                    print(",",end="")
                else:
                    print(")")

    print(f"\n l'optimum z* = {-1*tab[m+1][n+m+1]}")

def BIGM():
 
    e=[]                                                            #liste des variables d'ecart et d'excedent
    t=[]                                                            #liste des variables artificielles
    indice_t=[]   
    indice_e=[]                                                    #tableau qui va contenire les variable d'ecart ou d'excedent et/ou artificielle de chaque contrainte (ligne du tableau = contrainte)
    
    for j in range(m):
        ligne=[]
        if operateur[j]=="<=":
            e.append(f"e{j+1}")
            ligne.append(f"+e{j+1}")
            indice_e.append(j)
        elif operateur[j]==">=":
            e.append(f"e{j+1}")
            indice_e.append(j)
            t.append(f"t{j+1}")
            indice_t.append(j)
            ligne.append(f"-e{j+1}")
            ligne.append(f"+t{j+1}")
        elif operateur[j]=="=":
            t.append(f"t{j+1}")
            ligne.append(f"+t{j+1}")
            indice_t.append(j)

    contraintes=[]
    for j in range(m):
        lignec=[]
        for i in range(n):
            if a[j][i]!=0:
                lignec.append(f"{a[j][i]}*x{i+1}")
                if i<n-1 and a[j][i+1]!=0:
                    lignec.append("+")
        if operateur[j]=="<=":
            lignec.append(f"+e{j+1}")
        elif operateur[j]==">=":
            lignec.append(f"-e{j+1}")
            lignec.append(f"+t{j+1}")
        elif operateur[j]=="=":
            lignec.append(f"+t{j+1}")
        lignec.append(f" = {b[j]}")
        contraintes.append(" ".join(lignec))

    fct_obj=[f"{c[i]}*x{i+1} + " if i<n-1 else f"{c[i]}*x{i+1}"  for i in range(n) if c[i]!=0]+[f" + M*{t[i]} " if type =="min" else f" -  M*{t[i]} " for i in range(len(t))]
    fct_obj=" ".join(fct_obj)

    substitution={}

    for j in range(m):
        if operateur[j]==">=" or operateur[j]=="=":
            equation=contraintes[j].replace(" ","")                                     
            left,right=equation.split("=")
            var=f"t{j+1}"
            if var in left:
                t_expr=f"{right}-({left.replace(var,'0')})"
                substitution[var]=t_expr


    print(f"\n programme lineaire standard mixte:")
    print(f"\n La fonction objectif : {type}    z= {fct_obj}")

    print("\n Les contraintes : ")
    for j in range(0,m):
        print(contraintes[j])


    for val6, expressioon in substitution.items():
        fct_obj=fct_obj.replace(val6,f"({expressioon})")

    print(f"\n programme lineaire standard mixte: apres substitution")
    print(f"\n La fonction objectif : {type}    z= {fct_obj}")

    print("\n Les contraintes : ")
    for j in range(0,m):
        print(contraintes[j])


    Sol_base=[0]*n                              #Tableau qui va contenir notre solution de base 
    for j in range(m):
        if operateur[j]=="<=" :
            Sol_base.append(b[j])
        elif operateur[j]==">=" :
            Sol_base.append(0)

    for j in range(m):
        if operateur[j]=="=" or operateur[j]==">=":
            Sol_base.append(b[j])                        

    tab=[]                                      #Tableau simplexe
    ligne1=["Base"]+[f"x{i+1}" for i in range(n)]+[e[j] for j in range(len(e))]+[t[j] for j in range(len(t))]+["SM"]              
    tab.append(ligne1)

    for j in range(m):
        if operateur[j]=="<=":                                                                             
            ligne=[f"e{j+1}"]+a[j]+[1 if j==i else 0 for i in indice_e]+[0]*len(t)+[b[j]]
            tab.append(ligne)
        elif operateur[j]==">=":
            ligne=[f"t{j+1}"]+a[j]+[-1 if j==i else 0 for i in indice_e]+[1 if j==i else 0 for i in indice_t]+[b[j]]
            tab.append(ligne)
        else:                                                                         
            ligne=[f"t{j+1}"]+a[j]+[0]*len(e)+[1 if j==i else 0 for i in indice_t]+[b[j]]
            tab.append(ligne)

    M=1e6
    lignez=["-z"]
    if type=="min":
        for i in range(n):
            coeff=c[i]
            for j in range(m):
                if operateur[j]=="=" or operateur[j]==">=":
                    coeff-= a[j][i]*M
            lignez.append(coeff)
        
        for j in range(m):
            if operateur[j]=="<=":
                lignez.append(0)
            elif operateur[j]==">=":
                lignez.append(M)

        for j in range(len(t)):
            lignez.append(0)
    
        somme=0
        for j in range(m):
            if operateur[j]==">=" or operateur[j] =="=":
                somme+=b[j]  
            
        lignez.append(-somme*M)                                                               
        tab.append(lignez)
    elif type=="max":
        for i in range(n):
            coeff=c[i]
            for j in range(m):
                if operateur[j]=="=" or operateur[j]==">=":
                    coeff+= a[j][i]*M
            lignez.append(coeff)
        
        for j in range(m):
            if operateur[j]=="<=":
                lignez.append(0)
            elif operateur[j]==">=":
                lignez.append(-M)

        for j in range(len(t)):
            lignez.append(0)
    
        somme=0
        for j in range(m):
            if operateur[j]==">=" or operateur[j] =="=":
                somme+=b[j]   

        lignez.append(somme*M)                                                               
        tab.append(lignez)

    k=0                                                                                             #la variable k represente l'iteration
    print(f"\n k={k}")

    print(f"\n Votre solution de base : X({k})=(",end="")
    for i in range(n+len(e)+len(t)):
        print(f"{Sol_base[i]}",end="")
        if i<n+len(e)+len(t)-1:
            print(",",end="")
        else:
            print(")")

    print("\n  Tableau initial : ")
    for ligne in tab:
            print(" | ".join(str(elem) for elem in ligne )) 

    k=1
    nbt_t=len(t)
    while True:
        if type=="min":
            
            min_val=0                                           #la variable min_val contient la valeur minimale des Cj
            CP=-1                                               #la variable CP represente l'indice de la colonne de pivot
            degenere=0
            for i in range(m):
                if b[i]==0:
                    degenere=1
            if degenere==0:                                                           #la variable CP represente l'indice de la colonne de pivot
                for j in range(1,len(e)+len(t)+n+1):                                            
                    if tab[m+1][j]<min_val:                            
                        min_val=tab[m+1][j]
                        CP=j
            else:
                for j in range(1,len(e)+len(t)+n+1):
                    if tab[m+1][j]<min_val:                            
                        min_val=tab[m+1][j]
                        CP=j
                        break
            if CP==-1:                                         
                print("\n critere d'optimalite atteint")
                break                                        

            print(f"\n VBnew ={tab[0][CP]}")
            
            Test=[]                                              #Tableau qui va contenir les valeur de la colonne Test=SM/CP
            Lignes=[]                                            #Tableau qui va contenir les indice des VB candidate a sortir
            for i in range(1,m+1):                              
                if tab[i][CP]!=0:
                    if tab[i][n+len(t)+len(e)+1]!=0:
                        val5=tab[i][n+len(t)+len(e)+1]/tab[i][CP]
                    elif tab[i][CP]>0:
                        val5=0
                if val5>=0:
                    Test.append(val5)
                    Lignes.append(i)

            if not Test:                                         
                print("\n Le probleme est non borne")
                break

            minimum=min(Test)                                    #la variable minimum contient la valeur la plus petite du tableau Test
            LP=Lignes[Test.index(minimum)]                       #la variable LP contient l'indice de la ligne du pivot

            print(f"\n VHBnew = {tab[LP][0]}")
            
            VHB=tab[LP][0]
            indice_cvhb=-1

            for j in range(1,len(tab[0])):
                if tab[0][j]== VHB:
                    indice_cvhb=j
                    break

            if indice_cvhb!=-1 and VHB.startswith("t"):
                for ligne6 in tab:
                    del ligne6[indice_cvhb] 
                t.remove(VHB)

            #Recherche du pivot
            pivot=tab[LP][CP]                        #La variable pivot contient le pivot de l'iteration k

            print(f"\n pivot= {pivot}")

            tab[LP][0]=tab[0][CP]        
            for j in range(1,len(e)+len(t)+n+2):
                tab[LP][j]/=pivot

            for i in range(1,m+2):                             
                if i!=LP:
                    facteur=tab[i][CP]              #facteur contient le pivot de la ligne i
                    for j in range(1,len(e)+len(t)+n+2):
                        tab[i][j]-=facteur*tab[LP][j]
        
            Sol_base=[0]*(n+len(e)+nbt_t)
            try:
                for i in range(1,m+1):
                    idx=tab[i][0]                              
                    if idx.startswith("x"):
                        Sol_base[int(idx[1:])-1]=tab[i][-1]        #la variable idx extrait l'indice de la VB
                    elif idx.startswith("e"):    
                        Sol_base[n+int(idx[1:])-1]=tab[i][-1]
                    elif idx.startswith("t"):
                        Sol_base[n+len(e)+int(idx[1:])-1]=tab[i][-1]       
            except IndexError as e :
                print(f"\n erreur indexation : {e}")
                return
            
            print(f"\n k={k}")

            print(f"\n  X({k})=(",end="")
            
            for i in range(n+len(e)+nbt_t):
                print(f"{Sol_base[i]}",end="")
                if i<n+len(e)+nbt_t-1:
                    print(",",end="")
                else:
                    print(")")

            print(f"\n Votre Tableau a l'iteration {k} : ")
            for ligne in tab:
                print(" | ".join(str(elem) for elem in ligne ))


            k+=1

        #Cas d'une maximisation
        elif type=="max":
            
            max_val=0                                                           #la variable max_val contient la valeur maximale des Cj
            CP=-1    
            degenere=0
            for i in range(m):
                if b[i]==0:
                    degenere=1
            if degenere==0:                                                           #la variable CP represente l'indice de la colonne de pivot
                for j in range(1,len(e)+len(t)+n+1):                                          
                    if tab[m+1][j]>max_val:                             
                        max_val=tab[m+1][j]
                        CP=j
            else:
                for j in range(1,len(e)+len(t)+n+1):
                    if tab[m+1][j]>max_val:                            
                        max_val=tab[m+1][j]
                        CP=j
                        break


            if CP==-1:                                                          
                print("\n critere d'optimalite atteint")
                break

            print(f"\n VBnew ={tab[0][CP]}")

                         
            Test=[]                                              #Tableau qui va contenir les valeur de la colonne Test=SM/CP
            Lignes=[]                                            #Tableau qui va contenir les indice des VB candidate a sortir
            for i in range(1,m+1):                              
                if tab[i][CP]!=0:
                    if tab[i][n+len(t)+len(e)+1]!=0:
                        val5=tab[i][n+len(t)+len(e)+1]/tab[i][CP]
                    elif tab[i][CP]>0:
                        val5=0
                if val5>=0:
                    Test.append(val5)
                    Lignes.append(i)

            if not Test:                                             
                print("\n Le probleme est non borne")
                break

            minimum=min(Test)                                       #la variable minimum contient la valeur la plus petite du tableau Test
            LP=Lignes[Test.index(minimum)]                          #la variable LP contient l'indice de la ligne du pivot

            print(f"\n VHBnew = {tab[LP][0]}")

            VHB=tab[LP][0]
            indice_cvhb=-1

            for j in range(1,len(tab[0])):
                if tab[0][j]== VHB:
                    indice_cvhb=j
                    break

            if indice_cvhb!=-1 and VHB.startswith("t"):
                for ligne6 in tab:
                    del ligne6[indice_cvhb] 

                t.remove(VHB)

            pivot=tab[LP][CP]                            #La variable pivot contient le pivot de l'iteration k

            print(f"\n pivot= {pivot}")

            tab[LP][0]=tab[0][CP]                
            for j in range(1,len(e)+len(t)+n+2):
                tab[LP][j]/=pivot

            for i in range(1,m+2):                                      
                if i!=LP:
                    facteur=tab[i][CP]                       #facteur contient le pivot de la ligne i
                    for j in range(1,len(t)+len(e)+n+2):
                        tab[i][j]-=facteur*tab[LP][j]
 
            Sol_base=[0]*(n+len(e)+nbt_t)
            try:
                for i in range(1,m+1):
                    idx=tab[i][0]                              
                    if idx.startswith("x"):
                        idx_val=int(idx[1:])-1        #la variable idx extrait l'indice de la VB
                    elif idx.startswith("e"):     
                        idx_val=n+int(idx[1:])-1
                    elif idx.startswith("t"):
                        idx_val=n+len(e)+int(idx[1:])-1
                    else:
                        idx_val=None
                    if idx_val is not None and 0<= idx_val < len(Sol_base):
                        Sol_base[idx_val]=tab[i][-1]

            except IndexError as e :
                print(f"\n erreur indexation : {e}")
                return
  
            print(f"\n k={k}")

            print(f"\n  X({k})=(",end="")
            
            for i in range(n+len(e)+nbt_t):
                print(f"{Sol_base[i]}",end="")
                if i<n+len(e)+nbt_t-1:
                    print(",",end="")
                else:
                    print(")")

            print(f"\n  Tableau a l'iteration {k} : ")
            for ligne in tab:
                print(" | ".join(str(elem) for elem in ligne ))

            k+=1


    if len(t)>0:
        print(" pas de solution")
        return
    
    print("\n X*=(",end="")
    for i in range(n+len(e)+nbt_t):
        print(f"{Sol_base[i]}",end="")
        if i<n+m-1:
            print(",",end="")
        else:
            print(")")

    #Affichage de l'optimum
    print(f"\n avec l'optimum z* = {-1*tab[m+1][n+len(e)+1]}")

s=0
for j in range(m):
    if operateur[j]=="<=":
        s=s+1

if s==m:
    simplexe()

else:
    BIGM()
