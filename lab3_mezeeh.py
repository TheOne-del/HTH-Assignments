# Mezeeh Dolakeh | Lab 3 | Intro to Python 

# Ticket 1.
username = "Maverick45" #PREDICT: 10 characters
print(len(username)) # Yes, len counted every character.

# Ticket 2.
print(username[0]) # PREDICT: M and 5
print(username[9])
# The last index is minus 1 number because indexes start counting from 0 instead of 1

# Ticket 3.
first = "Welcome to Loop, @"
last = "Maverick45!"
full = first + last
print(full)
print(f"Welcome to Loop,@{username}!")
#PREDICT: Yes, both lines will look identical
# Using the f-string felt eaiser than the concatenation because I wasn't creating multiple variables.

# Ticket 4.
#username[0] = "X" 
"""
"/Users/grandmasterbaiter/Desktop/HTH-Assignments/lab3_mezeeh.py", line 22, in <module>
    username[0] = "X"
    ~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
"""
#PREDICT: It will print error as X is not the 0 index of username
# Immutable means a string cannot be changed once it's created

# Ticket 5.
feed = ["Prime was a problem", "Haaland inspires me endlessly", "GTA 6 PRICE REVEALED"]
print(len(feed))
print(feed[0])
# PREDICT: 3, First caption will be Prime was a problem
# I used 0 for the first post's index

# Ticket 6.
feed.append("this is a message to AI")
print(feed)
#PREDICT: 3
# The fourth post sits at 3 because indexes start counting from 0

# Ticket 7.
feed.pop(0)
feed.sort()
print(feed)
#PREDICT: Prime was a problem gets removed and the rest will be GTA 6 PRICE REVEALED,Haaland inspires me endlessly,this is a message to AI
# I used the alphabetical order method which sorted them based on the first letter of each phrase and the delete by position method which removed a phrase based on its position.

# Ticket 8
profile = {"username": "MAVERICK45", "followers": 1200, "verified": True}
print(profile["followers"])
#print(profile[0])
#PREDICT: Follower prints 1200 and profile[0] tries to use an index
"""
 "/Users/grandmasterbaiter/Desktop/HTH-Assignments/lab3_mezeeh.py", line 53
    profile = {"username": "followers": 1200, "verified": True}
                                      ^
SyntaxError: invalid syntax
"""
# Dictionaries are more complex than lists and using keys keeps the input fixed even if the order changes

# Ticket 9.
profile["followers"] += 50
profile["bio"] = "I am a guitarist"
print(profile)
profile["age"] = profile.get("age")#PREDICT: It prints none as there is no value assigned to age
print(profile)
# .get() is safer when you are not sure the key exsits because it allows you to bypass the error from python if you were to use profile["age"

# Ticket 10.
print(f"@{profile["username"]} has {profile["followers"]} followers and {len(feed)} posts. Top post: {feed[0]}")
#PREDICT: @MAVERICK45 has 1250 followers and 3 posts. Top post: GTA 6 PRICE REVEALED
# I used strings, lists, and dictionairies 

