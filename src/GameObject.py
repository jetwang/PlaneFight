import pygame


class GameObject(object):
    """所有类的基类"""

    def __init__(self, x, y, image_names, size):
        self.x = x
        self.y = y
        self.current_img_index = 0
        if image_names:
            self.images = []
            for image_name in image_names:
                self.images.append(pygame.image.load("./img/" + image_name))
        self.image_names = image_names
        self.size = size

    def hits(self, target):
        return 1;

    def change_modelling(self, index):
        self.current_img_index = index

    def current_img(self):
        return self.images[self.current_img_index]

    def move(self, x=0, y=0):
        self.x += x
        self.y += y
