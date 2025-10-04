# ==============================================
# **CIR 203 HOMEWORK ONE SOLUTIONS**
# ==============================================

import numpy as np

# ==============================================
# **EXERCISE 1: NUMPY ARRAYS (BANKING SECTOR)**
# ==============================================

transactions = np.array([
    [1200, 1500, 1600, 1700, 1400, 1800],  # Branch 1
    [1000, 1100, 1050, 1300, 1250, 1350],  # Branch 2
    [2000, 2100, 1900, 2200, 2300, 2400],  # Branch 3
    [900,  950,  1000, 1100, 1150, 1200]   # Branch 4
])

print("EXERCISE 1: NUMPY ARRAYS (BANKING SECTOR)")
print("Transactions Array:\n", transactions)

total_per_branch = np.sum(transactions, axis=1)
print("Total per branch:", total_per_branch)

highest_branch = np.argmax(total_per_branch) + 1
print("Branch with highest transactions: Branch", highest_branch)

avg_monthly = np.mean(transactions)
print("Average monthly transactions:", avg_monthly)

reshaped = transactions.reshape(3, 8)
print("Reshaped Array (3x8):\n", reshaped)
print("NOTE: Reshaping changes layout, not data.\n")


# ==============================================
# **EXERCISE 2: PYTHON LISTS (LOGISTICS SECTOR)**
# ==============================================

routes = ["Nairobi-Kisumu", "Mombasa-Malindi", "Nakuru-Eldoret",
          "Nyeri-Nanyuki", "Garissa-Mwingi", "Kitale-Bungoma",
          "Narok-Kajiado", "Isiolo-Marsabit", "Naivasha-Gilgil",
          "Thika-Muranga"]

print("EXERCISE 2: PYTHON LISTS (LOGISTICS SECTOR)")
print("Routes:", routes)

routes.append("Kakamega-Busia")
routes.remove("Garissa-Mwingi")
print("Updated routes:", routes)

routes.sort()
routes.reverse()
print("Sorted & reversed routes:", routes)

count_N = sum(1 for r in routes if r.startswith("N"))
print("Routes starting with N:", count_N)

long_routes = [r for r in routes if len(r) > 10]
print("Routes longer than 10 chars:", long_routes, "\n")


# ==============================================
# **EXERCISE 3: PYTHON TUPLES (HEALTHCARE SECTOR)**
# ==============================================

print("EXERCISE 3: PYTHON TUPLES (HEALTHCARE SECTOR)")
patient = ("Motanya Justin", 45, "120/80", 72)
print("Patient tuple:", patient)
print("Age:", patient[1], "Heart Rate:", patient[3])

print("WHY TUPLES? They are immutable, ensuring patient vitals are not accidentally changed.")

patient_list = list(patient)
patient_list[3] = 75
patient = tuple(patient_list)
print("Updated patient tuple:", patient)

patients = (
    ("Motanya Justin", 45, "120/80", 75),
    ("Jane Smith", 30, "110/70", 80),
    ("Paul Kamau", 55, "140/90", 85),
    ("Alice Wanjiku", 40, "125/85", 78),
    ("Peter Otieno", 60, "135/88", 82)
)
names = [p[0] for p in patients]
print("Patient names:", names, "\n")


# ==============================================
# **EXERCISE 4: PYTHON DICTIONARIES (E-COMMERCE SECTOR)**
# ==============================================

print("EXERCISE 4: PYTHON DICTIONARIES (E-COMMERCE SECTOR)")
inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Headphones": 20,
    "Monitor": 5,
    "Keyboard": 12
}
print("Initial inventory:", inventory)

inventory["Mouse"] = 18
inventory["Phone"] = 10
print("Updated inventory:", inventory)

def low_stock(inv):
    return {product: qty for product, qty in inv.items() if qty < 10}

print("Low stock items:", low_stock(inventory))

del inventory["Monitor"]
print("Inventory after deletion:", inventory)

print("Final inventory listing:")
for product, qty in inventory.items():
    print(product, ":", qty)
