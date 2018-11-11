#Problem Statement:

'''There are N frustrated coders standing in a circle with a gun in their hands. 
Each coder has a skill value S[i] and he can only kill those coders that have strictly less skill than him. 
All the guns have only 1 bullet. This roulette can take place in any random order.You can see all possible outcomes of the scenario. 
Find the outcome where the total sum of the remaining coder's skill is minimum. Print this sum.
'''

#My Solution:

total = int(input())

elements = [int(i) for i in input().split(' ')]
elements.sort()
final_sum = 0

i = total-1
j = i-1
final_sum = int(elements[i])
while i>0:
    while j>=0:
        if (int(elements[i]) > int(elements[j])):
            i -= 1
            j -= 1
            continue;
        else:
            final_sum += int(elements[j])
            j -= 1
            continue;
    i -= 1

print(final_sum)