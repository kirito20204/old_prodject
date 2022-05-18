from superwires import games, color
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)
class Pan(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
    def check_collide(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()
class Pizza(games.Sprite):
    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)
def main():
    wall_image = games.load_image('wall.jpg', transparent=False)
    # pizza_image = games.load_image('pizza.bmp')
    pan_image = games.load_image('pan.bmp')
    the_pan = Pan(image=pan_image,
                  x=games.mouse.x,
                  y=games.mouse.y)
    games.screen.background = wall_image
    pizza_image=games.load_image('pizza.bmp')
    pizza=Pizza(image=pizza_image, x=random.randrange(games.screen.width), y=random.randrange(games.screen.height))
    games.screen.add(pizza)
    games.screen.add(the_pan)
    games.mouse.is_visidle = False
    games.screen.event_grab = True
    games.screen.mainloop()
main()