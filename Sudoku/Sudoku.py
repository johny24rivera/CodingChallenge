import os

class sudoku:
  def __init__(self):
    self.board = []
    self.rows = []
    self.cols = []
    self.quads = []
    self.nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    self.complete = False
  
  def fillBoard(self, filename):
    z = range(9)
    lines = ''
    with open(filename) as f:
      lines = f.readlines()

    board = list(map(int, ''.join(lines).split()))
    rows = list(map(lambda x: list(map(int, x.split())), lines))
    cols = list(map(lambda x: list(map( lambda y: rows[y][x], z)) , z))

    self.board = board
    self.rows = rows
    self.cols = cols
    self.board_to_quads()

    # print(self.board, "\n")
    # print(self.rows, "\n")
    # print(self.cols, "\n")
    # print(self.quads, "\n")

  def board_to_quads(self):
    stuff = list(map(lambda x: self.updateQuads(x, self.board[x]), range(81)))
    lol = set(stuff)
    print(len(stuff))
    print(len(lol))

  
  def updateQuads(self, index, val):
    if len(self.quads) == 0:
      self.quads = [[0]*9]*9

    r = index // 9
    c = index % 9 
    
    s = (r // 3 * 3) + (c // 3)
    i = (r % 3 * 3) + (c % 3)

    self.quads[s][i] = val
    return (s , i)




sudo = sudoku()

sudo.fillBoard('test1.txt')