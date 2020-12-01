def kronecker(matrix1, matrix2):
    '''
    Description:
        Implementation of the Matrix Kronecker Product.
        It takes two nested lists as inputs and output the result of the Kronecker Product in a nested list.
        The algorithm is essentially computing the output matrix row by row.

        Inspired by Rosetta Code implementation: https://rosettacode.org/wiki/Kronecker_product#Python
    Args:
        matrix1: a nested list [[], [], ...] representing an M x N matrix
        matrix2: a nested list [[], [], ...] representing a P x Q matrix
    Returns:
        matrix: [[], [], [], ...]
    '''

    # Initialize the output matrix.
    matrix = [] # output matirx
    row = [] # row (sublist) of the output matrix

    # Loop through the first matrix.
    for row1 in matrix1:
        row2 = 0 # fix row for matrix2 in each iteration
        # Loop through rows of the second matrix.
        for _ in range(len(matrix2)):
            # Compute the Kronecker Product row by row.
            for num1 in row1:
                for num2 in matrix2[row2]:
                    row.append(num1 * num2)
            matrix.append(row) # append the computed row to the output matrix
            row2 += 1
            row = [] # reinitialization for the next row computation
            
    return matrix

def print_matrix(matrix):
    '''
    Description:
        Helper function to print out a 2-dimensional matrix.
    Args:
        matrix: a nested list [[], [], ...] representing a 2-dimensional matrix
    Returns:
        None
    '''
    for row in matrix:
        print(row)

if __name__ == '__main__':
    A = [[1, 2, 3], [3, 2, 1]]
    B = [[2, 1], [2, 3]]
    print_matrix(kronecker(A, B))