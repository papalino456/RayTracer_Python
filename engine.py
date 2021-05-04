from image import Image
from ray import Ray
from point import Point
from color import Color

class RenderEngine:

    MAX_DEPTH = 10
    MIN_DISPLACE = 0.001

    def render(self, scene):
        width = scene.width
        height = scene.height
        ratio = float(width)/height

        x0 = -1.0
        x1 = 1.0
        xStep = (x1-x0) / (width-1)

        y0 = -1.0 / ratio
        y1 = 1.0 / ratio
        yStep = (y1-y0) / (height-1)

        camera = scene.camera
        pixels=Image(width,height)

        for j in range(height):
            y = y0 + j * yStep
            for i in range(width):
                x = x0 + i * xStep
                ray = Ray(camera,Point(x,y) - camera)
                pixels.set_pixel(i, j, self.rayTrace(ray,scene))

        return pixels

    def rayTrace(self,ray,scene,depth=0):
        color = Color(0,0,0)

        distHit, objHit = self.findNearest(ray,scene)
        if objHit is None:
            return color
        hitPos = ray.origin + ray.direction * distHit
        hitNorm = objHit.normal(hitPos)
        color += self.colorAt(objHit,hitPos,hitNorm,scene)
        if depth < self.MAX_DEPTH:
            newRayPos = hitPos + hitNorm * self.MIN_DISPLACE
            newRayDir = ray.direction - 2 * ray.direction.dotProduct(hitNorm) * hitNorm
            newRay = Ray(newRayPos,newRayDir)
            color += (self.rayTrace(newRay,scene,depth+1) * objHit.material.reflection)
        return color

    def findNearest(self,ray,scene):
        distMin = None
        objHit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (objHit is None or dist < distMin):
                distMin = dist
                objHit = obj
        
        return (distMin, objHit)
    
    def colorAt(self,objHit,hitPos,normal, scene):
        material = objHit.material
        objColor = material.colorAt(hitPos)
        toCam = scene.camera-hitPos
        specular_k = 50
        color = material.ambient * Color.fromHex("#000000")

        for light in scene.lights:

            toLight = Ray(hitPos, light.position - hitPos)

            color += objColor * material.diffuse * max(normal.dotProduct(toLight.direction),0)

            halfVector = (toLight.direction + toCam).normalize()

            color += light.color * material.specular * max(normal.dotProduct(halfVector),0) ** specular_k

        return color

