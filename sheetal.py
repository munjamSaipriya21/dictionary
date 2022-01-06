# def prime_number(n):
#     i=1
#     c=0
#     while i<=n:
#         if n%i==0 :
#             c=c+1
#         i+=1
#     if c==2:
#         print("prime number")
#     else:
#         print("not prime number")
# user=int(input("enter the number:"))
# prime_number(user)
def prime_number(n):
    i=1
    while i<=n:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c=c+1
            j+=1
        if c==2:
            print(i,"prime number")
        i+=1
user=int(input("enter the number:"))
prime_number(user)




