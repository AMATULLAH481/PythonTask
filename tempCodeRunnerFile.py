names = ["Mayowa", "chizoba", "Chigozie"]
new_list = []

for name in names: 
    if name[0].isupper() and name.endswith("a"):
        new_list.append(name)

print(new_list)
