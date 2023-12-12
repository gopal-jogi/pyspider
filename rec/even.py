def is_add_even(num):
 
    if num==7:
        return 0
    if num%2==0:
        return num+is_add_even(num+1)
    return is_add_even(num+1)
    

print(is_add_even(1))
# is_add_even(50)