"""
Q1. Sorting algorithms and their time complexities:
ALGORITHM   BEST CASE   AVERAGE CASE    WORST CASE

Selection   O(n^2)        O(N^2)          O(N^2)
Bubble      O(N)          O(N^2)          O(N^2)
Insertion   O(N)          O(N^2)          O(N^2)
Heap        O(NLOGN)      O(NLOGN)        O(NLOGN)
Quick       O(NLOGN)      O(NLOGN)        O(N^2)
"""

# Q2.
for i in range(len(a)):
    mdx=i
    for j in range(i+1,len(a)):
        if a[mdx] > a[j]:
            mdx = j
    a[mdx],a[i] = a[i],a[mdx]
for i in range(len(a)):
    print(a[i])
    
# Q3.
a = [10,13,45,34,6]
# pops last 3 elements
for i in range(3):
    print(a.pop())
print(a)

# Q4.
q = [10,13,45,34,6]
# removes first 3 elements
for i in range(3):
    print(q.pop(0))
print(q)
    
