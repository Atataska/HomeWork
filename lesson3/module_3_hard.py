def calculate_structure_sum(*args):
  y = 0
  for i in args:
    if isinstance(i, list):
      for e in i:
        y += calculate_structure_sum(e)
    elif isinstance(i, tuple):
      for e in i:
        y += calculate_structure_sum(e)
    elif isinstance(i, set):
      for e in i:
        y += calculate_structure_sum(e)
    elif isinstance(i, dict):
      for key, value in i.items():
        y += calculate_structure_sum(key, value)
    elif isinstance(i, str):
      y += len(i)
    elif isinstance(i, int):
      y += i
  return y

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)