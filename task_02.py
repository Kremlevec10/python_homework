def print_operation_table(operation, num_rows=6, num_columns=6):
    length = num_rows if num_rows > num_columns else num_columns
    list_1 = range(1, num_columns + 1)
    list_2 = range(1, num_rows + 1)
    for el in list_2:
        any_list = (el for i in range(length))
        print(f'{list(map(operation, list_1, any_list))}')


print_operation_table(lambda x, y: x * y, 5, 3)
