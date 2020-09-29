
#Question 1 Task
songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])

print(songs[2])

#Will print Rockstar and Do It, cutting off For The Night
#Question 2 Task
print(songs[0:2])

songs[0] = "Dynamite"

print(songs)

#Question 3 task
songs[2] = "Greyhound"

print(songs)

#Question 4 Task

songs.append("Mood")

songs.extend(["Crying Now", "Blinding Lights"])

songs.insert(0, "Life is Good")

songs.extend(["Electric Love", "Tu", "Mercy"])

print(songs)

#Question 4 Task 2

songs.remove("Mood")

songs.pop(4)

del songs[4]

print(songs)

#Question 6 Final Task

animals = ["Ostrich", "Alpaca", "Shark"]

print(animals)

animals.append("Cow")

print(animals)

print(animals[2])

del animals[0]

print(animals)

for i in range(len(animals)):
    print(animals[i])

