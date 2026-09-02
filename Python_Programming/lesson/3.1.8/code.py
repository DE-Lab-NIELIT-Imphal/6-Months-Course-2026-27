# Opening a file, if no file exist then auto creates
f = open("data.txt", "r")

# reading the file and then printing the contents of the file
print(f.read())

# closing the file after accesing the contents to save up memory otherwise it will open in the background
f.close()

# ---------------------------------------------
# writing
f = open("data.txt", "w")
f.write("The Drone is in GUIDED mode")

f = open("data.txt", "r")
print(f.read())
f.close


# ---------------------------------------------
# appending

f = open("data.txt", "a")
f.write("\nStarting autonomous flight")

f = open("data.txt", "r")
print(f.read())
f.close


# ---------------------------------------------
# in actual implementation

with open("data.txt", "r") as f:
    print(f.read())
