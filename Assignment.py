"""def first_name(my_first_name:str):
    return(my_first_name)

def last_name(my_last_name:str):
    return(my_last_name)

def fullname(my_first_name, my_last_name):
    return f"My full name is {first_name(my_first_name)} {last_name(my_last_name)}"

print(fullname("Mahmud", "Amatullah"))"""


"""attribute_list = ["first name", "last_name", "date of birth"]
converted_value = []
for attribute in attribute_list:
    #for each_letter in attribute:
        #print(each_letter)
    if " " in attribute:
        converted_value.append(attribute.replace(" ", "_"))
    else:
        converted_value.append(attribute)
print(converted_value)"""

"""attribute_list = ["first name", "last_name", "date of birth"]
converted_value = []

for attribute in attribute_list:
    if " " in  attribute[0]:
        converted_value.append(attribute.replace(" ", "_"))
    else:
        converted_value.append(attribute)
print(converted_value)"""


           
#print("My name is", each_letter), #We need to understand why this is showing the last letter in the index

"""names = ["Mayowa", "chizoba", "Chigozie"]
new_list = []

for name in names:
    if name[0].isupper() and name.endswith("a"): #Going in without an index is giving an empty list and that is because upper is a method
        new_list.append(name)
    elif name[0].isupper() and not name.endswith("a"):
        new_list.append(name[:-1] + "a") #we cannot use the replace method because we are assuming we do not know the last letter

print(new_list)"""

"""names = ["Mayowa", "chizoba", "Chigozie"]
print(names[:-1])"""

data_names = ["Wofai", "Zainab", "A4atullah"]
new = []

def error_spotter(): #are we going to have a the list or element as a parameter? can we have a list as a parameter?
    for name in data_names:
        for letter in name:
            if not letter.isalpha():
                 print (f"The name {name} in the data received contains a foreign value")

   
            
error_spotter()
