'''
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
'''
def make_shirt(size, text):
    print(f"Shirt size selected is {size}.")
    print(f"The text will read:\n{text}")

make_shirt('small',"It's taco time!")
make_shirt(text="It's taco time!", size='small')