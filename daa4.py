class Item:
    def _init_(self, value, weight):
        self.value = value
        self.weight = weight


def print_dp_table(dp):
    print("\nDP Table (Rows = Items, Columns = Capacity):")
    for row in dp:
        for val in row:
            print(f"{val:4}", end=" ")
        print()
    print()


def knapsack(capacity, items):
    n = len(items)

    # DP table (n+1) x (capacity+1)
    dp = [0 * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w],
                               items[i - 1].value + dp[i - 1][w - items[i - 1].weight])
            else:
                dp[i][w] = dp[i - 1][w]

    # Print DP table after filling
    print_dp_table(dp)

    # Backtracking to find selected items
    result = dp[n][capacity]
    w = capacity

    print("Items Selected (weight, value):")
    for i in range(n, 0, -1):
        if result == dp[i - 1][w]:
            continue  # item not taken
        else:
            print(f"Item(weight={items[i - 1].weight}, value={items[i - 1].value})")
            result -= items[i - 1].value
            w -= items[i - 1].weight

    return dp[n][capacity]


# ---------------- MAIN PROGRAM ----------------

print("0-1 Knapsack Problem using Dynamic Programming\n")

n = int(input("Enter the number of items: "))
items = []

print("\nEnter the value and weight for each item:")
for i in range(n):
    value = int(input(f"Value of item {i + 1}: "))
    weight = int(input(f"Weight of item {i + 1}: "))
    items.append(Item(value, weight))

capacity = int(input("\nEnter capacity of the knapsack: "))

max_profit = knapsack(capacity, items)

print(f"\nMaximum Profit = {max_profit}\n")