def firstMissingInt(arr):
    arr.sort()
    ele = 1
    
    for i in range(0, len(arr)):
        if(arr[i] < ele):
            continue
        elif(arr[i] == ele):
            ele+=1
        else:
            return ele
    return ele
        
inputList = [int(item) for item in input("Enter the list items: ").split()]

print(firstMissingInt(inputList))
