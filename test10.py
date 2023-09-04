nums=[4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
nums.sort() #sort list min to max 
nums_dict ={} #empty dictionary 

for num in nums:
    if num in nums_dict:
        nums_dict[num]+=[num] #add same values in one array 
    else:
        nums_dict[num]=[num]

print(nums_dict)

'''''
output is :
    {2: [2, 2], 4: [4, 4, 4], 5: [5], 6: [6, 6], 8: [8, 8]}

'''''    
