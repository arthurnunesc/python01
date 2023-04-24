from vector import Vector


def main():
    vector_column_1 = Vector([[1.5], [2.5], [3.5]])
    vector_column_2 = Vector([[2], [2], [2]])
    print(vector_column_1.__dict__)
    print(vector_column_2.__dict__)
    print(vector_column_1.dot(vector_column_2))
    print(vector_column_1.T())

    vector_row_1 = Vector([[1.5, 2.5, 3.5]])
    vector_row_2 = Vector([[2, 2, 2]])
    print(vector_row_1.__dict__)
    print(vector_row_2.__dict__)
    print(vector_row_1.dot(vector_row_2))
    print(vector_row_1.T())
    
    # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    # Vector([[0.0], [5.0], [10.0], [15.0]])

    # Row vector of shape 1 * n 
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    # Vector([[0.0, 5.0, 10.0, 15.0]])

    v2 = v1 / 2.0
    print(v2)
    # Vector([[0.0], [0.5], [1.0], [1.5]])

    # v1 / 0.0
    # ZeroDivisionError: division by zero.

    # 2.0 / v1
    # NotImplementedError: Division of a scalar by a Vector is not defined here.

    # Column vector of shape (n, 1)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    # Expected output: (4,1)

    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    # Expected output: [[0.0], [1.0], [2.0], [3.0]]

    # Row vector of shape (1, n)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    # Expected output (1,4)

    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    # Expected output [[0.0, 1.0, 2.0, 3.0]]
    
    # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    # Expected output:(4,1)
    
    print(v1.T())
    # Expected output: Vector([[0.0, 1.0, 2.0, 3.0]])
    
    print(v1.T().shape)
    # Expected output: (1,4)
    
    # Example 2:
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)
    # Expected output: (1,4)
    
    print(v2.T())
    # Expected output: Vector([[0.0], [1.0], [2.0], [3.0]])
    
    print(v2.T().shape)
    # Expected output: (4,1)


    ### TODO ###
    # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))
    # Expected output: 18.0
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))
    # Expected output: 13.0
    repr(v1)
    # Expected output: to see what __repr__() should do
    # [[0.0, 1.0, 2.0, 3.0]]
    print(v1)
    # Expected output: to see what __str__() should do
    # [[0.0, 1.0, 2.0, 3.0]]

    print(Vector([[0.0, 1.0, 2.0, 3.0]]))
    print(Vector([[0.0], [1.0], [2.0], [3.0]]))
    print(Vector(3))
    # values = [[0.0], [1.0], [2.0]]
    print(Vector((10,16)))
    # values = [[10.0], [11.0], [12.0], [13.0], [14.0], [15.0]]
    print(Vector((2,0)))
    # if a > b, you must display accurate error message.            

if __name__ == "__main__":
    main()
