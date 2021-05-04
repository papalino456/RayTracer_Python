class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for j in range(width)]for i in range(height)]
    
    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def writePPM(self,imgFile):

        def to_byte(c):
            return round(max(min(c*255, 255),0))

        imgFile.write("P3 {} {}\n255\n".format(self.width,self.height))
        for row in self.pixels:
            for col in row:
                imgFile.write("{} {} {} ".format(to_byte(col.x),to_byte(col.y),to_byte(col.z)))
                imgFile.write("\n")
