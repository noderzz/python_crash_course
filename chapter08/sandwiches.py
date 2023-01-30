#Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
def sandwich_items(*items):
    print(f"\nNow creating a sandwhich with: ")
    for item in items:
        print(item.title())

sandwich_items('peanut butter','jelly','bananas')
sandwich_items('ham','cheese','bacon')
sandwich_items('chicken','avocado','bacon')

