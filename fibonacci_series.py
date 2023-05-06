n = int(input("Enter limit")) #in this question our limit is 50
a = 0
b = 1

c = 0 
while (c <= n):
    print(c,end=" ")
    a = b
    b = c
    c = a + b
