n = int(input("How many terms? "))

# first two terms
a, b = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
# if there is only one term, return a
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(a)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(a)
       nth = a + b
       # update values
       a = b
       b = nth
       count += 1
