from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
snake_velocity = 20
start_x = 0
start_y = 0
global score
# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    snake_x = start_x
    snake_y = start_y
    food_x = SIZE*random.randint(0, (CANVAS_WIDTH/20)-1)
    food_y = SIZE*random.randint(0, (CANVAS_WIDTH/20)-1)
    snake = canvas.create_rectangle(snake_x, snake_y, snake_x+SIZE, snake_y+SIZE, "blue")
    food = canvas.create_rectangle(food_x, food_y, food_x+SIZE, food_y+SIZE, 'orange')
    score=0; key=None
    text = canvas.create_text(20, 380, text='score = ', color="blue")
    text1 = canvas.create_text(70, 380, text= str(score), color = "red")
    #oval = canvas.create_oval(left_x, top_y, right_x, bottom_y)
    # TODO: your code here
    while snake_x>=0 and snake_x<=CANVAS_WIDTH and snake_y>=0 and snake_y<=CANVAS_HEIGHT:
        if snake_x == food_x and snake_y == food_y:
            score = score+1
            print(score)
            canvas.change_text(text1, str(score))
            food_x = SIZE*random.randint(0, (CANVAS_WIDTH/20)-1)
            food_y = SIZE*random.randint(0, (CANVAS_WIDTH/20)-1)
            canvas.moveto(food, food_x, food_y)
        #key = canvas.get_new_key_presses()
        okey = None
        nkey = canvas.get_last_key_press()
        if nkey != okey:
            key = nkey
        print(key)
        if key == 'ArrowLeft':
            snake_x -= snake_velocity
            canvas.moveto(snake, snake_x, snake_y)
        if key == 'ArrowRight':
            snake_x += snake_velocity
            canvas.moveto(snake, snake_x, snake_y)
        if key == 'ArrowUp':
            snake_y -= snake_velocity
            canvas.moveto(snake, snake_x, snake_y)
        if key == 'ArrowDown':
            snake_y += snake_velocity
            canvas.moveto(snake, snake_x, snake_y)
        snake_x = canvas.get_left_x(snake)
        snake_y = canvas.get_top_y(snake)
        time.sleep(DELAY)
    print("game over")
    print("Score = ", score)
if __name__ == '__main__':
    main()