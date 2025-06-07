def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    else:
        triangle = generate_pascals_triangle(numRows - 1)
        last_row = triangle[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
        return triangle

print(generate_pascals_triangle(3))