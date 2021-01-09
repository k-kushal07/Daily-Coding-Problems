def maxSum(arr): 
    incl = 0
    excl = 0
     
    for i in arr:
        new_excl = excl if excl>incl else incl 
         
        incl = excl + i 
        excl = new_excl 
      
    if excl>incl:
        return excl
    else:
        return incl
        
inputList = [int(item) for item in input("Enter the list items: ").split()]

print(maxSum(inputList))
