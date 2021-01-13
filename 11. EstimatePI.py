import random 

interval= 1000

circle_pts= 0
square_pts= 0

for i in range(interval**2): 
	ran_x= random.uniform(-1, 1) 
	ran_y= random.uniform(-1, 1) 

	origin_dist= ran_x**2 + ran_y**2

	if origin_dist<= 1: 
		circle_pts+= 1

	square_pts+= 1

	pi = 4* circle_pts/ square_pts 

print("Estimation of Pi is: ", pi)
