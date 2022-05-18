from superwires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)
sound=games.load_sound('missile.wav')
games.music.load('theme.mid')
choice=None
while choice!='0':
    print(  """
    Звук и музыка

    0 - Выход
    1 - Воспроизвести звук ракетного залпа
    2 - Циклизовать звук ракетного залпа
    3 - Стоп звук ракетного залпа
    4 - Воспроизвести музыкальную тему
    5 - Циклизовать музыкальную тему
    6 - Стоп музыкальную тему""")
    choice=input('Введите')
    print()
    if choice=="0":
        print('Пока')
    elif choice=="1":
        sound.play()
    elif choice=="2":
        loop=int(input('Сколько раз возпроизводить звук?'))
        sound.play(loop)
    elif choice=="3":
        sound.stop()
    elif choice=="4":
        games.music.play()
    elif choice=="5":
        loop=int(input('Сколько раз возпроизводить звук?'))
        games.music.play(loop)
    elif choice=='6':
        games.music.stop()
    else:
        print('Вы ошиблись')
input()