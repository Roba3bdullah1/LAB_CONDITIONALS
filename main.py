#Create a variables
movie:str = "Lost"
movieRate:int = 3
score:float = 72.65

# If statement
if movieRate >= 4 and score > 80:
    print("Highly recommended")
elif movieRate >= 3 and score > 70:
    print("I recommended it . It is good")
elif movieRate <= 2 and score > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")