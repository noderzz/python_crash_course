#Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
massive_list = [x for x in range(1,1_000_001)]

#Print the largest number:
print(max(massive_list))

#Print the smallest number:
print(min(massive_list))

#Adding a million numbers:
print(sum(massive_list))