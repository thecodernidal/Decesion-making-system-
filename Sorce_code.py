# -------- INPUT --------
n_criteria = int(input("Enter number of criteria: "))

criteria = []
types = []
ranks = []

for i in range(n_criteria):
    name = input(f"Enter name of criterion {i+1}: ")
    ctype = input("Type (benefit/cost): ")
    rank = int(input("Priority rank (1 highest): "))
    
    criteria.append(name)
    types.append(ctype)
    ranks.append(rank)

n_options = int(input("\nEnter number of options: "))

options = []
matrix = []

for i in range(n_options):
    option_name = input(f"\nEnter name of option {i+1}: ")
    options.append(option_name)

    values = []
    for j in range(n_criteria):
        val = float(input(f"Enter value for {criteria[j]}: "))
        values.append(val)

    matrix.append(values)

# -------- CONVERT RANK → WEIGHT --------
weights = []
total_weight = 0

for r in ranks:
    weight = (n_criteria - r + 1)
    weights.append(weight)
    total_weight += weight

# Normalize weights
for i in range(len(weights)):
    weights[i] = weights[i] / total_weight

# -------- NORMALIZATION --------
normalized = []

for j in range(n_criteria):
    column = []
    for i in range(n_options):
        column.append(matrix[i][j])

    max_val = max(column)
    min_val = min(column)

    for i in range(n_options):
        if j == 0:
            normalized.append([])

        if types[j] == "benefit":
            norm_value = matrix[i][j] / max_val
        else:  # cost
            norm_value = min_val / matrix[i][j]

        normalized[i].append(norm_value)

# -------- CALCULATE SCORES --------
scores = []

for i in range(n_options):
    score = 0
    for j in range(n_criteria):
        score += normalized[i][j] * weights[j]
    scores.append(score)

# -------- FIND BEST OPTION --------
best_index = 0
best_score = scores[0]

for i in range(1, n_options):
    if scores[i] > best_score:
        best_score = scores[i]
        best_index = i

# -------- OUTPUT --------
print("\n--- RESULTS ---")
for i in range(n_options):
    print(options[i], ":", round(scores[i], 4))

print("\nBest Option:", options[best_index])
print("Score:", round(best_score, 4))
