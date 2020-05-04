global matrixSize

def displayWordsearch(puzzle):
	print("======================")
	for row in range(0,matrixSize):
		line=""
		for col in range(0,matrixSize):
			line = line + puzzle[row][col] + " "
		print(line)
	print("======================")

def findSameFirstWordInRow(row, word, puzzle):
	col = 0
	while (puzzle[row][col] != word[0]) and col != (matrixSize-1):
		col = col + 1
	if(puzzle[row][col] == word[0]):
		return col
	else:
		return -1

def checkVerticalUtoD(raw, col, word, puzzle):
	idx = []
	i = row
	if (row != (matrixSize-1)) and ((row + len(word) - 1) < matrixSize):
		w = 0
		i = row
		j = col
		match = True
		while(match and i < (row + len(word))):
			if(word[w] == puzzle[i][j]):
				idx.append([i,j])
				w = w + 1
				i = i + 1
			else:
				match = False
		if(match):
			for k in range (len(idx)):
				temp = puzzle[idx[k][0]][idx[k][1]]
				puzzle[idx[k][0]][idx[k][1]] = "[" + temp + "]"

def checkDiagonalLDtoRU(row, col, word, puzzle):
	idx = []
	j = col
	if (row != 1) and (col != (matrixSize-1)) and ((col + len(word) - 1) < matrixSize):
		w = 0
		i = row
		j = col
		match = True
		while(match and i > (row - len(word))):
			if(word[w] == puzzle[i][j]):
				idx.append([i,j])
				w = w + 1
				i = i - 1
				j = j + 1
			else:
				match = False
		if(match):
			for k in range (len(idx)):
				temp = puzzle[idx[k][0]][idx[k][1]]
				puzzle[idx[k][0]][idx[k][1]] = "[" + temp + "]"

def checkHorizontalLToR(row, col, word, puzzle):
	idx = []
	j = col
	if (col != (matrixSize-1)) and ((col + len(word) - 1) < matrixSize):
		w = 0
		i = row
		j = col
		match = True
		while(match and j < (col + len(word))):
			if(word[w] == puzzle[i][j]):
				idx.append([i,j])
				w = w + 1
				j = j + 1
			else:
				match = False
		if(match):
			for k in range (len(idx)):
				temp = puzzle[idx[k][0]][idx[k][1]]
				puzzle[idx[k][0]][idx[k][1]] = "[" + temp + "]"

def checkDiagonalLUtoRD(row, col, word, puzzle):
	idx = []
	j = col
	if (row != (matrixSize-1)) and (col != (matrixSize-1)) and ((col + len(word) - 1) < matrixSize):
		w = 0
		i = row
		j = col
		match = True
		while(match and i < (row + len(word))):
			if(word[w] == puzzle[i][j]):
				idx.append([i,j])
				w = w + 1
				i = i + 1
				j = j + 1
			else:
				match = False
		if(match):
			for k in range (len(idx)):
				temp = puzzle[idx[k][0]][idx[k][1]]
				puzzle[idx[k][0]][idx[k][1]] = "[" + temp + "]"

# main
matrixSize = 5

rawPuzzle = [
'L', 'W', 'M', 'E', 'R', 
'I', 'W', 'C', 'E', 'X', 
'O', 'V', 'G', 'A', 'Q', 
'N', 'I', 'N', 'I', 'T',
'T', 'R', 'A', 'E', 'B'
]

puzzle = []
i = 0
for row in range(0, matrixSize):
	puzzle.append([])
	for idx in range(i, i + matrixSize):
		puzzle[row].append(rawPuzzle[idx])
	i = i + matrixSize
print("Soal:")
displayWordsearch(puzzle)

findWord = ['CAT', 'BEAR', 'TIGER', 'LION']
position = []

print("Jawaban yang diberi tanda [...]")
for w in range (len(findWord)):
	currentWord = findWord[w]
	row = 0
	col = -1
	while (col == -1) and row < matrixSize:
		col = findSameFirstWordInRow(row, currentWord, puzzle)
		if(col == -1):
			row = row + 1
	checkDiagonalLUtoRD(row, col, currentWord, puzzle)
	checkHorizontalLToR(row, col, currentWord, puzzle)
	checkDiagonalLDtoRU(row, col, currentWord, puzzle)
	checkVerticalUtoD(row, col, currentWord, puzzle)
	# checkVerticalDtoU(row, col, currentWord, puzzle)

displayWordsearch(puzzle)