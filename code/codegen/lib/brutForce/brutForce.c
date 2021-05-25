/*
 * brutForce.c
 *
 * Code generation for function 'brutForce'
 *
 */

/* Include files */
#include "brutForce.h"
#include "brutForce_emxutil.h"
#include "brutForce_types.h"
#include <math.h>

/* Function Definitions */
void brutForce(const double imageGS[565504], double *brutX, double *brutY)
{
  emxArray_int16_T *coloredX;
  emxArray_int16_T *coloredY;
  double y;
  int b_i;
  int i;
  int j;
  int k;
  boolean_T exitg1;
  boolean_T isFlag;
  boolean_T isFlag2;
  emxInit_int16_T(&coloredX, 2);
  emxInit_int16_T(&coloredY, 2);

  /*  параметры устройства */
  /*  диаметр отверстия */
  /*  толщина отверстия */
  /*  высота отверстия */
  /* format long */
  /*  height = 4.51e-3;    % Размеры матрицы */
  /*  width = 2.88e-3; */
  /*  pxH = 480; */
  /*  вспомогательный массив углов */
  /*  координата x контура пятна */
  /*  координата y контура пятна */
  /*  x - контур пятна в пикселях */
  /*  y - контур пятна в пикселях */
  /*      coloredX = []; */
  /*      coloredY = []; */
  coloredX->size[0] = 1;
  coloredX->size[1] = 0;
  coloredY->size[0] = 1;
  coloredY->size[1] = 0;
  isFlag = false;
  isFlag2 = false;
  i = 0;
  exitg1 = false;
  while ((!exitg1) && (i < 752)) {
    for (j = 0; j < 480; j++) {
      if (imageGS[j + 752 * i] != 0.0) {
        k = coloredX->size[1];
        b_i = coloredX->size[0] * coloredX->size[1];
        coloredX->size[1]++;
        emxEnsureCapacity_int16_T(coloredX, b_i);
        coloredX->data[k] = (short)(i + 1);
        k = coloredY->size[1];
        b_i = coloredY->size[0] * coloredY->size[1];
        coloredY->size[1]++;
        emxEnsureCapacity_int16_T(coloredY, b_i);
        coloredY->data[k] = (short)(j + 1);

        /*                  coloredX(end + 1) = i; */
        /*                  coloredY(end + 1) = j; */
        isFlag2 = true;
        isFlag = ((coloredX->size[1] == 1) || isFlag);
      }
    }

    if (isFlag && (!isFlag2)) {
      exitg1 = true;
    } else {
      isFlag2 = false;
      i++;
    }
  }

  if ((coloredX->size[1] == 0) || (coloredY->size[1] == 0)) {
    *brutX = 0.0;
    *brutY = 0.0;
  } else {
    i = coloredX->size[1];
    y = coloredX->data[0];
    for (k = 2; k <= i; k++) {
      y += (double)coloredX->data[k - 1];
    }

    *brutX = ceil(y / (double)coloredX->size[1]);
    i = coloredY->size[1];
    y = coloredY->data[0];
    for (k = 2; k <= i; k++) {
      y += (double)coloredY->data[k - 1];
    }

    *brutY = ceil(y / (double)coloredY->size[1]);
  }

  emxFree_int16_T(&coloredY);
  emxFree_int16_T(&coloredX);
}

/* End of code generation (brutForce.c) */
