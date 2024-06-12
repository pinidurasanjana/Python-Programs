total = 0
count = 0
score = int(input("Enter score, (Enter -9 to end): "))
while score != -9:
    total = total + score
    count += 1
    score = int(input("Enter another score, (Enter -9 to end): "))
average = float((total) / count)
print("class average is", average)
