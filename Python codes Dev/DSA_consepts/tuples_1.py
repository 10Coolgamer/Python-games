Details=('Dev',10)
address=('5','Shrewsbury','Massachusetts','123456')
for x in address:
    print(x,end='')
    
houseno , town , state , pin=address
print()
print("hno",houseno)
print("Town",town)
print(state)
Dog='Deg',1,"15 years"
print(Dog)
coding="c","o","d","i","n","g",' w',"i", "z" 
print(coding[6:9])
print(coding[0:3])
print(coding[:])
print(coding[:])

competition_record=[]
for g in range(5):
    print(f"\n Enter details of the group {g+1} :")
    a=input("What is the size of the group?: ")
    b=input("What is the group name?: ")
    c=input("What type of medal did they win?: ")
    d=input("What type of contest did they win?: ")
    e=input("Where was the contest?: ")
    f=input("What is the date of the contest?: ")
    
    contest=(a,b,c,d,e,f)
    competition_record.append(contest)
    
for contest in(competition_record):
    print('\ncontest')
    print("Size of group",contest[0])
    print("Group names",contest[1])
    print("Medals won",contest[2])
    print("Contests won",contest[3])
    print("Contest places",contest[4])
    print("Dates",contest[5])