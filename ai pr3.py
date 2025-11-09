# Experiment 4: Implementation of Alpha-Beta Pruning Search Engine for Game Search
# Now with user input for leaf values and tree depth.

def minimax(depth, node_index, maximizing, values, alpha, beta, max_depth):
    # Base case: return value at leaf node
    if depth == max_depth:
        return values[node_index]

    if maximizing:
        best = float('-inf')
        for i in range(2):  # binary tree
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} (α={alpha}, β={beta})")
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} (α={alpha}, β={beta})")
                break
        return best


# --- User input section ---
print("Alpha-Beta Pruning Demonstration")

max_depth = int(input("Enter the depth of the game tree (e.g., 3): "))

num_leaves = 2 ** max_depth
print(f"Enter {num_leaves} leaf node values (space-separated): ")
values = list(map(int, input().split()))

if len(values) != num_leaves:
    print(f"Error: Expected {num_leaves} values, but got {len(values)}.")
else:
    print("Leaf node values:", values)
    optimal_value = minimax(0, 0, True, values, float('-inf'), float('inf'), max_depth)
    print("\nOptimal value at root node:", optimal_value)
