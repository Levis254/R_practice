names=[]
with open("names.txt", "w+") as file:
    for _ in range(3):
        name=input("Enter your name:")
        file.write(f"{name}\n")
        names.append(name)


print(names)