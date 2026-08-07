def create_user_profile(username, age=19, premium=False):
    #Your Problem 3 solution
    if premium == True:
        return f"{username} (age: {age}) - Premium User"
    else:
        return f"{username} (age: {age}) - Standard User"

print(create_user_profile("Kevalin",19))
print(create_user_profile("Matalada"))
print(create_user_profile("Piti",24,True))