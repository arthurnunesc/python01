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
            return "Invalid vector values, values given are assymetric"
        cols_aux = 0
        rows += 1
    return (rows, cols)


def validate_vector(vector: List[List[float or int]]):
    validated_vector = vector
    for list in validated_vector:
        for number in list:
            if type(number) is float:
                continue
            elif type(number) is int:
                number = float(number)
            else:
                return "Invalid vector values, there is something that is not a number in it"
    return validated_vector


def generate_values_int_or_tuple(range_arg: int or tuple[int]):
    if type(range_arg) is int:
        if range_arg <= 0:
            return "Invalid range, number is negative or equal to zero"
        generated_values = [[None]] * range_arg
        # generated_values = [[None] * range_arg]
        for i in range(range_arg):
            generated_values[[i][0]] = [float(i)]
    elif type(range_arg) is tuple:
        if len(range_arg) > 2:
            return "Invalid range, more than two numbers were given on a tuple"
        if range_arg[0] > range_arg[1]:
            return "Invalid range, first number is bigger than second number"
        generated_values = [[None]] * int(range_arg[1] - range_arg[0])
        # generated_values = [[None] * range_arg[1] - range_arg[0]]
        j = 0
        for i in range(range_arg[0], range_arg[1]):
            generated_values[[j][0]] = [float(i)]
            j += 1
    return generated_values


class Vector:
    def __init__(self, values: List[List[float or int]] or int or tuple[int]):
        if type(values) is not int and type(values) is not tuple:
            self.values = validate_vector(values)
            self.shape = shape(values)
        else:
            self.values = generate_values_int_or_tuple(values)
            self.shape = shape(self.values)
        if type(self.values) is str:
            raise AssertionError(self.values)

        if type(self.shape) is str:
            raise AssertionError(self.shape)

    def dot(self, other):
        if not isinstance(other, Vector):
            raise AssertionError("Argument is not a Vector object")
            return 1
        elif self.shape != other.shape:
            raise AssertionError("The shapes of the vectors are different")
            return 1
        cols, rows = self.shape
        result_dot_product = 0.0
        if cols > 1:
            result_vector = [[None]] * cols
            for index in range(cols):
                result_vector[[index][0]] = [
                    self.values[index][0] * other.values[index][0]
                ]
                result_dot_product += self.values[index][0] * other.values[index][0]
        else:
            result_vector = [[None] * rows]
            for index in range(rows):
                result_vector[0][index] = self.values[0][index] * other.values[0][index]
                result_dot_product += self.values[0][index] * other.values[0][index]

        return result_dot_product

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
