/*
 * _coder_brutForce_api.c
 *
 * Code generation for function 'brutForce'
 *
 */

/* Include files */
#include "_coder_brutForce_api.h"
#include "_coder_brutForce_mex.h"

/* Variable Definitions */
emlrtCTX emlrtRootTLSGlobal = NULL;
emlrtContext emlrtContextGlobal = { true,/* bFirstTime */
  false,                               /* bInitialized */
  131595U,                             /* fVersionInfo */
  NULL,                                /* fErrorFunction */
  "brutForce",                         /* fFunctionName */
  NULL,                                /* fRTCallStack */
  false,                               /* bDebugMode */
  { 2045744189U, 2170104910U, 2743257031U, 4284093946U },/* fSigWrd */
  NULL                                 /* fSigMem */
};

/* Function Declarations */
static real_T (*b_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId))[565504];
static real_T (*c_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src,
  const emlrtMsgIdentifier *msgId))[565504];
static real_T (*emlrt_marshallIn(const emlrtStack *sp, const mxArray *imageGS,
  const char_T *identifier))[565504];
static const mxArray *emlrt_marshallOut(const real_T u);

/* Function Definitions */
static real_T (*b_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId))[565504]
{
  real_T (*y)[565504];
  y = c_emlrt_marshallIn(sp, emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
  return y;
}
  static real_T (*c_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src,
  const emlrtMsgIdentifier *msgId))[565504]
{
  static const int32_T dims[2] = { 752, 752 };

  real_T (*ret)[565504];
  emlrtCheckBuiltInR2012b(sp, msgId, src, "double", false, 2U, dims);
  ret = (real_T (*)[565504])emlrtMxGetData(src);
  emlrtDestroyArray(&src);
  return ret;
}

static real_T (*emlrt_marshallIn(const emlrtStack *sp, const mxArray *imageGS,
  const char_T *identifier))[565504]
{
  emlrtMsgIdentifier thisId;
  real_T (*y)[565504];
  thisId.fIdentifier = (const char_T *)identifier;
  thisId.fParent = NULL;
  thisId.bParentIsCell = false;
  y = b_emlrt_marshallIn(sp, emlrtAlias(imageGS), &thisId);
  emlrtDestroyArray(&imageGS);
  return y;
}
  static const mxArray *emlrt_marshallOut(const real_T u)
{
  const mxArray *m;
  const mxArray *y;
  y = NULL;
  m = emlrtCreateDoubleScalar(u);
  emlrtAssign(&y, m);
  return y;
}

void brutForce_api(const mxArray * const prhs[1], int32_T nlhs, const mxArray
                   *plhs[2])
{
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  real_T (*imageGS)[565504];
  real_T brutX;
  real_T brutY;
  st.tls = emlrtRootTLSGlobal;

  /* Marshall function inputs */
  imageGS = emlrt_marshallIn(&st, emlrtAlias(prhs[0]), "imageGS");

  /* Invoke the target function */
  brutForce(*imageGS, &brutX, &brutY);

  /* Marshall function outputs */
  plhs[0] = emlrt_marshallOut(brutX);
  if (nlhs > 1) {
    plhs[1] = emlrt_marshallOut(brutY);
  }
}

void brutForce_atexit(void)
{
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  mexFunctionCreateRootTLS();
  st.tls = emlrtRootTLSGlobal;
  emlrtEnterRtStackR2012b(&st);
  emlrtLeaveRtStackR2012b(&st);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
  brutForce_xil_terminate();
  brutForce_xil_shutdown();
  emlrtExitTimeCleanup(&emlrtContextGlobal);
}

void brutForce_initialize(void)
{
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  mexFunctionCreateRootTLS();
  st.tls = emlrtRootTLSGlobal;
  emlrtClearAllocCountR2012b(&st, false, 0U, 0);
  emlrtEnterRtStackR2012b(&st);
  emlrtFirstTimeR2012b(emlrtRootTLSGlobal);
}

void brutForce_terminate(void)
{
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  st.tls = emlrtRootTLSGlobal;
  emlrtLeaveRtStackR2012b(&st);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

/* End of code generation (_coder_brutForce_api.c) */
