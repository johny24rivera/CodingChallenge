import os

class sudoku:
  def __init__(self):
    self.board = []
    self.rows = []
    self.cols = []
    self.quads = []
    self.nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    self.complete = False
    self.updated = True
  
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

  def board_to_quads(self):
    for n in range(81):
      self.updateQuads(n, self.board[n])
  

  def updateRows(self, index, val):
    r = index // 9
    c = index % 9
    self.rows[r][c] = val

  def updateCols(self, index, val):
    r = index // 9
    c = index % 9
    self.cols[c][r] = val
  
  def updateQuads(self, index, val):
    if len(self.quads) == 0:
      self.quads = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    r = index // 9
    c = index % 9 
    
    s = (r // 3 * 3) + (c // 3)
    i = (r % 3 * 3) + (c % 3)

    self.quads[s][i] = val
    
  
  def updateBoard(self, index, val):
    self.board[index] = val
    self.updateRows(index, val)
    self.updateCols(index, val)
    self.updateQuads(index, val)

  def checkRows(self):
    for n in self.rows:
      nums = self.nums.symmetric_difference(set(n))
      print(nums)
  
  def checkCols(self):
    for n in self.cols:
      nums = self.nums.symmetric_difference(set(n))
      print(nums)
  
  def checkQuads(self):
    for n in range(9):
      nums = self.nums.symmetric_difference(set(self.quads[n]))
      print(nums)
      if len(nums) == 2:
        for x in nums:
          if x != 0:
            index = self.quads[n].index(0)
            o = index // 3
            r = (n // 3 * 3) + o
            c = (n % 3 * 3) + (index % 3)

            index = r * 9 + c
            self.updateBoard(index, x)
        self.updated = True
        return
  
  def checkBoard(self):
    self.updated = False
    self.checkRows()
    self.checkCols()
    self.checkQuads()


  def solve(self):
    while self.updated:
      print("\n\n\nNew Run:")
      self.checkBoard()





sudo = sudoku()

sudo.fillBoard('test1.txt')
sudo.solve()