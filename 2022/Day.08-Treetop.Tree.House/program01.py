import sys

tree_rows = []
tree_cols = []

visibile = 0

for line in sys.stdin:
    tree_rows.append([int(e) for e in list(line.strip())])
tree_cols = [[tree_rows[j][i] for j in range(len(tree_rows))] for i in range(len(tree_rows[0]))]


for i in range(len(tree_rows[0])):
    for j in range(len(tree_rows)):
        # Outer Edges are always visibile
        if i in [0,len(tree_rows[0])-1] or j in [0,len(tree_rows)-1]:
            visibile += 1
            continue
        up = max(tree_cols[j][0:i]) >= tree_rows[i][j]
        down = max(tree_cols[j][i+1:]) >= tree_rows[i][j]
        left = max(tree_rows[i][0:j]) >= tree_rows[i][j]
        right = max(tree_rows[i][j+1:]) >= tree_rows[i][j]
        if not(up and down and left and right):
            visibile += 1
            print(f"[{i}][{j}]")

print(visibile)
