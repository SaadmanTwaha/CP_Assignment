
n = int(input("Enter number of total students:"))
d = {}
x = 1

for i in range(n):
    key = input(f"Enter name of student {x}: ")
    value = float(input(f"Enter marks of {key}: "))
    d[key] = value
    x = x+1

print("-----Result Summary-----")
total_marks = sum(d.values())
avg_marks = total_marks/n
print("Average Marks:", avg_marks)

print("Passed Students: ")
for key, value in d.items():
    if value >= 33:
        print(key, "- Marks",value)

print("Top Score")

max_value = max(d.values())

for key, value in d.items():
    if value == max_value:
        print(key, "- marks", value)






