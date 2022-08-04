def gcd(p,q):
    if (q==0):
        return p
    return gcd(q,p%q)


n1 = int(input("First Number: "))
n2 = int(input("Second Number: "))

print("Gcd of",n1,"and",n2,"is",gcd(n1,n2))
