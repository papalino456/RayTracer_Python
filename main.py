from image import Image
from engine import RenderEngine
from Scenes import twoSpheres
from scene import Scene

def main():
    #CHANGE SCENE HERE
    sc = twoSpheres

    scene = Scene(sc.CAMERA,sc.OBJECTS,sc.LIGHTS,sc.WIDTH,sc.HEIGHT)
    engine = RenderEngine()
    img = engine.render(scene)
    with open("test.ppm", "w") as imgFile:
        img.writePPM(imgFile)

if __name__ == "__main__":
    main()