#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#site do robô ☝☝☝    


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def volta():
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def wall_on_left():
    turn_left()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
        if wall_on_right():
            turn_left()
    else:
        turn_right()
            
        
        