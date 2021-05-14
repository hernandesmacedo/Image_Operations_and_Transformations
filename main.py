#==========[Local Libraries]==========
#-----[Functionality]-----
from src.geometric_op import translation
from src.intensity_op import negative
from src.helper.img import get_pixeis
from src.helper.matrix import print_matrix
from src.arithmetic_op import sum, subtraction

#-----[Terminal Interface]-----
import src.cli.menu as menu

#==========[Main Function]==========
def main():
  img_original = menu.load()
  img_matrix = get_pixeis(img_original)
  img_second = None

  while True:
    selection = menu.home()

    if selection == 0:
      break

    elif selection == 1:
      img_matrix = get_pixeis(img_original)

    elif selection == 2:
      img_matrix = translation.op(img_matrix, 40, 60)

    elif selection == 3:
      img_matrix = negative.op(img_matrix)

    elif selection in [4, 5]:
      if img_second is None:
        img_second = get_pixeis(menu.load())

      if selection == 4:
        img_matrix = sum.sum_imgs(img_matrix, img_second)
        
      elif selection == 5:
        img_matrix = subtraction.sub_imgs(img_matrix, img_second)

    elif selection == 6:
      print_matrix(img_matrix)

    elif selection == 7:
      menu.export(img_matrix)

#==========[Script Initializer]==========
if __name__ == "__main__":
  main()