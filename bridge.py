# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
from abc import ABC

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
        
# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
class Shape(ABC):
    def __str__(self):
        return "Drawing " + self.name + " as " + str(self.renderer)
        
class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.name = "Triangle"

        
class RasterRenderer(Renderer):
    def __init__(self):
        super().__init__()
        
    def __str__(self):
        return "pixels"
        

class Square(Shape):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.name = "Square"


class VectorRenderer(Renderer):
    def __init__(self):
        super().__init__()
        
    def __str__(self):
        return "lines"

rrd = RasterRenderer()
tr = Triangle(renderer=rrd)
print(tr)
vrd = VectorRenderer()
sq = Square(renderer=vrd)
print(sq)