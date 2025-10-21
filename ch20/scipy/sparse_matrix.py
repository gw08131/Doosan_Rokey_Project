# sparse_matrix.py

from scipy.sparse import csr_matrix

data = [[0,0,3,0,0],
        [0,4,0,1,0],
        [0,0,0,5,0],
        [0,0,0,0,0]
]

sparse_matrix = csr_matrix(data)
print(sparse_matrix)
print(sparse_matrix.data)       # [3 4 1 5]