# def calc_sum(a,b):
#     s=a+b
#     return s



# num1=int(input("Enter first number."))
# num2=int(input("Enter second number."))


# sum= calc_sum(num1,num2)
# print(sum)

# def calc_prod(a,b):
#     s=a*b
#     return s

# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))


# prod= calc_prod(num1,num2)
# print("product is:",prod)


def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
num=int(input("Enter the number:"))

fac=fact(num)
print("Factorial of ",num,"is :",fac)