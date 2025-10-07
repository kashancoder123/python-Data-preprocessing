import matplotlib.pyplot as plt

print("Hi! I am your Data Helper Bot.")
print("Let's work with the Titanic data!")

# Step 1: Sample Titanic data (Name and Age only)
data = [
    {"Name": "John Doe", "Age": 22},
    {"Name": "Jane Smith", "Age": None},
    {"Name": "Alice Johnson", "Age": 30},
    {"Name": "Bob Brown", "Age": None},
    {"Name": "Charlie White", "Age": 25},
    {"Name": "Diana Green", "Age": None},
    {"Name": "Eve Black", "Age": 28},  # ✅ Missing comma added here
    {"Name": "Frank Blue", "Age": 35},
    {"Name": "Grace Yellow", "Age": None},
    {"Name": "Hank Red", "Age": 40},
]

print("\nOriginal Data:")
for row in data:
    print(row)

# Step 2: Filter missing ages
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

plt.bar(names, ages, color='blue')
plt.title("Titanic Passengers' Ages")
plt.xlabel("Names")
plt.ylabel("Ages")
plt.xticks(rotation=45, ha='right')  # ✅ Rotates labels for better readability
plt.tight_layout()
plt.show()

print("\nGreat! You can see the ages of Titanic passengers in the plot!")
