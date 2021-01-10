'''Given an array having both positive and negative integers. The task is to
compute the length of the largest subarray with sum 0'''
  
 
def maxLen(array): 
      
    # initialize result 
    max_len = 0
  
    # pick a starting point 
    for i in range(len(array)): 
          
        # initialize sum for every starting point 
        current_sum = 0
          
        # try all subarrays starting with 'i' 
        for j in range(i, len(array)): 
          
            current_sum += array[j] 
  
            # if curr_sum becomes 0, then update max_len 
            if current_sum == 0: 
                max_len = max(max_len, j-i + 1) 
  
    return max_len 
  
  
# test array 
array = [15,-2,2,-8,1,7,10,23]  #assign the array values
result= maxLen(array)           #call the def function and pass the argument value stored in a variable name
print ("Length of the largest subarray is % d" %result) 


'''OUTPUT LIKE
Length of the largest subarray is  5
'''
