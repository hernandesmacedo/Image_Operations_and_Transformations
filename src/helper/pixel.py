def overflow_handler(pixel: list) -> list:
  return list(map(lambda x: max(min(x, 0), 255), pixel))

def normalize(pixel: list) -> list:
  return list(map(lambda x: x / 255, pixel))

def denormalize(pixel: list) -> list:
  return list(map(lambda x: x * 255, pixel))