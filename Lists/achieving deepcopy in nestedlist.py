import copy
l1=[10,20,["python","java"],30]
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l1[2][1]="sql"
print(l1)
print(l2)
