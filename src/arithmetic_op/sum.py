# A técnica utilizada para controle do intervalo RGB foi a do limite superior
def sum_lists(list1: list, list2: list) -> list:
  r = list1[0] + list2[0] if list1[0] + list2[0] < 255 else 255
  g = list1[1] + list2[1] if list1[1] + list2[1] < 255 else 255
  b = list1[2] + list2[2] if list1[2] + list2[2] < 255 else 255
  return [r, g, b]

def sum_imgs(img1: list, img2: list) -> list:
  img1_lines, img2_lines = len(img1), len(img2)
  img1_columns, img2_columns = len(img1[0]), len(img2[0])
  min_line = min( img1_lines, img2_lines )
  min_column = min( img1_columns, img2_columns )

  new_img = []

  for l in range (min_line):
    new_line = []
    for c in range (min_column):
      new_line.append( sum_lists(img1[l][c], img2[l][c]) )
    new_img.append(new_line)

  return new_img