import os

class sudoku:
  def __init__(self):
    self.rows = []
    self.cols = []
    self.quads = []
    self.nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
  
  def fillBoard(self, filename):
    lines = ''
    with open(filename) as f:
      lines = f.readlines()
      
    stuff = list(map(lambda x: list(map(int, x.split())), lines))
    
    print(stuff)


sudo = sudoku()

sudo.fillBoard('test1.txt')