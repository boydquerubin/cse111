# first_name = input("Enter your first name: ")
# first_name_initial = first_name[0:1]
# last_name = input("Enter your first name: ")
# last_name_initial = last_name[0:1]

# print("Your initials are: " + first_name_initial.upper() + last_name_initial.upper())

def get_initial(name, force_uppercase=True):
  if force_uppercase:    
    initial = name[0:1].upper()
  else:
    initial = name[0:1]
  return initial

first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name)
last_name = input("Enter your first name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial + last_name_initial)

