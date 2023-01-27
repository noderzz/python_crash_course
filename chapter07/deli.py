import time

#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
sandwich_orders = ['pastrami','ham and cheese','grilled cheese','italian sub','philly cheese steak']
finished_sandwiches = []

print("\n")
while sandwich_orders:
    completed_sandwhich = sandwich_orders.pop(0)
    print(f"Sandwitch order, '{completed_sandwhich.title()}' is ready for pickup:")
    finished_sandwiches.append(completed_sandwhich)
    time.sleep(1)

print("\nTotal sandwiches completed are:")
for sandwich in finished_sandwiches:
    print(sandwich.title())