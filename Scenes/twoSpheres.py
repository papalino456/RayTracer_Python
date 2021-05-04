from vector import Vector
from image import Image
from color import Color
from point import Point
from sphere import Sphere
from light import Light
from material import Material, CheckerMat

WIDTH = 3840
HEIGHT = 2160
CAMERA = Vector(0,-0.35,-1)

OBJECTS = [Sphere(Point(0, 10000.5, 1), 10000.0, CheckerMat(ambient=0.2,reflection=0.5)),
           Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.fromHex("#0000FF"))),
           Sphere(Point(-1, -0.1, 2.25), 0.6, Material(Color.fromHex("#ff6e6e")))]

LIGHTS = [Light(Point(1.5,-0.5,-10), Color.fromHex("#FFFFFF")),
          Light(Point(-5,-10.5,0), Color.fromHex("#E6E6E6"))]