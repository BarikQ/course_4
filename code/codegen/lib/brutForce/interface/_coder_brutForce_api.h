/*
 * _coder_brutForce_api.h
 *
 * Code generation for function 'brutForce'
 *
 */

#ifndef _CODER_BRUTFORCE_API_H
#define _CODER_BRUTFORCE_API_H

/* Include files */
#include "emlrt.h"
#include "tmwtypes.h"
#include <string.h>

/* Variable Declarations */
extern emlrtCTX emlrtRootTLSGlobal;
extern emlrtContext emlrtContextGlobal;

#ifdef __cplusplus

extern "C" {

#endif

  /* Function Declarations */
  void brutForce(real_T imageGS[565504], real_T *brutX, real_T *brutY);
  void brutForce_api(const mxArray * const prhs[1], int32_T nlhs, const mxArray *
                     plhs[2]);
  void brutForce_atexit(void);
  void brutForce_initialize(void);
  void brutForce_terminate(void);
  void brutForce_xil_shutdown(void);
  void brutForce_xil_terminate(void);

#ifdef __cplusplus

}
#endif
#endif

/* End of code generation (_coder_brutForce_api.h) */
