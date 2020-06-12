import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

cache = {}

# Replace the nested for loops below with your improvements

# ***** Initial nested loops 5.95sec, 5.66sec, 5.46sec *****
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# **** Using a dictionary 0.0065sec, 0.0079sec, 0.0080sec ****
# for name_1 in names_1:
#     cache[name_1] = True

# for name_2 in names_2:
#     if name_2 in cache:
#         duplicates.append(name_2)

# **** Using set() 0.0039sec, 0.0051sec, 0.0049sec ****
temp = set(names_1)
duplicates = [name for name in names_2 if name in temp]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
    # I'm not sure if using the set() method is what was meant, but it seems to be slightly faster than using a dictionary
# What's the best time you can accomplish?  There are no restrictions on techniques or data
    # So far, the best time I recoreded for these attempts was 0.0039 seconds
# structures, but you may not import any additional libraries that you did not write yourself.
