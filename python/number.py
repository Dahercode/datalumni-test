# Your code goes here
tab=[]
for i in range(1000) :
    tab.append(i)

tab2=[]
for i in range(len(tab)):
    if sum([ int(c) for c in str(tab[i]) ]) <= 10:
        tab2.append(tab[i])

tab3=[]
for i in range(len(tab2)):
    a=str(tab2[i])
    if a[len(a)-2] == '4':
        tab3.append(tab2[i])

tab4=[]
for i in range(len(tab3)):
    if len(str(tab3[i]))>=2 :
        tab4.append(tab3[i])

tab5=[]
for i in range(len(tab4)):
    a=str(tab4[i])
    if a.find('7')==-1 and a.find('1')==-1:
        tab5.append(tab4[i])

tab6=[]
for i in range(len(tab5)):
    a=str(tab5[i])
    if ((int(a[0])+int(a[1]))%2) != 0:
        tab6.append(tab5[i])

tab7=[]
for i in range(len(tab6)):
    a=str(tab6[i])
    if str(len(a)) == a[len(a)-1]:
        tab7.append(tab6[i])

tab8=[]
for i in range(len(tab7)):
    if i%2!=0:
        tab8.append(tab7[i])

mystery_number=tab8[0]
print(f'Le nombre mystère est le : {mystery_number}')
