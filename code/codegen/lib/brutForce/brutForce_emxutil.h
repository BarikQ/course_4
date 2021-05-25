/*
 * brutForce_emxutil.h
 *
 * Code generation for function 'brutForce_emxutil'
 *
 */

#ifndef BRUTFORCE_EMXUTIL_H
#define BRUTFORCE_EMXUTIL_H

/* Include files */
#include "brutForce_types.h"
#include "rtwtypes.h"
#include <stddef.h>
#include <stdlib.h>
#ifdef __cplusplus

extern "C" {

#endif

  /* Function Declarations */
  extern void emxEnsureCapacity_int16_T(emxArray_int16_T *emxArray, int oldNumel);
  extern void emxFree_int16_T(emxArray_int16_T **pEmxArray);
  extern void emxInit_int16_T(emxArray_int16_T **pEmxArray, int numDimensions);

#ifdef __cplusplus

}
#endif
#endif

/* End of code generation (brutForce_emxutil.h) */
