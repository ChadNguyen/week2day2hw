#Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names

first_names = ['John', 'Evan', 'Jordan', 'Max']
last_names = ['Smith', 'Smith', 'Williams', 'Bell']

def full_name(first_names, last_names):
    full_name= []
    for i in range(0, len(first_names)):
        full_name.append(first_names[i] + " " + last_names[i])
    return full_name
print(full_name(first_names,last_names))





#Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]
list = [1,11,14,5,8,9]

def list():
    for i in list:
        if i != 10: 
            list.pop(i)
    return list
print(list)
    
    
    

    




# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge(l_1,l_2):
    for i in l_2:
        newlist=l_1+l_2
        newlist.sort()
    return newlist
print(merge(l_1,l_2))


