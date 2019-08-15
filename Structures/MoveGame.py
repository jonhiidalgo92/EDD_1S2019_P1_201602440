
import random
import curses
import SnakeStructure
import ScoreQueue
from curses import textpad

def create_food(snake, box):
	food = None
	while food is None:
		food = [random.randint(box[0][0]+1, box[1][0]-1),random.randint(box[0][1]+1, box[1][1]-1)]
		if food in snake:
			food = None
	return food


def Funtion(stdscr):
	# initial settings
	curses.curs_set(0)
	stdscr.nodelay(1)
	stdscr.timeout(100)
	snak = SnakeStructure.Snake()
	#scor = ScoreQueue.ScoreQueue()
	# create a game box
	sh, sw = stdscr.getmaxyx()
	box = [[3,3], [sh-3, sw-3]]  # [[ul_y, ul_x], [dr_y, dr_x]]
	textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

	# create snake and set initial direction
	snake = [[sh//2, sw//2+1], [sh//2, sw//2], [sh//2, sw//2-1]]
	snak = SnakeStructure.Snake()
	scor = ScoreQueue.ScoreQueue()

	direction = curses.KEY_RIGHT

	# draw snake
	for y,x in snake:
		stdscr.addstr(y, x, '#')


# food diferent
	cosa =''
	type1 = random.randint(0,99)
	if type1 <= 25:
		cosa= '*'
	else:
		cosa = '+'
	# create food
	food = create_food(snake, box)
	stdscr.addstr(food[0], food[1], cosa)

	# print score
	score = 0
	score_text = "Score: {}".format(score)
	stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)

	while 1:
		# non-blocking input
		key = stdscr.getch()

		# set direction if user pressed any arrow key
		if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
			direction = key

		# find next position of snake head
		head = snake[0]
		if direction == curses.KEY_RIGHT:
			new_head = [head[0], head[1]+1]

		elif direction == curses.KEY_LEFT:
			new_head = [head[0], head[1]-1]

		elif direction == curses.KEY_DOWN:
			new_head = [head[0]+1, head[1]]

		elif direction == curses.KEY_UP:
			new_head = [head[0]-1, head[1]]


		# insert and print new head
		stdscr.addstr(new_head[0], new_head[1], '#')
		snake.insert(0, new_head)


		# if sanke head is on food
		if snake[0] == food:
			# update score

			score += 1
			score_text = "Score: {}".format(score)
			stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)
			snak.Insert(food[0],food[1])
			scor.Insert(food[0],food[1])
			# create new food
			food = create_food(snake, box)
			stdscr.addstr(food[0], food[1], '*')


			# increase speed of game
			stdscr.timeout(100 - (len(snake)//3)%50)
		else:
			# shift snake's tail
			stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
			snake.pop()

		# conditions for game over
		if (snake[0][0] in [box[0][0], box[1][0]] or
			snake[0][1] in [box[0][1], box[1][1]] or
			snake[0] in snake[1:]):
			msg = "Game Over!"
			snak.GenerateSnakeOter(snak)
			scor.GenerateGraphic2(scor)
			stdscr.addstr(sh//2, sw//2-len(msg)//2, msg)
			stdscr.nodelay(0)
			stdscr.getch()

			break

curses.wrapper(Funtion)
