import random
when = ["Last Sunday", "20 days ago", "Yesterday", "Last Monday", "Last Year", "Once up on a time"]
who = ["Tiger", "Lion", "Rabbit", "Elephant", "Horse", "Peacock", "Parrot", "Monkey", "Panda"]
name =["Kranthi", "Palli", "Joshi", "Vishwa", "Jatin", "Sravya", "Ayesha", "Varsha", "Dude"]
residence = ["Jungle", "city", "town", "Hyderabad", "Erie", "Herndon"]
went = ["shopping", "dinner","water", "jogging","playing","meeting"]
happened = ["friends", "couple", "enemies", "strangers","bestfriends"]
print(random.choice(when)+ ", " + random.choice(who) + " went to jungle for drinking water " + "and met " + random.choice(happened))
print(random.choice(when)+ ", " + random.choice(name) + " went to " +random.choice(residence) + " for " + random.choice(went) + " and met " + random.choice(happened))