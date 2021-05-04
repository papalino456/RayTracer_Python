import math

class Sphere:
    def __init__(self,center,radius,material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self,ray):
        sphereToRay = ray.origin - self.center
        a = 1
        b = 2 * ray.direction.dotProduct(sphereToRay)
        c = sphereToRay.dotProduct(sphereToRay) - self.radius * self.radius
        disc = b*b - 4*a*c

        if disc >= 0:
            dist = (-b - math.sqrt(disc))/2
            if dist > 0:
                return dist
    
        return None

    def normal(self,surfacePoint):
        return (surfacePoint - self.center).normalize()