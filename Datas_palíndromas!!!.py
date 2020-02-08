import numpy as np

Ai, Af = 1, 10000-1
A = np.linspace(Ai, Af, Af-Ai+1)

a, m, d = [], [], []
am, ad = [], [] # ad conterá todos os anos palindromos 
data, date = [], [] # data conterá todos os anos palindromos no formato  ab/ba/abba
                    # date conterá  todos os anos palindromos no formato ab/ab/baba

# criação da lista a com os anos
#-------------------------#
for i in A:
    a.append(str(int(i)))
    
for i in range(len(a)):
    if len(a[i])==1:
        a[i] = '000'+a[i]
    if len(a[i])==2:
        a[i] = '00'+a[i]
    if len(a[i])==3:
        a[i] = '0'+a[i]
#-------------------------#

#cria a lista m com os meses
        
#-------------------------#
for i in range(12):
    if i+1 < 10:
        m.append('0'+str(i+1))
    if i+1 >= 10:
        m.append(str(i+1))
#-------------------------#

#cria a lista d com os dias
        
#-------------------------# 
for i in range(31):
    if i+1 < 10:
        d.append('0'+str(i+1))
    if i+1 >= 10:
        d.append(str(i+1))
#-------------------------# 
        
#separa todos os anos que são palíndromos
#  ----> se conseguir fazer um algoritimo melhor por favor não deixe de me mandar 

#-------------------------# 
for i in a:
    for j in m:
        if i[0] == j[1]:
            if i[1] == j[0]:
                am.append(i)
for i in am:
    for j in d:
        if i[2] == j[1]:
            if i[3] == j[0]:
                ad.append(i)
#-------------------------# 
         
#separa as datas palíndromas especiais            
            
#-------------------------# 
for i in ad:
    if i[0]== i[3]:
        if i[1] == i[2]:
            data.append(i)
            
for i in ad:
    if i[0]== i[2]:
        if i[1] == i[3]:
            date.append(i)
#-------------------------# 
    
    
for i in ad:              #todos dia palíndromos
#for i in data:            #dias palidromos do tipo ab/ba/abba
#for i in data:            #dias palidromos do tipo ab/ab/baba
    print(i[3] + i[2] + '/' + i[1] + i[0] + '/' + i)




