print("\t\tStudent Performance SC025 2023/2024")
print("\t\t***************************************")
studnum=float (input("\t\tEnter Number of Student : "))

marklist=[]
i=0 
while i<studnum:
    mark=int(input('\t\tEnter Mark :'))
    if (mark>100) or (mark<0):
        print("\t\t\tInvalid Mark")
    else:
        marklist.insert(i,mark)
        i+=1



#mark analysis
sum=0.00
x=0
for x in marklist: #x repersent s teh value of the list accodrig to their index then +1
    sum+=x
mean=sum/studnum
print("\n\t\tstudent Performance Analysis")
print("\t\t***************************************")
print("\t\tSummation of all marks is ",sum)
print("\t\tMean of all marks is ",mean)

acount=0.00
bcount=0.00
ccount=0.00
dcount=0.00
ecount=0.00
fcount=0.00



for x in marklist:
    if x>=90:
        acount+=1.00
    elif x>=80:
        bcount+=1.00
    elif x>=70:
        ccount+=1.00
    elif x>=60:
        dcount+=1.00
    elif x>=50:
        ecount+=1.00
    else:
        fcount+=1.00

aper=(acount/studnum)*100
bper=(bcount/studnum)*100
cper=(ccount/studnum)*100
dper=(dcount/studnum)*100
eper=(ecount/studnum)*100
fper=(fcount/studnum)*100


totalper=aper+bper+cper+dper+eper+fper



print('\t\t---------------------------------------------------')
print('\t\tGrade\tNumber of Students\tPercentage')
print('\t\t---------------------------------------------------')
print("\t\tA\t  ",acount,"\t\t\t  ",aper,"%")
print("\t\tB\t  ",bcount,"\t\t\t  ",bper,"%")
print("\t\tC\t  ",ccount,"\t\t\t  ",cper,"%")
print("\t\tD\t  ",dcount,"\t\t\t  ",dper,"%")
print("\t\tE\t  ",ecount,"\t\t\t  ",eper,"%")
print("\t\tF\t  ",fcount,"\t\t\t  ",fper,"%")
print('\t\t---------------------------------------------------')
print('\t\tTotal\t  ',studnum,'\t\t\t  ',totalper,'%')


highest=-999
lowest=999
for x in marklist:
    if x>highest:
        highest=x
        highloc=marklist.index(x)
    if x<lowest:
        lowest=x
        lowloc=marklist.index(x)




print("\t\tHighest & Lowest")
print('\t\t*******************')
print('\t\tThe Highest mark is : ',highest,'.(Index Location :',highloc,')')
print('\t\tThe Highest mark is : ',lowest,'.(Index Location :',lowloc,')')

