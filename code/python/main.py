import numpy as np
import random
import math
import os
import csv
import time
import cProfile
# from memory_profiler import profile
from PIL import Image
from collections import deque

script_dir = os.path.dirname(__file__)
height = 4e-3
width = 4e-3
d = 0.0003
pxW = 752
pxH = 752
pxSize = pxW / width
defPxDiameter = math.ceil(d * pxSize)
data = []
timeBruteOverall = 0
timeDoubleSearch = 0
timeRandomSpotOverall = 0
timeRandomOverall = 0
timeBreadthOverall = 0
timeDoublePointOverall = 0
timeDoubleBreadthOverall = 0

def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper

def bruteForce(arrGS, arr, folder_path, iii, generateImage):
  y = 0
  x = 0
  totalX = np.array([])
  totalY = np.array([])
  dtotalX = []
  dtotalY = []
  rowFlag = False
  rowFlag_2 = False

  if (generateImage):
    arrCopy = arr.copy()

  for y, rows in enumerate(arrGS):
    colFlag = False
    for x, cols in enumerate(rows):
      if (generateImage):
        arrCopy[y][x] = [255, 255, 0]

      if (cols[0] > 10 or cols[1] < 255):

        if (generateImage):
          arrCopy[y][x] = [255, 0, 0]

        # totalX = np.append(totalX, x + 1)
        # totalY = np.append(totalY, y + 1)
        dtotalX.append(x + 1)
        dtotalY.append(y + 1)
        
        rowFlag_2 = True
        colFlag = True
        if (len(dtotalX) == 1):
          rowFlag = True
      else:
        if (colFlag):
          break

    if (rowFlag and not(rowFlag_2)):
      break
    
    rowFlag_2 = False
  # centerX = math.ceil(np.sum(totalX) / len(totalX))
  # centerY = math.ceil(np.sum(totalY) / len(totalY))
  centerX = math.ceil(sum(dtotalX) / len(dtotalX))
  centerY = math.ceil(sum(dtotalY) / len(dtotalY))

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'brute_image_' + str(iii) + '.png'))

  return [centerX, centerY]

def randomSpot(arrGS, arr, folder_path, iii, generateImage):
  pointX = 0
  pointY = 0
  find = False
  rows = len(arrGS)
  cols = len(arrGS[0])
  if (generateImage):
    arrCopy = arr.copy()

  columns = np.array(range(0, len(arrGS)))
  matrix = np.array([{'row': x, 'columns': columns} for x in range(len(columns))])

  for iter in range(rows * cols): 
    if (find):
      break

    randRowIndex = random.randint(0, len(matrix) - 1)
    randRow = matrix[randRowIndex]['row']
    randColumnIndex = random.randint(0, len(matrix[randRowIndex]['columns']) - 1)
    randColumn = matrix[randRowIndex]['columns'][randColumnIndex]

    if (generateImage):
      arrCopy[randRow][randColumn] = [255, 0, 0]

    if (arrGS[randRow][randColumn][0] > 10 or arrGS[randRow][randColumn][1] < 255):
      find = True
      pointX = randColumn
      pointY = randRow

    matrix[randRowIndex]['columns'] = np.delete(matrix[randRowIndex]['columns'], randColumnIndex)
  
  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'spot_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def randPick(arrGS, point, arr, folder_path, iii, generateImage):
  leftTopX = point[0] - defPxDiameter
  leftTopY = point[1] - defPxDiameter
  leftBottomX = point[0] - defPxDiameter;
  leftBottomY = point[1] + defPxDiameter;
  rightTopX = point[0] + defPxDiameter;
  rightTopY = point[1] - defPxDiameter;
  rightBottomX = point[0] + defPxDiameter;
  rightBottomY = point[1] + defPxDiameter;
  
  quadroX = [leftTopX, rightTopX, rightBottomX, leftBottomX]
  quadroY = [leftTopY, rightTopY, rightBottomY, leftBottomY]

  for i in range(4):
    if (quadroX[i] < 0):
      quadroX[i] = 0
    else :
      if (quadroX[i] >= pxW):
        quadroX[i] = pxW - 1
    
    if (quadroY[i] < 0):
      quadroY[i] = 0
    else :
      if (quadroY[i] >= pxH):
        quadroY[i] = pxH - 1

  y = 0
  x = 0
  totalX = np.array([])
  totalY = np.array([])
  dtotalX = []
  dtotalY = []
  rowFlag = False
  rowFlag_2 = False
  if (generateImage):
    arrCopy = arr.copy()

  for y in range(quadroY[0], quadroY[2]):
    colFlag = False
    for x in range(quadroX[0], quadroX[2]):
      if (generateImage):
        arrCopy[y][x] = [255, 255, 0]

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0]

        # totalX = np.append(totalX, x + 1)
        # totalY = np.append(totalY, y + 1)
        dtotalX.append(x + 1)
        dtotalY.append(y + 1)

        colFlag = True
        rowFlag_2 = True

        if (len(dtotalX) == 1):
          rowFlag = True
      else:
        if (colFlag):
          break

    if (rowFlag and not(rowFlag_2)):
      break
    
    rowFlag_2 = False

  # centerX = math.ceil(np.sum(totalX) / len(totalX))
  # centerY = math.ceil(np.sum(totalY) / len(totalY))
  centerX = math.ceil(sum(dtotalX) / len(dtotalX))
  centerY = math.ceil(sum(dtotalY) / len(dtotalY))

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'random_image_' + str(iii) + '.png'))

  return [centerX, centerY]

def breadthSearch(arrGS, point, arr, folder_path, iii, generateImage):
  if (generateImage):
    arrCopy = arr.copy()

  totalX = np.array([])
  totalY = np.array([])
  dtotalX = []
  dtotalY = []
  point = tuple(point)
  frontier = deque()
  frontier.append(point)
  reached = set()
  reached.add(point)

  while not len(frontier) == 0:
    current = frontier.popleft()
    neighboors = [
      [current[0] + 1, current[1]],
      [current[0] - 1, current[1]],
      [current[0], current[1] + 1],
      [current[0], current[1] - 1],
    ]

    for next in neighboors:
      if (next[0] < 0):
        next[0] = 0
      if (next[1] < 0):
        next[1] = 0
      if (next[0] >= pxW):
        next[0] = pxW - 1
      if (next[1] >= pxH):
        next[1] = pxH - 1
      next = tuple(next)
    
      if (next not in reached):
        if (not(arrGS[next[1]][next[0]][0] > 10 or arrGS[next[1]][next[0]][1] < 255)):
          continue
        
        if (generateImage):
          arrCopy[next[1], next[0]] = [255, 0, 0]

        frontier.append(next)
        reached.add(next)
        # totalX = np.append(totalX, next[0] + 1)
        # totalY = np.append(totalY, next[1] + 1)
        dtotalX.append(next[0] + 1)
        dtotalY.append(next[1] + 1)

  # centerX = math.ceil(np.sum(totalX) / len(totalX))
  # centerY = math.ceil(np.sum(totalY) / len(totalY))
  centerX = math.ceil(sum(dtotalX) / len(dtotalX))
  centerY = math.ceil(sum(dtotalY) / len(dtotalY))

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'breadth_image_' + str(iii) + '.png'))

  return [centerX, centerY]

def doubleSearch(arrGS, arr, folder_path, iii, generateImage):
  y = 0
  x = 0
  pointX = 0
  pointY = 0
  flag = False

  if (generateImage):
    arrCopy = arr.copy()

  for y in range(math.floor(len(arrGS) / 2)):
    y = y * 2
    for x in range(math.floor(len(arrGS[y]) / 2)):
      x = x * 2

      if (generateImage):
        arrCopy[y][x] = [255, 255, 0]

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

        if (generateImage):
          arrCopy[y][x] = [255, 0, 0]

        pointX = x;
        pointY = y;
        flag = True
        break
    
    if (flag):
      break
        
  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'double_image_' + str(iii) + '.png'))

  return [pointX, pointY]

@profile
def imageProcessing():
  for iii in range(1, 15):
    rel_path = ('../images/circle_' + str(iii) + '.png')
    abs_path = os.path.join(script_dir, rel_path)
    folder_rel_path = ('./images/image_' + str(iii))
    folder_path = os.path.join(script_dir, folder_rel_path)
    os.makedirs(os.path.join(script_dir, folder_path), exist_ok=True)

    arr = np.asarray(Image.open(abs_path))
    arrGS = np.asarray(Image.open(abs_path).convert('LA'))

    generateImage = False

# =============================================================

    start_1 = time.time()
    bruteCenter = bruteForce(arrGS, arr, folder_path, iii, generateImage)
    end_1 = time.time()

    global timeBruteOverall
    timeBruteOverall += end_1 - start_1
    timeBruteString = "%.4f" %(end_1 - start_1) + ' s',

# =============================================================

    start_2 = time.time()
    randPoint = randomSpot(arrGS, arr, folder_path, iii, generateImage)
    end_2 = time.time()

    global timeRandomSpotOverall
    timeRandomSpotOverall += end_2 - start_2
    timeSpotString = "%.4f" %(end_2 - start_2) + ' s',

# =============================================================

    start_3 = time.time()
    randCenter = randPick(arrGS, randPoint, arr, folder_path, iii, generateImage)
    end_3 = time.time()

    global timeRandomOverall
    timeRandomOverall += end_3 - start_3
    timeRandString = "%.4f" %(end_3 - start_3) + ' s',

# =============================================================

    start_4 = time.time()
    breadthCenter = breadthSearch(arrGS, randPoint, arr, folder_path, iii, generateImage)
    end_4 = time.time()

    global timeBreadthOverall
    timeBreadthOverall += end_4 - start_4
    timeSBreadthtring = "%.4f" %(end_4 - start_4) + ' s',

# =============================================================

    start_5 = time.time()
    doublePoint = doubleSearch(arrGS, arr, folder_path, iii, generateImage)
    end_5 = time.time()

    global timeDoublePointOverall
    timeDoublePointOverall += end_5 - start_5
    timeDoublePointString = "%.4f" %(end_5 - start_5) + ' s',

# =============================================================

    start_6 = time.time()
    doubleBreadthCenter = breadthSearch(arrGS, doublePoint, arr, folder_path, iii, generateImage)
    end_6 = time.time()

    global timeDoubleBreadthOverall
    timeDoubleBreadthOverall += end_6 - start_6
    timeDoubleBreadthString = "%.4f" %(end_6 - start_6) + ' s',

# =============================================================

    print(iii,
    "  |  brute ", bruteCenter, timeBruteString,
    "  |  double brdth ", doubleBreadthCenter, timeDoubleBreadthString, 
    "  |  rand " , randCenter, timeRandString, 
    "  |  breadth " , breadthCenter, timeSBreadthtring, 
    "  |  rand spot ", timeSpotString, 
    "  |  double spot ", timeDoublePointString)
    
    data.append((
      str(bruteCenter[0]),
      str(bruteCenter[1]),
      ''.join(timeBruteString),
      str(randCenter[0]),
      str(randCenter[1]),
      ''.join(timeRandString),
      str(breadthCenter[0]),
      str(breadthCenter[1]),
      ''.join(timeSBreadthtring),
      str(doubleBreadthCenter[0]),
      str(doubleBreadthCenter[1]),
      ''.join(timeDoubleBreadthString),
      ''.join(timeSpotString),
      ''.join(timeDoublePointString),
    ))

imageProcessing()

timeBruteOverall = ("%.4f" % (timeBruteOverall)) + ' s'
timeRandomOverall = ("%.4f" % (timeRandomOverall + timeRandomSpotOverall)) + ' s'
timeBreadthOverall = ("%.4f" % (timeBreadthOverall + timeRandomSpotOverall)) + ' s'
timeRandomSpotOverall = ("%.4f" % (timeRandomSpotOverall)) + ' s'
timeDoubleBreadthOverall = ("%.4f" % (timeDoubleBreadthOverall + timeDoublePointOverall)) + ' s'
timeDoublePointOverall = ("%.4f" % (timeDoublePointOverall)) + ' s'

times = ["Brute:", timeBruteOverall, "Random:", timeRandomOverall, "Breadth:", timeBreadthOverall, "Double breadth:", timeDoubleBreadthOverall, "Random Spot:", timeRandomSpotOverall, "Double spot:", timeDoublePointOverall]
print(times)

data.insert(0, ('bruteX', 'bruteY', 'time', 'randX', 'randY', 'time', 'breadthX', 'breadthY', 'time', 'dBrdthX', 'dBrdthY', 'time', 'spot time', 'double time')) 
data.insert(0, ('', '', timeBruteOverall, '', '', timeRandomOverall, '', '', timeBreadthOverall, '', '', timeDoubleBreadthOverall, timeRandomSpotOverall, timeDoublePointOverall))

with open('compare_py.csv', "w", newline="") as file:
  writer = csv.writer(file)
  for row in data:
    line = ';'.join(row)
    file.write(line + '\n')
  file.close()