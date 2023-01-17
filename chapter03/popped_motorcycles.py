#Initial List
motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles)

#"pop" the last item from a list
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)

#"pop" the first item from a list
motorcycles = ["honda","yamaha","suzuki"]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I ever owned was a {first_owned.title()}.")

