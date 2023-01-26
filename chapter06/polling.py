'''
Use the code in favorite_languages.py.

Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
'''
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil':'python',
    'george':'python'
}
not_taken_poll = ["jane","jack","carter","edward","george"]
for name in not_taken_poll:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for taking the poll!")
    else:
        print(f"Dear {name.title()}, we invite you to take our poll!")

