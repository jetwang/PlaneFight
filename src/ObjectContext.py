import inspect

from src.GameObject import GameObject


class ObjectContext:
    def __init__(self, window_screen):
        self.game_objects = []
        self.window_screen = window_screen

    def create_hero_plane(self, x, y, image_names, size):
        return self.create_object(GameObject(x, y, image_names, size))

    def create_object(self, game_object):
        self.game_objects.append(game_object)
        return game_object

    def remove_object(self, game_object):
        self.game_objects.remove(game_object)

    def fire_hit_events(self):
        for game_object1 in self.game_objects:
            for game_object2 in self.game_objects:
                if game_object1 != game_object2:
                    if game_object1.current_img().get_rect().colliderect(game_object2.current_img().get_rect()):
                        game_object1.hits(game_object2)
                        # print(game_object1)

    def render_objects(self):
        for game_object in self.game_objects:
            self.window_screen.blit(game_object.current_img(), (game_object.x, game_object.y))
