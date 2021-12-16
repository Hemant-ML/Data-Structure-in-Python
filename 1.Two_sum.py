#Naive Approach:
#Time Complexity: O(n^2)
#Space Complexity: O(1)
lst = list(map(int,input().split()))
target = int(input())
def twoSum(lst,target):
    for i in range(len(lst)-1):
        firstnum=lst[i]
        for j in range(i+1,len(lst)):
            secondNum=lst[j]
            if firstnum+secondNum==target:
                return[firstnum,secondNum]
    return[]
print(twoSum(lst,target))
            
#Optimized Approach:
# Time Complexity: O(n)
# Space Complexity: O(n)

def opt_twosum(lst,target):
    nums={}
    for num in lst:
        potentialmatch = target - num
        if potentialmatch in nums:
            return [potentialmatch,num]
        else:
            nums[num]=True
    return []


#using kadane algorithm
#time complexity 0(nlogn)
#space complexity O(1)
def opt_twosum(lst,target):
    lst.sort()
    left=0
    right=len(lst)-1
    while left<right:
        currentSum= lst[left]+lst[right]
        if currentSum==target:
            return[lst[left],lst[right]]
        elif currentSum < target:
            left+=1
        elif currentSum>target:
            target-=1
    return[]
print(opt_twosum(lst,target))





    

