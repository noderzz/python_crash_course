#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
multiples = [x for x in range(1,31) if x % 3 == 0] #I used the remainder operator sometimes also known as the modulus operator
print(multiples)