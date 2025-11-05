# lab assignment 2
# In a company, employee salaries are stored in a list as floating-point numbers.
# Write a Python program that sorts the employee salaries in ascending order using:
# • Selection Sort
# • Bubble Sort
# After sorting, display the top five highest salaries.

# Function for Selection Sort
def selection_sort(salaries):
    n = len(salaries)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries

# Function for Bubble Sort
def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n):
        for j in range(0, n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries

# Main Program
n = int(input("Enter number of employees: "))
salaries = []

for i in range(n):
    s = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(s)

print("\nOriginal Salaries:", salaries)

# Selection Sort
sel_sorted = selection_sort(salaries.copy())
print("\nSalaries after Selection Sort:", sel_sorted)

# Bubble Sort
bub_sorted = bubble_sort(salaries.copy())
print("Salaries after Bubble Sort:", bub_sorted)

# Display top 5 highest salaries
top_5 = sorted(salaries, reverse=True)[:5]
print("\nTop 5 Highest Salaries:", top_5)
