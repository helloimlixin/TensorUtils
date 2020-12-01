#
# Created on Tue Dec 01 2020
#
# The MIT License (MIT)
# Copyright (c) 2020 Xin Li
# Insitution: Department of Electrical and Computer Engineering, Rutgers University New Brunswick
# Email: xl598@scarletmail.rutgers.edu
# Personal Website: helloimlixin.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import time

def timeme(function):
    """Helper annotation function for performance measure.

    Contains a wrapper function that computes method runtime by seconds.

    Args:
        function: function to annotate for time measure.

    Returns:
        wrapper: a wrapper function for time measure.
    """

    def wrapper(*args, **kwargs):
        """Wrapper function to compute function runtime.

        Uses time library.

        Args:
            *args: non-keyworded variable length argument list passed to the
            wrapper function.
            **kwargs: keyworded variable length argument list passed to the
            wrapper function.

        Returns:
            result: execution time in seconds.
        """
        start_time = time.time() * 1000
        result = function(*args, **kwargs)
        end_time = time.time() * 1000
        print("Execution time: {}".format((end_time - start_time) / 1000))
        return result

    return wrapper

@timeme
def kronecker(matrix1, matrix2):
    """Implementation of the Matrix Kronecker Product.
        It takes two nested lists as inputs and output the result of the Kronecker Product in a nested list.
        The algorithm is essentially computing the output matrix row by row.

        Inspired by Rosetta Code implementation: https://rosettacode.org/wiki/Kronecker_product#Python.

        Reference: https://archive.siam.org/books/textbooks/OT91sample.pdf.

    Args:
        matrix1 ([[], [], ...]): a nested list representing an I x K matrix
        matrix2 ([[], [], ...]): a nested list representing a J x L matrix

    Returns:
        nested list [[], [], ...]: a nested list representing the output matrix
    """

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