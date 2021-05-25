/*
 * main.c
 *
 * Code generation for function 'main'
 *
 */

/*************************************************************************/
/* This automatically generated example C main file shows how to call    */
/* entry-point functions that MATLAB Coder generated. You must customize */
/* this file for your application. Do not modify this file directly.     */
/* Instead, make a copy of this file, modify it, and integrate it into   */
/* your development environment.                                         */
/*                                                                       */
/* This file initializes entry-point function arguments to a default     */
/* size and value before calling the entry-point functions. It does      */
/* not store or use any values returned from the entry-point functions.  */
/* If necessary, it does pre-allocate memory for returned values.        */
/* You can use this file as a starting point for a main function that    */
/* you can deploy in your application.                                   */
/*                                                                       */
/* After you copy the file, and before you deploy it, you must make the  */
/* following changes:                                                    */
/* * For variable-size function arguments, change the example sizes to   */
/* the sizes that your application requires.                             */
/* * Change the example values of function arguments to the values that  */
/* your application requires.                                            */
/* * If the entry-point functions return values, store these values or   */
/* otherwise use them as required by your application.                   */
/*                                                                       */
/*************************************************************************/

/* Include files */
#include "main.h"
#include "brutForce.h"
#include "brutForce_terminate.h"

/* Function Declarations */
static void argInit_752x752_real_T(double result[565504]);
static double argInit_real_T(void);
static void main_brutForce(void);

/* Function Definitions */
static void argInit_752x752_real_T(double result[565504])
{
  int idx0;
  int idx1;

  /* Loop over the array to initialize each element. */
  for (idx0 = 0; idx0 < 752; idx0++) {
    for (idx1 = 0; idx1 < 752; idx1++) {
      /* Set the value of the array element.
         Change this value to the value that the application requires. */
      result[idx0 + 752 * idx1] = argInit_real_T();
    }
  }
}

static double argInit_real_T(void)
{
  return 0.0;
}

static void main_brutForce(void)
{
  static double dv[565504];
  double brutX;
  double brutY;

  /* Initialize function 'brutForce' input arguments. */
  /* Initialize function input argument 'imageGS'. */
  /* Call the entry-point 'brutForce'. */
  argInit_752x752_real_T(dv);
  brutForce(dv, &brutX, &brutY);
}

int main(int argc, const char * const argv[])
{
  (void)argc;
  (void)argv;

  /* The initialize function is being called automatically from your entry-point function. So, a call to initialize is not included here. */
  /* Invoke the entry-point functions.
     You can call entry-point functions multiple times. */
  main_brutForce();

  /* Terminate the application.
     You do not need to do this more than one time. */
  brutForce_terminate();
  return 0;
}

/* End of code generation (main.c) */
