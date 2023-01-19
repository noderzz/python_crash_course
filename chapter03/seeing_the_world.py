places = ["Italy","Japan","Norway","New Zealand","Argentina"]

#Print list normally
print(places)

#Print list alphabetically
print(sorted(places))
print(places)

#Print list reverse-alphabetically
print(sorted(places,reverse=True))
print(places)

print("\n Now we do some reverses.")
places.reverse()
print(places)
places.reverse()
print(places)

print("\n Now we sort.")
places.sort()
print(places)
places.sort(reverse=True)
print(places)