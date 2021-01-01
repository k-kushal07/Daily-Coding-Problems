def sumOfPairs(arr, value):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (i!=j and (arr[i]+arr[j]) == value):
                return True

inputList = [int(item) for item in input("Enter the list items: ").split()]
key = int(input("Enter the Target value: "))

print(sumOfPairs(inputList, key))
