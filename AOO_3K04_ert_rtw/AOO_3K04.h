/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: AOO_3K04.h
 *
 * Code generated for Simulink model 'AOO_3K04'.
 *
 * Model version                  : 1.19
 * Simulink Coder version         : 9.7 (R2022a) 13-Nov-2021
 * C/C++ source code generated on : Mon Oct 17 17:38:26 2022
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_AOO_3K04_h_
#define RTW_HEADER_AOO_3K04_h_
#ifndef AOO_3K04_COMMON_INCLUDES_
#define AOO_3K04_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#endif                                 /* AOO_3K04_COMMON_INCLUDES_ */

#include "AOO_3K04_types.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  real_T PACING_REF_PWM;               /* '<Root>/Chart' */
  real_T PACE_GND_CTRL;                /* '<Root>/Chart' */
  real_T Z_ATR_CTRL;                   /* '<Root>/Chart' */
  real_T VENT_GND_CTRL;                /* '<Root>/Chart' */
  real_T VENT_PACE_CTRL;               /* '<Root>/Chart' */
  real_T Z_VENT_CTRL;                  /* '<Root>/Chart' */
} B_AOO_3K04_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  freedomk64f_DigitalWrite_AOO__T obj; /* '<Root>/Digital Write9' */
  freedomk64f_DigitalWrite_AOO__T obj_e;/* '<Root>/Digital Write8' */
  freedomk64f_DigitalWrite_AOO__T obj_j;/* '<Root>/Digital Write7' */
  freedomk64f_DigitalWrite_AOO__T obj_i;/* '<Root>/Digital Write6' */
  freedomk64f_DigitalWrite_AOO__T obj_l;/* '<Root>/Digital Write5' */
  freedomk64f_DigitalWrite_AOO__T obj_b;/* '<Root>/Digital Write4' */
  freedomk64f_DigitalWrite_AOO__T obj_jv;/* '<Root>/Digital Write3' */
  freedomk64f_DigitalWrite_AOO__T obj_h;/* '<Root>/Digital Write2' */
  freedomk64f_DigitalWrite_AOO__T obj_n;/* '<Root>/Digital Write12' */
  freedomk64f_DigitalWrite_AOO__T obj_g;/* '<Root>/Digital Write10' */
  freedomk64f_PWMOutput_AOO_3K0_T obj_e0;/* '<Root>/PWM Output' */
  uint32_T temporalCounter_i1;         /* '<Root>/Chart' */
  uint8_T is_active_c3_AOO_3K04;       /* '<Root>/Chart' */
  uint8_T is_c3_AOO_3K04;              /* '<Root>/Chart' */
} DW_AOO_3K04_T;

/* Parameters (default storage) */
struct P_AOO_3K04_T_ {
  real_T Constant1_Value;              /* Expression: 5
                                        * Referenced by: '<S2>/Constant1'
                                        */
  real_T Constant2_Value;              /* Expression: 1
                                        * Referenced by: '<S2>/Constant2'
                                        */
  real_T Constant_Value;               /* Expression: 60
                                        * Referenced by: '<S2>/Constant'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_AOO_3K04_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_AOO_3K04_T AOO_3K04_P;

/* Block signals (default storage) */
extern B_AOO_3K04_T AOO_3K04_B;

/* Block states (default storage) */
extern DW_AOO_3K04_T AOO_3K04_DW;

/* Model entry point functions */
extern void AOO_3K04_initialize(void);
extern void AOO_3K04_step(void);
extern void AOO_3K04_terminate(void);

/* Real-time Model object */
extern RT_MODEL_AOO_3K04_T *const AOO_3K04_M;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<Root>/Scope' : Unused code path elimination
 * Block '<Root>/Scope1' : Unused code path elimination
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'AOO_3K04'
 * '<S1>'   : 'AOO_3K04/Chart'
 * '<S2>'   : 'AOO_3K04/Subsystem1'
 */
#endif                                 /* RTW_HEADER_AOO_3K04_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
