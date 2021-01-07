def num_of_decodings(s, n):  
    count = 0
    if n == 0 or n == 1 :  
        return 1
    if s[n-1] > "0":  
        count = num_of_decodings(s,n-1)  
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7') ) :  
        count += num_of_decodings(s, n - 2)  
    return count  
          
digits = input('Enter the digits sequence:')
print("Count is ",num_of_decodings(digits, len(digits)))
