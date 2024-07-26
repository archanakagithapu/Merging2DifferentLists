# 2 different lists and merging them

List1=list(map(int,input().split()))
List2=list(map(int,input().split()))
#print(List1+List2,sep=',')
List3=sorted(List1+List2)
print(List3)

