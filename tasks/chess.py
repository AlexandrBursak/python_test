def get_new_table():
	return list(
		(		#  x0  x1  x2  x3  x4  x5  x6  x7
			list(('i','i','i','i','i','i','i','i',)), # y0
			list(('0','0','0','0','0','0','0','0',)), # y1
			list(('0','0','0','0','0','0','0','0',)), # y2
			list(('0','0','0','0','0','0','0','0',)), # y3
			list(('0','0','0','0','0','0','0','0',)), # y4
			list(('0','0','0','0','0','0','0','0',)), # y5
			list(('0','0','0','0','0','0','0','0',)), # y6
			list(('0','0','0','0','0','0','0','0',)), # y7
		)
	)


def validate(table, pos_x, pos_y):
	if pos_x != 0:
		for line_x in list(range(0, pos_x)):
			point = find_in_row(table, line_x)

			diag_up = pos_y - (pos_x - line_x)
			diag_down = pos_y + (pos_x - line_x)

			if point in [pos_y, diag_up, diag_down]:
				return False

	return True


def set_queen(table, pos_x, pos_y):
	for row_y in list(range(0, 8)):
		# set quen to new coordinate and refresh other position in col
		table[row_y][pos_x] = 'i' if row_y == pos_y else '0'

	return table


def find_in_row(table, pos_x):
	for row_y in list(range(0, 8)):
		if table[row_y][pos_x] == 'i':
			return row_y


def print_table(table):
	for line_y in table:
		line='|'	
		print('-----------------')
		for col_x in line_y:
			line = line + col_x + '|'
		print(line)
	print('-----------------')


def need_to_move_queen(table, next_x, next_y):
	next_y = 0 if next_y + 1 > 7 else next_y + 1
	table = set_queen(table, next_x, next_y)

	if next_y == 0:
		# moves prev col queen
		next_x = next_x - 1
		next_y = find_in_row(table, next_x)
		table, next_x, next_y = need_to_move_queen(table, next_x, next_y)

	return table, next_x, next_y


def validation_of_position(table, next_x, next_y, is_validate, stopper):

	while is_validate == False:
		if table[next_y][next_x] == 'i' and validate(table, next_x, next_y):
			next_x = next_x + 1
			if next_x == 8:
				is_validate = True
				next_x = 0
			next_y = find_in_row(table, next_x)
		else:
			table, next_x, next_y = need_to_move_queen(table, next_x, next_y)

		stopper = stopper + 1

	print('moves: ', stopper)
	return table, next_x, next_y, is_validate, stopper


def init_data(table, is_validate = False, next_x = 0):
	stopper = 0
	next_y = find_in_row(table, next_x)
	return is_validate, stopper, next_x, next_y


table = get_new_table()
underlimit_loop = True
is_validate, stopper, next_x, next_y = init_data(table, is_validate = False, next_x = 0)
yes_choices = ['yes', 'y']
no_choices = ['no', 'n']

count = 0
print('Lets find combination (yes/no)? yes')
while underlimit_loop:
	count = count + 1
	user_input = input() or 'y'
	if user_input.lower() in yes_choices:
		table, next_x, next_y, is_validate, stopper = validation_of_position(table, next_x, next_y, is_validate, stopper)
		print('Combination #', count)
		print_table(table)

		is_validate, stopper, next_x, next_y = init_data(table, is_validate = False, next_x = 7)
		table, next_x, next_y = need_to_move_queen(table, next_x, next_y)
		print('and one more combination (yes/no)? yes')

	elif user_input.lower() in no_choices:
		underlimit_loop = False




