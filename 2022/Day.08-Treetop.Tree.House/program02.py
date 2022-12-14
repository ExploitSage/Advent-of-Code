import sys

tree_rows = []
tree_cols = []

max_scenic = 0

for line in sys.stdin:
    tree_rows.append([int(e) for e in list(line.strip())])
tree_cols = [[tree_rows[j][i] for j in range(len(tree_rows))] for i in range(len(tree_rows[0]))]


for i in range(len(tree_rows[0])):
    for j in range(len(tree_rows)):
        
        up = 0
        if i != 0:
            up_seg = tree_cols[j][0:i]
            up_seg.reverse()
            for tree in up_seg:
                if tree <= tree_rows[i][j]:
                    up += 1
                if tree == tree_rows[i][j]:
                    break
        
        
        down = 0
        if i != len(tree_rows[0])-1:
            down_seg = tree_cols[j][i+1:]
            for tree in down_seg:
                if tree <= tree_rows[i][j]:
                    down += 1
                if tree == tree_rows[i][j]:
                    break
            
        left = 0
        if j != 0:
            left_seg = tree_rows[i][0:j]
            left_seg.reverse()
            for tree in left_seg:
                if tree <= tree_rows[i][j]:
                    left += 1
                if tree == tree_rows[i][j]:
                    break
        
        right = 0
        if j != len(tree_rows)-1:
            right_seg = tree_rows[i][j+1:]
            for tree in right_seg:
                if tree <= tree_rows[i][j]:
                    right += 1
                if tree == tree_rows[i][j]:
                    break
        
        scenic_score = up*down*left*right
        if scenic_score > max_scenic:
            max_scenic = scenic_score

print(max_scenic)
