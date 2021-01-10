'''3. Given an array arr[] of positive integers of size N. Reverse every
sub-array group of size K.'''


def reverse_array(array, N, k): 
    i = 0
      
    while(i<N): 
      
        left = i  
  
        # To handle case when k is not 
        # multiple of n 
        right = min(i + k - 1, N - 1)  
  
        # Reverse the sub-array [left, right] 
        while (left < right): 
              
            array[left], array[right] = array[right], array[left] 
            left+= 1; 
            right-=1
        i+= k 
      
 
array = [5,6,8,9]  #Assign the argument values
k = 3
N = len(array)     #to get length of the array size
reverse_array(array, N, k)   # call the def fuction and pass the arguments
  
for i in range(0, N):     # iterate the array 
        
        print(array[i], end =" ") 
          
'''OUTPUT LIKE
8 6 5 9 
>>>
'''

