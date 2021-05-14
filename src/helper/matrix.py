from .img import sum_channels

def print_matrix(matrix: list) -> None:
  matrix = sum_channels(matrix)
  len_x, len_y = len(matrix[0]), len(matrix)
  len_big = len(str(get_biggest(matrix)))

  print('┌' + (('─' * len_big) + '┬') * (len_x - 1) + ('─' * len_big) + '┐')

  for y in range(len_y):
    for x in range(len_x):
      print('│' + str(matrix[y][x]).rjust(len_big, ' '), end='')
    print('│')

    if y == len_y - 1:
      break

    print('├' + (('─' * len_big) + '┼') * (len_x - 1) + ('─' * len_big) + '┤')

  print('└' + (('─' * len_big) + '┴') * (len_x - 1) + ('─' * len_big) + '┘')

def get_biggest(matrix: list) -> int:
  return max(list(map(lambda x: max(x), matrix)))
