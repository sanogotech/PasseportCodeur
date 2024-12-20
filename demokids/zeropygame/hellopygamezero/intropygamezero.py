import pgzrun

slimearm = Actor('alien')
slimearm.topright = 0, 10

WIDTH = 712
HEIGHT = 508

def draw():

    #Vert citron (0, 255, 0)
    #screen.fill((240, 6, 253))
    screen.fill((123,104,238))
    slimearm.draw()

def update():
    slimearm.left += 2
    if slimearm.left > WIDTH:
        slimearm.right = 0

def on_mouse_down(pos):
    if slimearm.collidepoint(pos):
        set_alien_hurt()
    else:
        print("you missed me!")

def set_alien_hurt():
    print("Eek!")
    sounds.eep.play()
    slimearm.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    slimearm.image = 'alien'



pgzrun.go()

