from superwires import games, color
games.init(screen_width = 640, screen_height = 480, fps = 50)
class Pan(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
def mein():
    wall_image = games.load_image('wall.jpg', transparent=False)
    #pizza_image = games.load_image('pizza.bmp')
    pan_image = games.load_image('pan.bmp')
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)

    games.screen.background=wall_image
    games.screen.add(the_pan)
    games.mouse.is_visidle = False
    games.screen.event_grab = True
    games.screen.mainloop()
mein()