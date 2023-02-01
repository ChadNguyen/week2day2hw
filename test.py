user_input = input("enter a string with some vowels: ")
print("input string: " + str(user_input))
non_vowels = ('a','e','i','o','u','A','E','I','O','U')
new_string="";
for i in range(0,len(user_input),1):
    if user_input[i] in non_vowels:
        print ('found a vowel, removing...')
    else:
        new_string+=user_input[i]
print("I've removed the vowels for you. You're welcome! The new string is: " + new_string)