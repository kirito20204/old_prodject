from superwires import games, color
games.init(screen_width = 640, screen_height = 480, fps = 50)
wall_image=games.load_image('wall.jpg', transparent=False)
pizza_image=games.load_image('pizza.bmp')
pizza=games.Sprite(image=pizza_image, x=430, y=320)
score=games.Text(value=958390480934609189680867013, size=50, color=color.black, x=350, y=30)
message=games.Message(value='игра началась',size=100, color=color.red, x=games.screen.width/2, y=games.screen.height/2, lifetime=250, after_death=games.screen.quit)


games.screen.add(message)
games.screen.add(score)
games.screen.background=wall_image
games.screen.add(pizza)
games.screen.mainloop()