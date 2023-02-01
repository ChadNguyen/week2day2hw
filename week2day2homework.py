#Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names

first_names = ['John', 'Evan', 'Jordan', 'Max']
last_names = ['Smith', 'Smith', 'Williams', 'Bell']

def full_name(first_names, last_names):
    full_name= []
    for i in range(0, len(first_names)):
        full_name.append(first_names[i] + " " + last_names[i])
    return full_name
print(full_name(first_names,last_names))
