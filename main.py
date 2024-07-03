n=[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

node_a=1

node_b=2

def is_adjacent(matrix, node1, node2):
    if matrix[node1][node2]==1:
        return True
    return False

print(is_adjacent([[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]],0,1))


# matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
# Test.assert_equals(is_adjacent(matrix, 0, 1), True)
# Test.assert_equals(is_adjacent(matrix, 0, 2), False)
# Test.assert_equals(is_adjacent(matrix, 2, 1), True)

# matrix = [[0,1,0,1,1], [1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]
# Test.assert_equals(is_adjacent(matrix, 0, 3), True)
# Test.assert_equals(is_adjacent(matrix, 1, 4), False)
# Test.assert_equals(is_adjacent(matrix, 3, 2), True)