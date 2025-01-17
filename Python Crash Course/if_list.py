current_users = ['a','b','c', 'd', 'e']
new_users = ['a', 'b', 'f', 'g', 'h']

for users in new_users:
    if users.lower() in current_users:
        print("This username already exist, choose another one")
    else:
        print("The username is available")