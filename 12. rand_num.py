# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random 

a = int(input().strip())

 
def random_num(x): 
    
    temp_num = 0 
	
	count = 0 

	count += 1

	if (count == 1): 
		temp_num = x 
	else: 
		i = random.randrange(count); 

		if (i == count - 1): 
			temp_num = x 
	return temp_num 


stream = [1, 2, 3, 4]; 
n = len(stream); 

for i in range (n): 
	print(f"Random number from first {(i+1)} numbers is {random_num(stream[i])}") 
		); 
