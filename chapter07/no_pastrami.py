import time
#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders = ['pastrami','ham and cheese','grilled cheese','pastrami','italian sub','pastrami','philly cheese steak']
finished_sandwiches = []
print("Unfortunately, we're all out of pastrami today.""\n""Now removing all pastrami-related sandwhiches from today's orders""\n")
#Remove all instances of "pastrami" from the orders.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#Make the orders
while sandwich_orders:
    completed_sandwhich = sandwich_orders.pop(0)
    print(f"Sandwitch order, '{completed_sandwhich.title()}' is ready for pickup:")
    finished_sandwiches.append(completed_sandwhich)
    time.sleep(1)

print("\nTotal sandwiches completed are:")
for sandwich in finished_sandwiches:
    print(sandwich.title())