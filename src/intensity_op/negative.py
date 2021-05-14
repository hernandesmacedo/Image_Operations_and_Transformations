from ..helper import pixel as p

def op(matrix: list) -> list:
  len_x, len_y = len(matrix[0]), len(matrix)

  for y in range(len_y):
    for x in range(len_x):
      matrix[y][x] = __negative(matrix[y][x])

  return matrix

def __negative(pixel: list) -> list:
  return p.denormalize(map(lambda x: abs(x - 1), p.normalize(pixel)))