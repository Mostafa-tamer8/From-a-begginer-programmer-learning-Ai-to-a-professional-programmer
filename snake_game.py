#import modules
import random
import curses

#initialize window
screen = curses.initscr()

#hiding cursor
curses.curs_set(0)

#getting window size
snk_height, snk_width = screen.getmaxyx()

#creating a new window
window = curses.newwin(snk_height, snk_width, 0, 0)

#enabling keypad input
window.keypad(1)

#setting up the game
curses.noecho()
curses.cbreak()
window.timeout(100)

#initial position of the snake
snake_x = snk_width // 4
snake_y = snk_height // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

#initial position of the food
food = [snk_height // 2, snk_width // 2]

window.addch(food[0], food[1], curses.ACS_DEGREE)

#set movement to right
key = curses.KEY_RIGHT

#create game loop that loops forecver unti player loses

while True:
    next_key = window.getch()
    # Prevent reversing direction
    if (next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT) or \
       (next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT) or \
       (next_key == curses.KEY_UP and key != curses.KEY_DOWN) or \
       (next_key == curses.KEY_DOWN and key != curses.KEY_UP):
        key = next_key
        key = key if next_key == -1 else next_key

    #calculate new head of the snake
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    #insert new head
    snake.insert(0, new_head)

    #check if snake ate the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, snk_height - 1),
                random.randint(1, snk_width - 1)
            ]
            food = nf if food not in snake else None    
        window.addch(food[0], food[1],  curses.ACS_DEGREE)
    else:
        #remove last segment of snake
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    #check for collision with borders or self
    if (snake[0][0] == 0 or snake[0][0] == snk_height-1 or
        snake[0][1] == 0 or snake[0][1] == snk_width-1 or
        snake[0] in snake[1:]):
        quit() # End the game

#update the position of the snake
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    window.refresh()
