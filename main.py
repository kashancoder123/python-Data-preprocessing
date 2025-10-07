import matplotlib.pyplot as plt

print("Hi! I am your Data Helper Bot.")
print("Students Data")

# Step 1: Students Data (Name and Age only)
data = [
    {"Name": "smith", "Age": 5},
    {"Name": "john", "Age": None},
    {"Name": "jane", "Age": 10},
    {"Name": "doe", "Age": None},
    {"Name": "alice", "Age": 15},
    {"Name": "bob", "Age": 20},
    {"Name": "eve", "Age": None},
    {"Name": "charlie", "Age": 25},
    {"Name": "haris", "Age": None},
    {"Name": "anna", "Age": 30},
    {"Name": "mike", "Age": 35},
    {"Name": "linda", "Age": None},
    {"Name": "tom", "Age": 40},
    {"Name": "jerry", "Age": None},
    {"Name": "nancy", "Age": 45},
    {"Name": "paul", "Age": None},
    {"Name": "kate", "Age": 50},
    {"Name": "sam", "Age": None},
    {"Name": "lucy", "Age": 55},
    {"Name": "dave", "Age": None},
]

print("\nOriginal Data:")
for row in data:
    print(row)

# Step 2: Fill missing ages
print("\nFiltering missing ages with 25...")
for row in data:
    if row["Age"] is None:
        row["Age"] = 25

# Step 3: Show processed data
print("\nProcessed Data:")
for row in data:
    print(row)

# Step 4: Plot ages
names = [row["Name"] for row in data]
ages = [row["Age"] for row in data]

# 🎨 Multi-color bars
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan', 'magenta', 'brown']

plt.bar(names, ages, color=colors)
plt.title("Students Data")
plt.xlabel("Names")
plt.ylabel("Ages")
plt.xticks(rotation=45, ha='right')

# ✅ Add age values on top of each bar
for i, age in enumerate(ages):
    plt.text(i, age + 0.3, str(age), ha='center', fontsize=9, color='black')

plt.tight_layout()
plt.show()

print("\nGreat! You can see the ages of students in the plot!")
