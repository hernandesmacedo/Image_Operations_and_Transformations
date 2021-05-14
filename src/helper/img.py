import numpy
from copy import deepcopy
from cv2 import imwrite, imread

def get_pixeis(img: numpy.ndarray) -> list:
  largura, altura = len(img[0]), len(img)
  pixeis = []
  for y in range (altura):
    new_line = []
    for x in range(largura):
      new_line.append(img[y][x].tolist())
    pixeis.append(new_line)

  return pixeis

def sum_channels(matrix: list) -> list:
  len_x, len_y = len(matrix[0]), len(matrix)
  new_matrix = deepcopy(matrix)

  for y in range(len_y):
    for x in range(len_x):
      new_matrix[y][x] = sum(new_matrix[y][x])

  return new_matrix

def import_image(file_path: str):
  return imread(file_path)

def export_image(matrix: list, name: str) -> bool:
  filename = './export/' + name + '.png'
  try:
    imwrite(filename, numpy.array(matrix))
  except:
    return False
  return True