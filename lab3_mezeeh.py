# Mezeeh Dolakeh | Lab 3 | Intro to Python 

# Ticket 1.
#PREDICT: 10 characters
username = "Maverick45" 
print(len(username)) # Yes, len counted every character.

# Ticket 2.
# PREDICT: M and 5
print(username[0]) 
print(username[9])
# The last index is minus 1 number because indexes start counting from 0 instead of 1

# Ticket 3.
#PREDICT: Yes, both lines will look identical
first = "Welcome to Loop, @"
last = "Maverick45!"
full = first + last
print(full)
print(f"Welcome to Loop,@{username}!")
# Using the f-string felt eaiser than the concatenation because I wasn't creating multiple variables.

# Ticket 4.
#PREDICT: It will print error as X is not the 0 index of username
#username[0] = "X" 
"""
"/Users/grandmasterbaiter/Desktop/HTH-Assignments/lab3_mezeeh.py", line 22, in <module>
    username[0] = "X"
    ~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
"""
# Immutable means a string cannot be changed once it's created

# Ticket 5.
# PREDICT: 3, First caption will be Prime was a problem
feed = ["Prime was a problem", "Haaland inspires me endlessly", "GTA 6 PRICE REVEALED"]
print(len(feed))
print(feed[0])
# I used 0 for the first post's index

# Ticket 6.
#PREDICT: 3
feed.append("this is a message to AI")
print(feed)
# The fourth post sits at 3 because indexes start counting from 0

# Ticket 7.
#PREDICT: Prime was a problem gets removed and the rest will be GTA 6 PRICE REVEALED,Haaland inspires me endlessly,this is a message to AI
feed.pop(0)
feed.sort()
print(feed)
# I used the alphabetical order method which sorted them based on the first letter of each phrase and the delete by position method which removed a phrase based on its position.

# Ticket 8
#PREDICT: Follower prints 1200 and profile[0] tries to use an index
profile = {"username": "MAVERICK45", "followers": 1200, "verified": True}
print(profile["followers"])
#print(profile[0])
"""
 "/Users/grandmasterbaiter/Desktop/HTH-Assignments/lab3_mezeeh.py", line 53
    profile = {"username": "followers": 1200, "verified": True}
                                      ^
SyntaxError: invalid syntax
"""
# Dictionaries are more complex than lists and using keys keeps the input fixed even if the order changes

# Ticket 9.
#PREDICT: It prints none as there is no value assigned to age
profile["followers"] += 50
profile["bio"] = "I am a guitarist"
print(profile)
profile["age"] = profile.get("age")
print(profile)
# .get() is safer when you are not sure the key exsits because it allows you to bypass the error from python if you were to use profile["age"

# Ticket 10.
#PREDICT: It prints none as there is no value assigned to age
print(f"@{profile["username"]} has {profile["followers"]} followers and {len(feed)} posts. Top post: {feed[0]}")
# I used strings, lists, and dictionairies 

