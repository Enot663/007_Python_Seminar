# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

values = [1, 26, 15, 'asdfg']
transformed_values = list(map(lambda x: x, values))
print(transformed_values)
if values == transformed_values:
    print('ok')
else:
    print('fail')