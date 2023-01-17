#Initial list
motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles)

#Changing the first item in the list
motorcycles[0] = "ducati"
print(motorcycles)

#Add a new motorcycle to the end of the list
motorcycles.append("honda")
print(motorcycles)

#Add a new motorcycle to the beggining of a list
motorcycles.insert(0,"motorcyclone")
print(motorcycles)

#Add a new motorcycle to the middle of a list
motorcycles.insert(2,"toyota")
print(motorcycles)

#Removing items from a list
del motorcycles[0]
print(motorcycles)