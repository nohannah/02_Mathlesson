# 4. Ask the user to enter their last name in lower case, and then ask them to enter their first name in lower 
#case. Change the case of the last name to upper case, and capitalize the first name. Then, join them 
#together with a space between and display the whole name and the length of whole name
last_name= str(input("Enter last name in lower case:"))
first_name= str(input("Enter frist name in lower latter:")) 
last=last_name.upper()
first=first_name.capitalize()
print (last)
print(first)
name= last + first
print(last , first)
print(len(name))
