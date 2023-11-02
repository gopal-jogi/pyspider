# def isB2C(num,Sum=0,p=1):
#     while(num!=0):
#         rem=num%2
#         Sum+=rem*p
#         num//=2
#         p*=10
#     return Sum
# num=17
# print(isB2C(num))
decimal_to_binary = lambda decimal_num: decimal_to_binary(decimal_num // 2) + str(decimal_num % 2) if decimal_num > 1 else str(decimal_num)

# Example usage
decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_number}")