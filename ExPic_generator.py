#! /usr/bin/env python3

import sys
from PIL import Image

class Generator():
    """
    """
    def __init__(self, image):
        """
        """
        self.image = Image.open(image)
        self.image_width = self.image.size[0]
        self.image_height = self.image.size[1]
        self.image_pix = self.image.load()

    def rgb2hex(self, rgb):
        """
        """
        hex_value = '#%02x%02x%02x' % rgb
        return hex_value

    def draw(self):
        """
        """
        pass



if __name__ == "__main__":
    image = sys.argv[1]

    GEN = Generator(image)
    GEN.draw()