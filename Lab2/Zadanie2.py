rows = int(input("Ile gwiazdek? "))

for _ in range(rows):
    print("* * *")
  
print("\n")

for i in range(1, rows + 1):
    print("*" * i)

print("\n")

for i in range(1, rows + 1):
    print("* " * i)
