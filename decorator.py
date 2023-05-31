class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    # todo
    return "circle of radius " + str(self.radius)

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    # todo
    return "square with side " + str(self.side)


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    # todo
    # note that a Square doesn't have resize()
    rs = getattr(self.shape, "resize", None)
    if rs:
      rs(factor)
  
  def __str__(self):
    return "A " + str(self.shape)+ " has the color " + self.color

circle = ColoredShape(Circle(5), 'red')
print(
  'A circle of radius 5 has the color red',
  str(circle)
)
circle.resize(2)
print(
    'A circle of radius 10 has the color red',
    str(circle)
)