
num=1
print( 'prime' if num>1 and len([val for val in range(2,int(num**0.5)+1) if num%val==0])==0 else 'not prime')