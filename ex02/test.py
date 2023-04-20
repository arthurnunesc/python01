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

    v1 / 0.0
    # ZeroDivisionError: division by zero.

    2.0 / v1
    # NotImplementedError: Division of a scalar by a Vector is not defined here.


if __name__ == "__main__":
    main()
