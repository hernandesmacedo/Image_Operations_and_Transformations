class Dialog:
  def __init__(self, *lines: str, header: str = None, footer: str = None):
    self.lines = lines
    self.max_len = max(map(lambda x: len(x), lines))
    if header != None:
      self.header = header
      self.max_len = max(self.max_len, len(header))
    if footer != None:
      self.footer = footer
      self.max_len = max(self.max_len, len(footer))
    self.max_len += 2

  def show(self):
    self.print_division('┌', '┐')
    if hasattr(self, 'header'):
      self.print_text(self.header)
      self.print_division('├', '┤')
    for line in self.lines:
      self.print_text(line)
    if hasattr(self, 'footer'):
      self.print_division('├', '┤')
      self.print_text(self.footer)
    self.print_division('└', '┘')

  def print_division(self, begin: str, end: str):
    print(begin + '─' * self.max_len + end)

  def print_text(self, text: str):
    print('│' + text.center(self.max_len, ' ') + '│')

class Input(Dialog):
  def __init__(self, *lines: str, header: str = None, footer: str = None, input_title: str = 'Entrada'):
    super().__init__(*lines, header=header, footer=footer)
    self.input_title = input_title

  def show(self):
    super().show()
    return self.get_input()

  def get_input(self):
    return input(f'{self.input_title}: ')

class Menu(Dialog):
  def __init__(self, *lines: str, header: str = None, footer: str = None):
    super().__init__(*lines, header=header, footer=footer)
    self.index_len = len(str(len(self.lines)))

  def show(self):
    if hasattr(self, 'header'):
      self.print_division('┌', '┐')
      self.print_text(self.header)
      self.print_division('├', '┤', '┬')
    else:
      self.print_division('┌', '┐', '┬')

    for i in range(len(self.lines)):
      self.print_text(self.lines[i], i)
      if i != len(self.lines) - 1:
        self.print_division('├', '┤', '┼')

    if hasattr(self, 'footer'):
      self.print_division('├', '┤', '┴')
      self.print_text(self.footer)
      self.print_division('└', '┘')
    else:
      self.print_division('└', '┘', '┴')

    return self.get_selection()

  def print_division(self, begin: str, end: str, div: str = '─'):
    print(begin + '─' * self.index_len + div + '─' * self.max_len + end)

  def print_text(self, text: str, index: int = None):
    if index is not None:
      print('│' + str(index).rjust(self.index_len, ' ') + '│' + text.center(self.max_len, ' ') + '│')
    else:
      print('│' + text.center(self.max_len + self.index_len + 1, ' ') + '│')

  def get_selection(self):
    try:
      selection = int(input('Seleção: '))
      if selection not in range(len(self.lines)):
        raise Exception
      return selection
    except:
      Dialog('Por favor, tente novamente!', header = 'Seleção inválida').show()
      return self.get_selection()