s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1 - s2) # {1, 2, 3}
print(s1.difference(s2)) # {1, 2, 3}

print(s2 - s1) # {8, 6, 7}
print(s2.difference(s1)) # {8, 6, 7}
