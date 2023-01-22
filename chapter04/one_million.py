#Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
huge_list = [x for x in range(1,1_000_001)]
for i in huge_list:
    print(i)