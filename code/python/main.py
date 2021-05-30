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
m_height = 4e-3
m_width = 4e-3
d = 0.0003
pxW = 752
pxH = 752
pxSize = pxW / m_width
defPxDiameter = math.ceil(d * pxSize)
data = []

timeBruteOverall = 0
timeDoubleSearch = 0
timeRandomOverall = 0
timeBreadthOverall = 0
timeRoundBreadthOverall = 0
timeDoubleBreadthOverall = 0
timeBreadthBreadthOverall = 0
timeRoundDoubleBreadthOverall = 0

timeDoubleSpotOverall = 0
timeRandomSpotOverall = 0
timeRoundSpotOverall = 0
timeRoundDoubleSpotOverall = 0
timeBreadthSpotOverall = 0

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
  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'brute_image_' + str(iii) + '.png'))

  if (len(dtotalX) == 0 or len(dtotalY) == 0):
    return [0, 0]

  centerX = math.ceil(sum(dtotalX) / len(dtotalX))
  centerY = math.ceil(sum(dtotalY) / len(dtotalY))


  return [centerX, centerY]

def randomSpot(arrGS, arr, folder_path, iii, generateImage):
  pointX = -1
  pointY = -1
  find = False
  rows = len(arrGS)
  cols = len(arrGS[0])
  if (generateImage):
    arrCopy = arr.copy()

  columns = np.array(range(0, len(arrGS)))
  matrix = np.array([{'row': x, 'columns': columns} for x in range(len(columns))])

  for iter in range(math.ceil(rows * cols / 4)): 
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

    np.delete(matrix[randRowIndex]['columns'], randColumnIndex)

    if (len(matrix[randRowIndex]['columns']) == 0):
      np.delete(matrix, randRowIndex)

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'spot_rand_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def randPick(arrGS, point, arr, folder_path, iii, generateImage):
  if (generateImage):
    arrCopy = arr.copy()

  if (point[0] == -1 or point[1] == -1):
    if (generateImage):
      img = Image.fromarray(arrCopy)
      img.save(os.path.join(folder_path, 'random_image_' + str(iii) + '.png'))
    return [0, 0]

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
    img.save(os.path.join(folder_path, 'c_rand_image_' + str(iii) + '.png'))

  return [centerX, centerY]

def breadthSearch(arrGS, point, arr, folder_path, iii, generateImage, algoType):
  if (generateImage):
    arrCopy = arr.copy()
  if (point[0] == -1 or point[1] == -1):
    if (generateImage):
      fileName = 'c_breadth_' + algoType + 'image_' + str(iii) + '.png'

      img = Image.fromarray(arrCopy)
      img.save(os.path.join(folder_path, fileName))
    return [0, 0]

  if (generateImage):
    arrCopy = arr.copy()

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
        dtotalX.append(next[0] + 1)
        dtotalY.append(next[1] + 1)

  if (generateImage):
    fileName = 'c_breadth_' + algoType + 'image_' + str(iii) + '.png'

    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, fileName))

  if (len(dtotalX) == 0 or len(dtotalY) == 0):
    return [0, 0]

  centerX = math.ceil(sum(dtotalX) / len(dtotalX))
  centerY = math.ceil(sum(dtotalY) / len(dtotalY))

  return [centerX, centerY]

def doubleSearch(arrGS, arr, folder_path, iii, generateImage):
  y = 0
  x = 0
  pointX = -1
  pointY = -1
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

  if (pointX == -1 or pointY == -1):
    rows = [0, len(arrGS) - 1]
    cols = [0, len(arrGS[0]) - 1]

    for y in rows:
      for x in range(math.floor(len(arrGS[y]) / 2)):
        x = x * 2 + 1

        if (generateImage):
          arrCopy[y][x] = [255, 255, 0]

        if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

          if (generateImage):
            arrCopy[y][x] = [255, 0, 0]

          pointX = x;
          pointY = y;
          break

    for x in cols:
      for y in range(math.floor(len(arrGS) / 2)):
        y = y * 2 + 1

        if (generateImage):
          arrCopy[y][x] = [255, 255, 0]

        if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

          if (generateImage):
            arrCopy[y][x] = [255, 0, 0]

          pointX = x;
          pointY = y;
          break

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'spot_double_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def roundSearch(arrGS, arr, folder_path, iii, generateImage):
  if (generateImage):
    arrCopy = arr.copy()

  width = len(arrGS[0])
  height = len(arrGS)
  pointX = -1
  pointY = -1
  imgCenterX = math.floor(width / 2)
  imgCenterY = math.floor(height / 2) 
  flag = False

  for rad in range(math.floor(width / 2)):
    topLeftX = imgCenterX - rad - 1
    topLeftY = imgCenterY - rad - 1
    topRightX = imgCenterX + rad
    topRightY = imgCenterY - rad - 1
    bottomRightX = imgCenterX + rad
    bottomRightY = imgCenterY + rad + 1
    bottomLeftX = imgCenterX - rad - 1
    bottomLeftY = imgCenterY + rad

    color = [0, 255, 0]
    if (rad % 2 == 0):
      color = [0, 0, 255]
      
    for x in range(topLeftX, topRightX):
      y = topLeftY

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0]

        pointX = x
        pointY = y
        flag = True
        break

    for x in range(bottomLeftX, bottomRightX):
      y = bottomLeftY

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0] 

        pointX = x
        pointY = y
        flag = True
        break

    for y in range(topLeftY, bottomLeftY):
      x = topLeftX

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0]

        pointX = x
        pointY = y
        flag = True
        break

    for y in range(topRightY, bottomRightY):
      x = topRightX

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0] 

        pointX = x
        pointY = y
        flag = True
        break

    if (flag):
       break;

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'spot_round_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def roundDoubleSearch(arrGS, arr, folder_path, iii, generateImage):
  if (generateImage):
    arrCopy = arr.copy()

  width = len(arrGS[0]) - 1
  height = len(arrGS) - 1
  pointX = -1
  pointY = -1
  imgCenterX = math.floor(width / 2)
  imgCenterY = math.floor(height / 2) 
  flag = False

  for rad in range(math.floor(width / 2) + 1):
    topLeftX = imgCenterX - rad 
    topLeftY = imgCenterY - rad
    topRightX = imgCenterX + rad 
    topRightY = imgCenterY - rad
    bottomRightX = imgCenterX + rad + 1
    bottomRightY = imgCenterY + rad + 1
    bottomLeftX = imgCenterX - rad
    bottomLeftY = imgCenterY + rad

    color = [0, 255, 0]
    if (rad % 2 == 0):
      color = [0, 0, 255]
      
    for x in range(topLeftX, topRightX, 2):
      y = topLeftY

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0]

        pointX = x
        pointY = y
        flag = True
        break

    for x in range(bottomLeftX, bottomRightX, 2):
      y = bottomLeftY

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0] 

        pointX = x
        pointY = y
        flag = True
        break

    for y in reversed(range(topLeftY, bottomLeftY, 2)):
      x = topLeftX

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0]

        pointX = x
        pointY = y
        flag = True
        break

    for y in reversed(range(topRightY, bottomRightY, 2)):
      x = topRightX

      if (generateImage):
        arrCopy[y][x] = color

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        if (generateImage):
          arrCopy[y][x] = [255, 0, 0] 

        pointX = x
        pointY = y
        flag = True
        break

    if (flag):
       break;

  if (pointX == -1 or pointY == -1):
    rows = [0, len(arrGS) - 1]
    cols = [0, len(arrGS[0]) - 1]

    for y in rows:
      for x in range(len(arrGS[y])):

        if (generateImage):
          arrCopy[y][x] = [255, 255, 0]

        if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

          if (generateImage):
            arrCopy[y][x] = [255, 0, 0]

          pointX = x;
          pointY = y;
          break

    for x in cols:
      for y in range(len(arrGS)):

        if (generateImage):
          arrCopy[y][x] = [255, 255, 0]

        if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

          if (generateImage):
            arrCopy[y][x] = [255, 0, 0]

          pointX = x;
          pointY = y;
          break

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, 'spot_round_double_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def breadthSpot(arrGS, point, arr, folder_path, iii, generateImage, algoType):
  if (generateImage):
    arrCopy = arr.copy()
  if (point[0] == -1 or point[1] == -1):
    if (generateImage):
      fileName = algoType + 'breadth_image_' + str(iii) + '.png'

      img = Image.fromarray(arrCopy)
      img.save(os.path.join(folder_path, fileName))
    return [0, 0]

  if (generateImage):
    arrCopy = arr.copy()
  spotX = -1
  spotY = -1
  flag = False

  point = tuple(point)
  frontier = deque()
  frontier.append(point)
  reached = set()
  reached.add(point)

  while (not len(frontier) == 0):
    if (flag):
      break

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
        
        if (generateImage):
          arrCopy[next[1], next[0]] = [0, 255, 0]

        frontier.append(next)
        reached.add(next)

        if (arrGS[next[1]][next[0]][0] > 10 or arrGS[next[1]][next[0]][1] < 255):
          spotX = next[0] 
          spotY = next[1] 
          flag = True
          break

  if (generateImage):
    fileName = algoType + 'breadth_image_' + str(iii) + '.png'

    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, fileName))


  return [spotX, spotY]

@profile
def imageProcessing():
  for iii in range(1, 501):
    rel_path = ('../images/circle_' + str(iii) + '.png')
    abs_path = os.path.join(script_dir, rel_path)
    folder_rel_path = ('./images/image_' + str(iii))
    folder_path = os.path.join(script_dir, folder_rel_path)
    # os.makedirs(os.path.join(script_dir, folder_path), exist_ok=True)

    arr = np.asarray(Image.open(abs_path))
    arrGS = np.asarray(Image.open(abs_path).convert('LA'))
    generateImage = False

# brute
# =============================================================

    start_1 = time.time()
    bruteCenter = bruteForce(arrGS, arr, folder_path, iii, generateImage)
    end_1 = time.time()

    global timeBruteOverall
    timeBruteOverall += end_1 - start_1
    timeBruteString = "%.4f" %(end_1 - start_1) + ' s',

# rand spot
# =============================================================

    start_2 = time.time()
    randPoint = randomSpot(arrGS, arr, folder_path, iii, generateImage)
    end_2 = time.time()

    global timeRandomSpotOverall
    timeRandomSpotOverall += end_2 - start_2
    timeSpotString = "%.4f" %(end_2 - start_2) + ' s',

# rand spot + brute / 4
# =============================================================

    start_3 = time.time()
    randCenter = randPick(arrGS, randPoint, arr, folder_path, iii, generateImage)
    end_3 = time.time()

    global timeRandomOverall
    timeRandomOverall += end_3 - start_3
    timeRandString = "%.4f" %(end_3 - start_3) + ' s',

# rand spot + breadth
# =============================================================

    start_4 = time.time()
    breadthCenter = breadthSearch(arrGS, randPoint, arr, folder_path, iii, False, 'r_')
    end_4 = time.time()

    global timeBreadthOverall
    timeBreadthOverall += end_4 - start_4
    timeSBreadthtring = "%.4f" %(end_4 - start_4) + ' s',

# double spot
# =============================================================

    start_5 = time.time()
    doublePoint = doubleSearch(arrGS, arr, folder_path, iii, generateImage)
    end_5 = time.time()

    global timeDoubleSpotOverall
    timeDoubleSpotOverall += end_5 - start_5
    timeDoublePointString = "%.4f" %(end_5 - start_5) + ' s',

# double spot + breadth
# =============================================================

    start_6 = time.time()
    doubleBreadthCenter = breadthSearch(arrGS, doublePoint, arr, folder_path, iii, False, 'd_')
    end_6 = time.time()

    global timeDoubleBreadthOverall
    timeDoubleBreadthOverall += end_6 - start_6
    timeDoubleBreadthString = "%.4f" %(end_6 - start_6) + ' s',

# round spot
# =============================================================

    start_7 = time.time()
    roundSpot = roundSearch(arrGS, arr, folder_path, iii, generateImage)
    end_7 = time.time()

    global timeRoundSpotOverall
    timeRoundSpotOverall += end_7 - start_7
    timeRoundSpotString = "%.4f" %(end_7 - start_7) + ' s',

# round spot + breadth
# =============================================================

    start_8 = time.time()
    roundBreadthCenter = breadthSearch(arrGS, roundSpot, arr, folder_path, iii, False, 'ro_')
    end_8 = time.time()

    global timeRoundBreadthOverall
    timeRoundBreadthOverall += end_8 - start_8
    timeRoundBreadthString = "%.4f" %(end_8 - start_8) + ' s',

# breadth spot
# =============================================================

    start_9 = time.time()
    cImX = math.floor(pxW / 2 - 1);
    cImY = math.floor(pxH / 2 - 1);
    breadthPoint = breadthSpot(arrGS, [cImX, cImY], arr, folder_path, iii, generateImage, 'spot_')
    end_9 = time.time()

    global timeBreadthSpotOverall
    timeBreadthSpotOverall += end_9 - start_9
    timeBreadthSpotString = "%.4f" %(end_9 - start_9) + ' s',

# breadth spot + breadth
# =============================================================

    start_10 = time.time()
    breadthBreadthCenter = breadthSearch(arrGS, breadthPoint, arr, folder_path, iii, False, 'br_')
    end_10 = time.time()

    global timeBreadthBreadthOverall
    timeBreadthBreadthOverall += end_10 - start_10
    timeBreadthBreadthString = "%.4f" %(end_10 - start_10) + ' s',

# round double spot
# =============================================================

    start_11 = time.time()
    roundDoubleSpot = roundDoubleSearch(arrGS, arr, folder_path, iii, generateImage)
    end_11 = time.time()

    global timeRoundDoubleSpotOverall
    timeRoundDoubleSpotOverall += end_11 - start_11
    timeRoundDoubleSpotString = "%.4f" %(end_11 - start_11) + ' s',

# round double spot + breadth
# =============================================================

    start_12 = time.time()
    roundDoubleBreadthCenter = breadthSearch(arrGS, roundDoubleSpot, arr, folder_path, iii, False, 'round-double_')
    end_12 = time.time()

    global timeRoundDoubleBreadthOverall
    timeRoundDoubleBreadthOverall += end_12 - start_12
    timeRoundDoubleBreadthString = "%.4f" %(end_12 - start_12) + ' s',

# print center & time
# =============================================================

    print(
    "iter:", iii,
    "\n  |  brute ", bruteCenter, timeBruteString,
    "\n  |  random brute " , randCenter, timeRandString, 
    "\n  |  random breadth " , breadthCenter, timeSBreadthtring, 
    "\n  |  double breadth ", doubleBreadthCenter, timeDoubleBreadthString, 
    "\n  |  round breadth ", roundBreadthCenter, timeRoundBreadthString, 
    "\n  |  breadth breadth", breadthBreadthCenter, timeBreadthBreadthString,
    "\n  |  round double breadth", roundDoubleBreadthCenter, timeRoundDoubleBreadthString,
    "\n  |  rand spot ", timeSpotString, 
    "\n  |  double spot ", timeDoublePointString,
    "\n  |  round spot", timeRoundSpotString,
    "\n  |  breadth spot", timeBreadthSpotString,
    "\n  |  round d spot", timeRoundDoubleSpotString,
    "\n"
    )
    
# append data
# =============================================================

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
      str(roundBreadthCenter[0]),
      str(roundBreadthCenter[1]),
      ''.join(timeRoundBreadthString),
      str(breadthBreadthCenter[0]),
      str(breadthBreadthCenter[1]),
      ''.join(timeBreadthBreadthString),
      str(roundDoubleBreadthCenter[0]),
      str(roundDoubleBreadthCenter[1]),
      ''.join(timeRoundDoubleBreadthString),
      ''.join(timeSpotString),
      ''.join(timeDoublePointString),
      ''.join(timeRoundSpotString),
      ''.join(timeBreadthSpotString),
      ''.join(timeRoundDoubleSpotString),
    ))

imageProcessing()

timeBruteOverall = ("%.4f" % (timeBruteOverall)) + ' s'
timeRandomOverall = ("%.4f" % (timeRandomOverall + timeRandomSpotOverall)) + ' s'
timeBreadthOverall = ("%.4f" % (timeBreadthOverall + timeRandomSpotOverall)) + ' s'
timeDoubleBreadthOverall = ("%.4f" % (timeDoubleBreadthOverall + timeDoubleSpotOverall)) + ' s'
timeRoundBreadthOverall = ("%.4f" % (timeRoundBreadthOverall + timeRoundSpotOverall)) + ' s'
timeBreadthBreadthOverall = ("%.4f" % (timeBreadthBreadthOverall + timeBreadthSpotOverall)) + ' s'
timeRoundDoubleBreadthOverall = ("%.4f" % (timeRoundDoubleBreadthOverall + timeRoundDoubleSpotOverall)) + ' s'

timeDoubleSpotOverall = ("%.4f" % (timeDoubleSpotOverall)) + ' s'
timeRoundSpotOverall = ("%.4f" % (timeRoundSpotOverall)) + ' s'
timeRandomSpotOverall = ("%.4f" % (timeRandomSpotOverall)) + ' s'
timeBreadthSpotOverall = ("%.4f" % (timeBreadthSpotOverall)) + ' s'
timeRoundDoubleSpotOverall = ("%.4f" % (timeRoundDoubleSpotOverall)) + ' s'

times = [
  " Brute:", timeBruteOverall, 
  "\n R Br:", timeRandomOverall, 
  "\n R Breadth:", timeBreadthOverall, 
  "\n Double breadth:", timeDoubleBreadthOverall, 
  "\n Round breadth:", timeRoundBreadthOverall, 
  "\n Breadth breadth:", timeBreadthBreadthOverall, 
  "\n Random Spot:", timeRandomSpotOverall, 
  "\n Double spot:", timeDoubleSpotOverall, 
  "\n Round:", timeRoundSpotOverall,
  "\n Breadth:", timeBreadthSpotOverall,
  "\n Round Double:", timeRoundDoubleSpotOverall,
  "\n"
]
print(times)

data.insert(0, ('Brute X', 'Brute Y', 'time',
  'Rand X', 'Rand Y', 'time',
  'R_Breadth X', 'R_Breadth Y', 'time', 
  'D_Breadth X', 'D_Breadth Y', 'time', 
  'Ro_Breadth X', 'Ro_Breadth Y', 'time', 
  'Br_Breadth X', 'Br_Breadth Y', 'time', 
  'RoD_Breadth X', 'RoD_Breadth Y', 'time', 
  'rand time', 'double time', 'round time', 'breadth', 'ro_do'
)) 

data.insert(0, (
  '', '', timeBruteOverall, 
  '', '', timeRandomOverall, 
  '', '', timeBreadthOverall, 
  '', '', timeDoubleBreadthOverall,
  '', '', timeBreadthBreadthOverall,
  '', '', timeRoundDoubleBreadthOverall,
  timeRandomSpotOverall,
  timeDoubleSpotOverall,
  timeRoundSpotOverall,
  timeBreadthSpotOverall,
  timeRoundDoubleSpotOverall,
  ))

with open('compare_py.csv', "w", newline="") as file:
  writer = csv.writer(file)
  for row in data:
    line = ';'.join(row)
    file.write(line + '\n')
  file.close()