# Python 3 code to demonstrate the  
# working of MD5 (string - hexadecimal) 
  
import hashlib 
  
# initializing string 
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode() 
# then sending to md5() 
result = hashlib.md5(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 

#Output:
#The hexadecimal equivalent of hash is : f1e069787ece74531d112559945c6871
