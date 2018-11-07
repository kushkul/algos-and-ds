#Problem Statement:

'''The problem is given an array A having N integers, for each i between 
1 and N (including both), find x+y where x is the largest number less than i 
such that A[x] > A[i] and y is the smallest number greater than i such that 
A[y] > A[i]. If there is no x < i such that A[x] > A[i] then take x = -1. 
Similarly, if there is no y > i such that  A[y] > A[i], then take y = -1
'''

#My Solution:
stack_temp = []
left = []
total = int(input())
numbers = [int(i) for i in input().split(' ')]

for i in range(0,total):
    #print('i is ',i)
    while (len(stack_temp) >0):
        k = stack_temp[-1]
        #print('k is: ',k)
        #print('inside if',numbers[i],'<',numbers[k])
        if numbers[i]<numbers[k]:
            left.append(k+1)
            #print('left is: ', left)
            #print('here?')
            #stack_temp.push(k)
            stack_temp.append(i)
            break
        else:
            stack_temp.pop()
    if len(stack_temp) == 0:
        left.append(-1)
        #print('left is: ', left)
        stack_temp.append(i)

right = []
stack_temp = []

for i in range(total-1,-1, -1):
    while (len(stack_temp) >0):
        k = stack_temp[-1]
        if numbers[i]<numbers[k]:
            right.append(k+1)
            #stack_temp.push(k)
            stack_temp.append(i)
            break
        else:
            stack_temp.pop()
    if len(stack_temp) == 0:
        right.append(-1)
        stack_temp.append(i)

final = []
for i in range(len(left)):
    final.append(left[i] + right[len(right)-1 - i])
print(*final)
