prompt = "Please enter the naem of a city you have visited:"
prompt += "\n(Enter 'quit' to end the program.)\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")