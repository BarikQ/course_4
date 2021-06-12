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

# =================================================

timeBruteSpot_S = 0
timeRandSpot_S = 0
timeBreadthSpot_S = 0
timeDoubleSpot_S = 0
timeRoundSpot_S = 0
timeRoundDoubleSpot_s = 0

timeBruteDef_S = 0
timeBreadthCenter_S = 0
timeQuadroCenter_S = 0

# =================================================

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
  return [0, 0]
  dtotalX = []
  dtotalY = []
  rowFlag = False
  rowFlag_2 = False

  # if (generateImage):
    # arrCopy = arr.copy()

  for y, rows in enumerate(arrGS):
    colFlag = False

    for x, cols in enumerate(rows):
      # if (generateImage):
        # arrCopy[y][x] = [255, 255, 0]

      if (cols[0] > 10 or cols[1] < 255):

        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0]

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

  # if (generateImage):
    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, 'brute_image_' + str(iii) + '.png'))

  if (len(dtotalX) == 0 or len(dtotalY) == 0):
    return [0, 0]

  centerX = math.ceil(sum(dtotalX) / len(dtotalX))
  centerY = math.ceil(sum(dtotalY) / len(dtotalY))

  return [centerX, centerY]

def bruteSpot(arrGS, arr, folder_path, iii, generateImage):
  return [0, 0]
  y = 0
  x = 0
  spotX = -1
  spotY = -1
  flag = False

  # if (generateImage):
    # arrCopy = arr.copy()

  for y, rows in enumerate(arrGS):
    for x, cols in enumerate(rows):
      # if (generateImage):
        # arrCopy[y][x] = [255, 255, 0]

      if (cols[0] > 10 or cols[1] < 255):

        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0]

        spotX = x
        spotY = y
        flag = True
        break

    if (flag):
      break

  # if (generateImage):
    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, 'spot_brute_image_' + str(iii) + '.png'))

  return [spotX, spotY]

def randomSpot(arrGS, arr, folder_path, iii, generateImage):
  pointX = -1
  pointY = -1
  find = False
  rows = len(arrGS)
  cols = len(arrGS[0])
  # if (generateImage):
    # arrCopy = arr.copy()

  columns = np.array(range(0, len(arrGS)))
  matrix = np.array([{'row': x, 'columns': columns} for x in range(len(columns))])

  for iter in range(math.ceil(rows * cols / 4)): 
    if (find):
      break

    randRowIndex = random.randint(0, len(matrix) - 1)
    randRow = matrix[randRowIndex]['row']
    randColumnIndex = random.randint(0, len(matrix[randRowIndex]['columns']) - 1)
    randColumn = matrix[randRowIndex]['columns'][randColumnIndex]

    # if (generateImage):
      # arrCopy[randRow][randColumn] = [255, 0, 0]

    if (arrGS[randRow][randColumn][0] > 10 or arrGS[randRow][randColumn][1] < 255):
      find = True
      pointX = randColumn
      pointY = randRow

    np.delete(matrix[randRowIndex]['columns'], randColumnIndex)

    if (len(matrix[randRowIndex]['columns']) == 0):
      np.delete(matrix, randRowIndex)

  # if (generateImage):
    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, 'spot_rand_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def randomSpot_2(arrGS, arr, folder_path, iii, generateImage):
  return [-1, -1]
  pointX = -1
  pointY = -1
  find = False
  rows = len(arrGS)
  cols = len(arrGS[0])
  if (generateImage):
    arrCopy = arr.copy()

  randRows = list(range(rows));
  random.shuffle(randRows);
  randCols = list(range(cols));
  random.shuffle(randCols);

  for y in randRows:
    for x in randCols:
      if (generateImage):
        arrCopy[y][x] = [255, 0, 0]
      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        find = True
        pointX = x
        pointY = y
        break
    if (find):
      break

  if (generateImage):
    img = Image.fromarray(arrCopy)
    img.save(os.path.join(folder_path, '2spot_rand_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def quadroSearch(arrGS, point, arr, folder_path, iii, generateImage):
  # if (generateImage):
    # arrCopy = arr.copy()

  if (point[0] == -1 or point[1] == -1):
    # if (generateImage):
      # img = Image.fromarray(arrCopy)
      # img.save(os.path.join(folder_path, 'random_image_' + str(iii) + '.png'))
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
  dtotalX = []
  dtotalY = []
  rowFlag = False
  rowFlag_2 = False


  for y in range(quadroY[0], quadroY[2]):
    colFlag = False
    for x in range(quadroX[0], quadroX[2]):
      # if (generateImage):
        # arrCopy[y][x] = [255, 255, 0]

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0]

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

  centerX = math.ceil(sum(dtotalX) / len(dtotalX))
  centerY = math.ceil(sum(dtotalY) / len(dtotalY))

  # if (generateImage):
    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, 'c_rand_image_' + str(iii) + '.png'))

  return [centerX, centerY]

def breadthSearch(arrGS, point, arr, folder_path, iii, generateImage, algoType):
  # if (generateImage):
    # arrCopy = arr.copy()
  if (point[0] == -1 or point[1] == -1):
    # if (generateImage):
      # fileName = 'c_breadth_' + algoType + 'image_' + str(iii) + '.png'

      # img = Image.fromarray(arrCopy)
      # img.save(os.path.join(folder_path, fileName))
    return [0, 0]

  # if (generateImage):
    # arrCopy = arr.copy()

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
        
        # if (generateImage):
          arrCopy[next[1], next[0]] = [255, 0, 0]

        frontier.append(next)
        reached.add(next)
        dtotalX.append(next[0] + 1)
        dtotalY.append(next[1] + 1)

  # if (generateImage):
    fileName = 'c_breadth_' + algoType + 'image_' + str(iii) + '.png'

    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, fileName))

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

  # if (generateImage):
    # arrCopy = arr.copy()

  for y in range(0, math.floor(len(arrGS) / 2), 2):
    # y = y * 2
    for x in range(0, math.floor(len(arrGS[y]) / 2), 2):

      # if (generateImage):
        # arrCopy[y][x * 2] = [255, 0, 0]

      if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

        # if (generateImage):
          # arrCopy[y][x * 2] = [0, 0, 255]

        pointX = x;
        pointY = y;
        flag = True
        break
    
    if (flag):
      break

  # if (pointX == -1 or pointY == -1):
  #   rows = [0, len(arrGS) - 1]
  #   cols = [0, len(arrGS[0]) - 1]

  #   for y in rows:
  #     for x in range(math.floor(len(arrGS[y]) / 2)):

  #       # if (generateImage):
  #         # arrCopy[y][x] = [255, 255, 0]

  #       if (arrGS[y][x * 2 + 1][0] > 10 or arrGS[y][x * 2 + 1][1] < 255):

  #         # if (generateImage):
  #           # arrCopy[y][x] = [255, 0, 0]

  #         pointX = x;
  #         pointY = y;
  #         break

  #   for x in cols:
  #     for y in range(math.floor(len(arrGS) / 2)):

  #       # if (generateImage):
  #         # arrCopy[y][x] = [255, 255, 0]

  #       if (arrGS[y * 2 + 1][x][0] > 10 or arrGS[y * 2 + 1][x][1] < 255):

  #         # if (generateImage):
  #           # arrCopy[y][x] = [255, 0, 0]

  #         pointX = x;
  #         pointY = y;
  #         break

  # if (generateImage):
    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, 'spot_double_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def roundSearch(arrGS, arr, folder_path, iii, generateImage):
  # if (generateImage):
    # arrCopy = arr.copy()

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
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[topLeftY][x][0] > 10 or arrGS[topLeftY][x][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0]

        pointX = x
        pointY = topLeftY
        flag = True
        break

    for x in range(bottomLeftX, bottomRightX):
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[bottomLeftY][x][0] > 10 or arrGS[bottomLeftY][x][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0] 

        pointX = x
        pointY = bottomLeftY
        flag = True
        break

    for y in range(topLeftY, bottomLeftY):
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[y][topLeftX][0] > 10 or arrGS[y][topLeftX][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0]

        pointX = topLeftX
        pointY = y
        flag = True
        break

    for y in range(topRightY, bottomRightY):
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[y][topRightX][0] > 10 or arrGS[y][topRightX][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0] 

        pointX = topRightX
        pointY = y
        flag = True
        break

    if (flag):
       break;

  # if (generateImage):
    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, 'spot_round_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def roundDoubleSearch(arrGS, arr, folder_path, iii, generateImage):
  # if (generateImage):
    # arrCopy = arr.copy()

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
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[topLeftY][x][0] > 10 or arrGS[topLeftY][x][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0]

        pointX = x
        pointY = topLeftY
        flag = True
        break

    for x in range(bottomLeftX, bottomRightX, 2):
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[bottomLeftY][x][0] > 10 or arrGS[bottomLeftY][x][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0] 

        pointX = x
        pointY = bottomLeftY
        flag = True
        break

    for y in reversed(range(topLeftY, bottomLeftY, 2)):
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[y][topLeftX][0] > 10 or arrGS[y][topLeftX][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0]

        pointX = topLeftX
        pointY = y
        flag = True
        break

    for y in reversed(range(topRightY, bottomRightY, 2)):
      # if (generateImage):
        # arrCopy[y][x] = color

      if (arrGS[y][topRightX][0] > 10 or arrGS[y][topRightX][1] < 255):
        # if (generateImage):
          # arrCopy[y][x] = [255, 0, 0] 

        pointX = topRightX
        pointY = y
        flag = True
        break

    if (flag):
       break;

  # if (pointX == -1 or pointY == -1):
  #   rows = [0, len(arrGS) - 1]
  #   cols = [0, len(arrGS[0]) - 1]

    # for y in rows:
    #   for x in range(len(arrGS[y])):

    #     # if (generateImage):
    #       # arrCopy[y][x] = [255, 255, 0]

    #     if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

    #       # if (generateImage):
    #         # arrCopy[y][x] = [255, 0, 0]

    #       pointX = x;
    #       pointY = y;
    #       break

    # for x in cols:
    #   for y in range(len(arrGS)):

    #     # if (generateImage):
    #       # arrCopy[y][x] = [255, 255, 0]

    #     if (arrGS[y][x][0] > 10 or arrGS[y][x][1] < 255):

    #       # if (generateImage):
    #         # arrCopy[y][x] = [255, 0, 0]

    #       pointX = x;
    #       pointY = y;
    #       break

  # if (generateImage):
    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, 'spot_round_double_image_' + str(iii) + '.png'))

  return [pointX, pointY]

def breadthSpot(arrGS, point, arr, folder_path, iii, generateImage, algoType):
  return [0, 0]
  # if (generateImage):
    # arrCopy = arr.copy()
  if (point[0] == -1 or point[1] == -1):
    # if (generateImage):
      # fileName = algoType + 'breadth_image_' + str(iii) + '.png'

      # img = Image.fromarray(arrCopy)
      # img.save(os.path.join(folder_path, fileName))
    return [0, 0]

  # if (generateImage):
    # arrCopy = arr.copy()
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
        
        # if (generateImage):
          # arrCopy[next[1], next[0]] = [0, 255, 0]

        frontier.append(next)
        reached.add(next)

        if (arrGS[next[1]][next[0]][0] > 10 or arrGS[next[1]][next[0]][1] < 255):
          spotX = next[0] 
          spotY = next[1] 
          flag = True
          break

  # if (generateImage):
    # fileName = algoType + 'breadth_image_' + str(iii) + '.png'

    # img = Image.fromarray(arrCopy)
    # img.save(os.path.join(folder_path, fileName))


  return [spotX, spotY]

@profile
def imageProcessing():
  for iii in range(1, 50):
    rel_path = ('../images/circle_' + str(iii) + '.png')
    abs_path = os.path.join(script_dir, rel_path)
    folder_rel_path = ('./images/image_' + str(iii))
    folder_path = os.path.join(script_dir, folder_rel_path)
    # os.makedirs(os.path.join(script_dir, folder_path), exist_ok=True)

    arr = np.asarray(Image.open(abs_path))
    arrGS = np.asarray(Image.open(abs_path).convert('LA'))
    generateImage = False

# bruteForce
# =============================================================

    start_1 = time.time()
    bruteCenter = bruteForce(arrGS, arr, folder_path, iii, generateImage)
    end_1 = time.time()
    bruteCenter = [0, 0]
    global timeBruteDef_S
    timeBruteDef_S += end_1 - start_1
    timeBruteDefString = "%.4f" %(end_1 - start_1) + ' s',

# brute spot
# =============================================================

    start_2 = time.time()
    brutePoint = bruteSpot(arrGS, arr, folder_path, iii, generateImage)
    end_2 = time.time()
    brutePoint = [0, 0]
    global timeBruteSpot_S
    timeBruteSpot_S += end_2 - start_2
    timeBruteSpotString = "%.4f" %(end_2 - start_2) + ' s',

# rand spot
# =============================================================

    start_3 = time.time()
    randPoint = randomSpot_2(arrGS, arr, folder_path, iii, generateImage)
    end_3 = time.time()

    global timeRandSpot_S
    timeRandSpot_S += end_3 - start_3
    timeRandSpotString = "%.4f" %(end_3 - start_3) + ' s',

# quadro
# =============================================================

    start_4 = time.time()
    quadroCenter = quadroSearch(arrGS, randPoint, arr, folder_path, iii, generateImage)
    end_4 = time.time()

    global timeQuadroCenter_S
    timeQuadroCenter_S += end_4 - start_4
    timeQuadroCenterString = "%.4f" %(end_4 - start_4) + ' s',

# breadth
# =============================================================

    start_5 = time.time()
    breadthCenter = breadthSearch(arrGS, randPoint, arr, folder_path, iii, True, 'r_')
    end_5 = time.time()

    global timeBreadthCenter_S
    timeBreadthCenter_S += end_5 - start_5
    timeBreadthCenterString = "%.4f" %(end_5 - start_5) + ' s',

# double spot
# =============================================================

    start_6 = time.time()
    doublePoint = doubleSearch(arrGS, arr, folder_path, iii, generateImage)
    end_6 = time.time()

    global timeDoubleSpot_S
    timeDoubleSpot_S += end_6 - start_6
    timeDoubleSpotString = "%.4f" %(end_6 - start_6) + ' s',

# round spot
# =============================================================

    start_7 = time.time()
    roundSpot = roundSearch(arrGS, arr, folder_path, iii, generateImage)
    end_7 = time.time()

    global timeRoundSpot_S
    timeRoundSpot_S += end_7 - start_7
    timeRoundSpotString = "%.4f" %(end_7 - start_7) + ' s',

# breadth spot
# =============================================================

    start_8 = time.time()
    cImX = math.floor(pxW / 2 - 1);
    cImY = math.floor(pxH / 2 - 1);
    breadthPoint = breadthSpot(arrGS, [cImX, cImY], arr, folder_path, iii, generateImage, 'spot_')
    end_8 = time.time()

    global timeBreadthSpot_S 
    timeBreadthSpot_S += end_8 - start_8
    timeBreadthSpotString = "%.4f" %(end_8 - start_8) + ' s',

# round double spot
# =============================================================

    start_9 = time.time()
    roundDoubleSpot = roundDoubleSearch(arrGS, arr, folder_path, iii, generateImage)
    end_9 = time.time()

    global timeRoundDoubleSpot_s
    timeRoundDoubleSpot_s += end_9 - start_9
    timeRoundDoubleSpotString = "%.4f" %(end_9 - start_9) + ' s',

# print center & time
# =============================================================

    print(
    "iter:", iii,
    "\n  |  brute ", bruteCenter, timeBruteDefString,
    "\n  |  quadro " , quadroCenter, timeQuadroCenterString, 
    "\n  |  breadth " , breadthCenter, timeBreadthCenterString, 
    "\n  |  brute spot: ", timeBruteSpotString,
    "\n  |  rand spot ", timeRandSpotString, 
    "\n  |  double spot ", timeDoubleSpotString,
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
      ''.join(timeBruteDefString),
      str(quadroCenter[0]),
      str(quadroCenter[1]),
      ''.join(timeQuadroCenterString),
      str(breadthCenter[0]),
      str(breadthCenter[1]),
      ''.join(timeBreadthCenterString),
      ''.join(timeBruteSpotString),
      ''.join(timeRandSpotString),
      ''.join(timeDoubleSpotString),
      ''.join(timeRoundSpotString),
      ''.join(timeBreadthSpotString),
      ''.join(timeRoundDoubleSpotString),
    ))

imageProcessing()

# ===============================================================

timeBruteSpot_S = ("%.4f" % (timeBruteSpot_S)) + ' s'
timeRandSpot_S = ("%.4f" % (timeRandSpot_S)) + ' s'
timeBreadthSpot_S = ("%.4f" % (timeBreadthSpot_S)) + ' s'
timeDoubleSpot_S = ("%.4f" % (timeDoubleSpot_S)) + ' s'
timeRoundSpot_S = ("%.4f" % (timeRoundSpot_S)) + ' s'
timeRoundDoubleSpot_s = ("%.4f" % (timeRoundDoubleSpot_s)) + ' s'

# ===============================================================

timeBruteDef_S = ("%.4f" % (timeBruteDef_S)) + ' s'
timeQuadroCenter_S = ("%.4f" % (timeQuadroCenter_S)) + ' s'
timeBreadthCenter_S = ("%.4f" % (timeBreadthCenter_S)) + ' s'

# ===============================================================

timeSpot = [timeBruteSpot_S, timeRandSpot_S, timeBreadthSpot_S, timeDoubleSpot_S, timeRoundSpot_S, timeRoundDoubleSpot_s]
timeLoc = [timeBruteDef_S, timeQuadroCenter_S, timeBreadthCenter_S]

# ===============================================================

times = [
  " Brute Def:", timeBruteDef_S, 
  "\n Quadro:", timeQuadroCenter_S, 
  "\n Breadth:", timeBreadthCenter_S, 
  "\n Brute Spot:", timeBruteSpot_S, 
  "\n Rand Spot:", timeRandSpot_S, 
  "\n Breadth Spot:", timeBreadthSpot_S, 
  "\n Double Spot:", timeDoubleSpot_S, 
  "\n Round spot:", timeRoundSpot_S, 
  "\n Round&Double spot:", timeRoundDoubleSpot_s,
  "\n"
]
print(times)

data.insert(0, ('Brute X', 'Brute Y', 'time',
  'Quad X', 'Quad Y', 'time',
  'Breadth X', 'Breadth Y', 'time', 
  'Brute', 'Rand', 'Double', 'Round', 'Breadth', 'Round&Double'
)) 

data.insert(0, (
  '', '', timeBruteDef_S, 
  '', '', timeQuadroCenter_S, 
  '', '', timeBreadthCenter_S, 
  timeBruteSpot_S,
  timeRandSpot_S,
  timeDoubleSpot_S,
  timeRoundSpot_S,
  timeBreadthSpot_S,
  timeRoundDoubleSpot_s,
  ))

for row in data:
  line = ';'.join(row)
  print(line)

with open('compare_py2.csv', "w", newline="") as file:
  writer = csv.writer(file)
  for row in data:
    line = ';'.join(row)
    file.write(line + '\n')
  file.close()