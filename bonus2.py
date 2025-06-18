# asks the user
name:str = input("Enter your name: ")
email:str = input("Enter your email: ")

# if statement
if len(name) > 2:
    if "@gmail.com" in email and email.index("@gmail.com") >0 and email.count("@")==1 and email.count(" ")==0:
        print("Welcome",name,", you registered with the email",email)
    else:
         print(" the email is not valid , please provide a valid email .")

else:
    print("the name length must be more than 2 characters, please provide a valid name.")
