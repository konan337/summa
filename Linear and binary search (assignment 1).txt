# lab assignment 1
# In an e-commerce system, customer account IDs are stored in a list,
# and you are tasked with writing a program that implements:
# • Linear Search
# • Binary Search

# Function for Linear Search
def linear_search(customer_ids, target_id):
    for i in range(len(customer_ids)):
        if customer_ids[i] == target_id:
            return i
    return -1

# Function for Binary Search
def binary_search(customer_ids, target_id):
    low = 0
    high = len(customer_ids) - 1

    while low <= high:
        mid = (low + high) // 2
        if customer_ids[mid] == target_id:
            return mid
        elif customer_ids[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Main Program
# Take list of customer IDs from user
n = int(input("Enter number of customer account IDs: "))
customer_ids = []

for i in range(n):
    cid = int(input(f"Enter Customer ID {i+1}: "))
    customer_ids.append(cid)

print("\nCustomer Account IDs entered:", customer_ids)

# Take target ID from user
target_id = int(input("\nEnter Customer ID to search: "))

# Perform Linear Search
result_linear = linear_search(customer_ids, target_id)
if result_linear != -1:
    print(f"[Linear Search] Customer ID {target_id} found at index {result_linear}.")
else:
    print(f"[Linear Search] Customer ID {target_id} not found.")

# Perform Binary Search (requires sorted list)
customer_ids.sort()
result_binary = binary_search(customer_ids, target_id)
if result_binary != -1:
    print(f"[Binary Search] Customer ID {target_id} found at sorted index {result_binary}.")
else:
    print(f"[Binary Search] Customer ID {target_id} not found.")
