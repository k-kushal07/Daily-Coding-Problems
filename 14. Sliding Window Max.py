def max_of_sub(arr, n, k):
	max = 0

	for i in range(n - k + 1):
		max = arr[i]
		
		for j in range(1, k):
			if(arr[i + j] > max):
				max = arr[i + j]
		
		print(str(max), end = " ")

arr = [int(item) for item in input("Enter the array items: ").split()]
n = len(arr)
k = int(input('Enter the size of sub-array: '))
max_of_sub(arr, n, k)
