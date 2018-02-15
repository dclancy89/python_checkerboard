numCols = 8 		# number of colums on the board
numRows = 8			# number of rows on the board
printChar = "*"		# character to mark the square


# print the board
for x in range(numRows):
	row = ""
	if x % 2 == 0: 
		for y in range(numCols):
			if y % 2 == 0:
				row += printChar
			else:
				row += " "
	else:
		for y in range(numCols):
			if y % 2 == 0:
				row += " "
			else:
				row += printChar
	print row
	