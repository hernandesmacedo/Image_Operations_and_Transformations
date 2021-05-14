def op(matrix:list, mov_x: int, mov_y: int) -> list:
  len_x = len(matrix[0])
  len_y = len(matrix)
  new_matrix = __empty_matrix(len_x, len_y)

  for y in range(len_y):
    for x in range(len_x):
      new_x, new_y = __translate((x, y), (mov_x, mov_y))
      if new_x not in range(len_x) or new_y not in range(len_y):
        continue
      new_matrix[new_y][new_x] = matrix[y][x]
  
  return new_matrix

def __empty_matrix(len_x: int, len_y: int) -> list:
  new_matrix = []

  for y in range(len_y):
    new_line = []
    for x in range(len_x):
      new_line.append([0, 0, 0])
    new_matrix.append(new_line)
  
  return new_matrix

def __translate(coords: tuple, move: tuple) -> tuple:
  return coords[0] + move[0], coords[1] + move[1]