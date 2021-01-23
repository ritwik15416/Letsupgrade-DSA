#Q1.
lst = [12, 3, 55, 6, 144]
ans = []
for i in lst:
    if i%2==0:
        ans.append(i)
print(ans)


#Q2.
for i in range(1,6):
    print(' '*(5-i),str(i)*i)
