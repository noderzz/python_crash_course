favorite_languages = {
    'jen':'java',
    'sarah': 'c',
    'edward':'ruby',
    'phil':'python',
    'george':'python'
}

new_guy = set(favorite_languages.values())
print(new_guy)

print("\n")
for language in set(favorite_languages.values()):
    print(language)