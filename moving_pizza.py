from superwires import games, color
games.init(screen_width = 640, screen_height = 480, fps = 50)
class Pizza(games.Sprite):
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
def mein():
    wall_image=games.load_image('wall.jpg', transparent=False)
    pizza_image=games.load_image('pizza.bmp')
    #pizza=games.Sprite(image=pizza_image, x=430, y=320)
    the_pizza=Pizza(image=pizza_image,
                        x=games.screen.width/2,
                        y=games.screen.height/2,
                        dx=1,
                         dy=1)

    games.screen.background=wall_image
    games.screen.add(the_pizza)
    games.screen.mainloop()
mein()