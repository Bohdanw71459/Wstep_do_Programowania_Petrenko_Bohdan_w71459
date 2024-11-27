# a) 1, 2, 3, ..., 99, 100
print("a) ", end="")
for i in range(1, 101):
    print(i, end=", " if i < 100 else "\n")

# b) 100, 99, ..., 2, 1, 0
print("b) ", end="")
for i in range(100, -1, -1):
    print(i, end=", " if i > 0 else "\n")

# c) 7, 14, 21, ..., 70, 77
print("c) ", end="")
for i in range(7, 78, 7):
    print(i, end=", " if i < 77 else "\n")

# d) 20, 18, ..., 2, 0
print("d) ", end="")
for i in range(20, -1, -2):
    print(i, end=", " if i > 0 else "\n")
