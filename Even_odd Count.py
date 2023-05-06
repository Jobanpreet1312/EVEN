  # taking input from user 

numb1 = input("Enter a list of numbers , separated by spaces : ").split() 

#convert this list of strings to the integers 

numb1 = [ int(num) for num in numb1]

even_count = 0
odd_count = 0

for num in numb1 :
    if num % 2 == 0 :
        even_count += 1
    else :
        odd_count += 1

print("Count of even numbers: ", even_count)  
print("Count of odd numbers: ", odd_count)          

  


