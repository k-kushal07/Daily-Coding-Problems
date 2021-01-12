def fibo(n): 
    if n <= 1: 
        return n 
    return fibo(n-1) + fibo(n-2) 
  
def ways(s): 
    return fibo(s + 1)
  
total_stairs = int(input('Enter the total number of stairs: '))
print(f"The person can reach the top in {ways(total_stairs)} number of ways")
