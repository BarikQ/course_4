/*
 * _coder_brutForce_mex.h
 *
 * Code generation for function 'brutForce'
 *
 */

#ifndef _CODER_BRUTFORCE_MEX_H
#define _CODER_BRUTFORCE_MEX_H

/* Include files */
#include "emlrt.h"
#include "mex.h"
#include "tmwtypes.h"
#ifdef __cplusplus

extern "C" {

#endif

  /* Function Declarations */
  void brutForce_mexFunction(int32_T nlhs, mxArray *plhs[2], int32_T nrhs, const
    mxArray *prhs[1]);
  MEXFUNCTION_LINKAGE void mexFunction(int32_T nlhs, mxArray *plhs[], int32_T
    nrhs, const mxArray *prhs[]);
  emlrtCTX mexFunctionCreateRootTLS(void);

#ifdef __cplusplus

}
#endif
#endif

/* End of code generation (_coder_brutForce_mex.h) */
