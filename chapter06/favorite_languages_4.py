#This is a dicitonary
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil':'python',
}

#This is a list
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("\nErin, please take our poll!")
