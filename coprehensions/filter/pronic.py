print(list(filter(lambda num:[n*(n+1) for n in range(int(num**0.5)+1) if n*(n+1)>=num]==[num], range(1,101))))
