from typing import List


def shape(vector: List[List[float]]):
    rows = 0
    cols = 0
    cols_aux = 0
    for row in vector:
        if cols == 0:
            for col in row:
                cols += 1
        else:
            for col in row:
                cols_aux += 1
        if cols_aux != 0 and cols != cols_aux:
            return False
        cols_aux = 0
        rows += 1
    return (rows, cols)


def validate_vector(vector: List[List[float]]):
    validated_vector = vector
    for list in validated_vector:
        for number in list:
            if type(number) is float:
                continue
            elif type(number) is int:
                number = float(number)
            else:
                return False
    return validated_vector


class Vector:
    def __init__(self, values: List[List[float or int]]):
        self.values = validate_vector(values)
        if self.values:
            pass
        else:
            raise AssertionError("Vector has values that are not numbers")

        self.shape = shape(values)
        if self.shape:
            pass
        else:
            raise AssertionError("Assymetrical vector")

    def dot(self, other):
        if not isinstance(other, Vector):
            raise AssertionError("Argument is not a Vector object")
        elif self.shape != other.shape:
            raise AssertionError("The shapes of the vectors are different")
        cols, rows = self.shape
        result_vector: List[List[float]] = [[]]
        if cols > 1:
            result_vector = [[None]] * cols
            for index in range(cols):
                result_vector[[index][0]] = [
                    self.values[index][0] * other.values[index][0]
                ]
        else:
            result_vector = [[None] * rows]
            for index in range(rows):
                result_vector[0][index] = self.values[0][index] * other.values[0][index]

        return Vector(result_vector)

    def T(self):
        cols, rows = self.shape
        transposed_vector: List[List[float]] = [[]]
        if cols > 1:
            transposed_vector = [[None] * cols]
            for index in range(cols):
                transposed_vector[0][index] = self.values[index][0]
        else:
            transposed_vector = [[None]] * rows
            for index in range(rows):
                transposed_vector[[index][0]] = [self.values[0][index]]
        
        return Vector(transposed_vector)

    def __mul__(self, number: int or float):
        cols, rows = self.shape
        result_vector: List[List[float]] = [[]]
        if cols > 1:
            result_vector = [[None]] * cols
            for index in range(cols):
                result_vector[[index][0]] = [self.values[index][0] * number]
        else:
            result_vector = [[None] * rows]
            for index in range(rows):
                result_vector[0][index] = self.values[0][index] * number

        return Vector(result_vector)

    def __rmul__(self, number):
        raise NotImplementedError(
            "Multiplication of a scalar by a Vector is not defined here."
        )

    def __truediv__(self, number: int or float):
        cols, rows = self.shape
        result_vector: List[List[float]] = [[]]
        if cols > 1:
            result_vector = [[None]] * cols
            for index in range(cols):
                result_vector[[index][0]] = [self.values[index][0] / number]
        else:
            result_vector = [[None] * rows]
            for index in range(rows):
                result_vector[0][index] = self.values[0][index] / number

        return Vector(result_vector)

    def __rtruediv__(self, number):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here."
        )

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        print(str(self.values)) 
        return str(self.values)
