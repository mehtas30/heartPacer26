/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: AOO_3K04.c
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

#include "AOO_3K04.h"
#include "rtwtypes.h"
#include <math.h>
#include "AOO_3K04_types.h"

/* Named constants for Chart: '<Root>/Chart' */
#define AOO_3K04_IN_ATR_Pacing         ((uint8_T)1U)
#define AOO_3K04_IN_Charging_C22       ((uint8_T)2U)

/* Block signals (default storage) */
B_AOO_3K04_T AOO_3K04_B;

/* Block states (default storage) */
DW_AOO_3K04_T AOO_3K04_DW;

/* Real-time model */
static RT_MODEL_AOO_3K04_T AOO_3K04_M_;
RT_MODEL_AOO_3K04_T *const AOO_3K04_M = &AOO_3K04_M_;

/* Model step function */
void AOO_3K04_step(void)
{
  int32_T rtb_ATR_GND_CTRL;
  int32_T rtb_ATR_PACE_CTRL;
  int32_T rtb_PACE_CHARGE_CTRL;

  /* Chart: '<Root>/Chart' incorporates:
   *  Constant: '<S2>/Constant'
   *  Constant: '<S2>/Constant1'
   *  Constant: '<S2>/Constant2'
   */
  if (AOO_3K04_DW.temporalCounter_i1 < MAX_uint32_T) {
    AOO_3K04_DW.temporalCounter_i1++;
  }

  if (AOO_3K04_DW.is_active_c3_AOO_3K04 == 0U) {
    AOO_3K04_DW.is_active_c3_AOO_3K04 = 1U;
    AOO_3K04_DW.is_c3_AOO_3K04 = AOO_3K04_IN_Charging_C22;
    AOO_3K04_DW.temporalCounter_i1 = 0U;
    AOO_3K04_B.VENT_PACE_CTRL = 0.0;
    AOO_3K04_B.VENT_GND_CTRL = 0.0;
    AOO_3K04_B.PACE_GND_CTRL = 1.0;
    AOO_3K04_B.Z_VENT_CTRL = 0.0;
    AOO_3K04_B.Z_ATR_CTRL = 0.0;
    AOO_3K04_B.PACING_REF_PWM = AOO_3K04_P.Constant1_Value * 10.0;
    rtb_ATR_PACE_CTRL = 0;
    rtb_ATR_GND_CTRL = 1;
    rtb_PACE_CHARGE_CTRL = 1;
  } else if (AOO_3K04_DW.is_c3_AOO_3K04 == AOO_3K04_IN_ATR_Pacing) {
    rtb_PACE_CHARGE_CTRL = 0;
    rtb_ATR_PACE_CTRL = 1;
    rtb_ATR_GND_CTRL = 0;
    if (AOO_3K04_DW.temporalCounter_i1 >= (uint32_T)ceil
        (AOO_3K04_P.Constant2_Value)) {
      AOO_3K04_DW.is_c3_AOO_3K04 = AOO_3K04_IN_Charging_C22;
      AOO_3K04_DW.temporalCounter_i1 = 0U;
      AOO_3K04_B.VENT_PACE_CTRL = 0.0;
      AOO_3K04_B.VENT_GND_CTRL = 0.0;
      AOO_3K04_B.PACE_GND_CTRL = 1.0;
      AOO_3K04_B.Z_VENT_CTRL = 0.0;
      AOO_3K04_B.Z_ATR_CTRL = 0.0;
      AOO_3K04_B.PACING_REF_PWM = AOO_3K04_P.Constant1_Value * 10.0;
      rtb_ATR_PACE_CTRL = 0;
      rtb_ATR_GND_CTRL = 1;
      rtb_PACE_CHARGE_CTRL = 1;
    }
  } else {
    /* case IN_Charging_C22: */
    AOO_3K04_B.VENT_PACE_CTRL = 0.0;
    AOO_3K04_B.VENT_GND_CTRL = 0.0;
    AOO_3K04_B.PACE_GND_CTRL = 1.0;
    AOO_3K04_B.Z_VENT_CTRL = 0.0;
    AOO_3K04_B.Z_ATR_CTRL = 0.0;
    rtb_ATR_PACE_CTRL = 0;
    rtb_ATR_GND_CTRL = 1;
    rtb_PACE_CHARGE_CTRL = 1;
    if (AOO_3K04_DW.temporalCounter_i1 >= (uint32_T)ceil(60000.0 /
         AOO_3K04_P.Constant_Value - AOO_3K04_P.Constant2_Value)) {
      AOO_3K04_DW.is_c3_AOO_3K04 = AOO_3K04_IN_ATR_Pacing;
      AOO_3K04_DW.temporalCounter_i1 = 0U;
      rtb_PACE_CHARGE_CTRL = 0;
      rtb_ATR_PACE_CTRL = 1;
      rtb_ATR_GND_CTRL = 0;
    }
  }

  /* End of Chart: '<Root>/Chart' */

  /* MATLABSystem: '<Root>/Digital Write10' */
  MW_digitalIO_write(AOO_3K04_DW.obj_g.MW_DIGITALIO_HANDLE, rtb_ATR_PACE_CTRL !=
                     0);

  /* MATLABSystem: '<Root>/Digital Write12' */
  MW_digitalIO_write(AOO_3K04_DW.obj_n.MW_DIGITALIO_HANDLE,
                     AOO_3K04_B.VENT_GND_CTRL != 0.0);

  /* MATLABSystem: '<Root>/Digital Write2' */
  MW_digitalIO_write(AOO_3K04_DW.obj_h.MW_DIGITALIO_HANDLE, rtb_ATR_PACE_CTRL !=
                     0);

  /* MATLABSystem: '<Root>/Digital Write3' */
  MW_digitalIO_write(AOO_3K04_DW.obj_jv.MW_DIGITALIO_HANDLE,
                     AOO_3K04_B.VENT_PACE_CTRL != 0.0);

  /* MATLABSystem: '<Root>/Digital Write4' */
  MW_digitalIO_write(AOO_3K04_DW.obj_b.MW_DIGITALIO_HANDLE, rtb_ATR_GND_CTRL !=
                     0);

  /* MATLABSystem: '<Root>/Digital Write5' */
  MW_digitalIO_write(AOO_3K04_DW.obj_l.MW_DIGITALIO_HANDLE,
                     AOO_3K04_B.PACE_GND_CTRL != 0.0);

  /* MATLABSystem: '<Root>/Digital Write6' */
  MW_digitalIO_write(AOO_3K04_DW.obj_i.MW_DIGITALIO_HANDLE,
                     AOO_3K04_B.Z_ATR_CTRL != 0.0);

  /* MATLABSystem: '<Root>/Digital Write7' */
  MW_digitalIO_write(AOO_3K04_DW.obj_j.MW_DIGITALIO_HANDLE,
                     AOO_3K04_B.Z_VENT_CTRL != 0.0);

  /* MATLABSystem: '<Root>/Digital Write9' */
  MW_digitalIO_write(AOO_3K04_DW.obj.MW_DIGITALIO_HANDLE, rtb_PACE_CHARGE_CTRL
                     != 0);

  /* MATLABSystem: '<Root>/PWM Output' */
  MW_PWM_SetDutyCycle(AOO_3K04_DW.obj_e0.MW_PWM_HANDLE,
                      AOO_3K04_B.PACING_REF_PWM);

  /* MATLABSystem: '<Root>/Digital Write8' */
  MW_digitalIO_write(AOO_3K04_DW.obj_e.MW_DIGITALIO_HANDLE, false);
}

/* Model initialize function */
void AOO_3K04_initialize(void)
{
  {
    freedomk64f_DigitalWrite_AOO__T *obj;
    freedomk64f_PWMOutput_AOO_3K0_T *obj_0;

    /* Start for MATLABSystem: '<Root>/Digital Write10' */
    AOO_3K04_DW.obj_g.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_g.isInitialized = 0;
    AOO_3K04_DW.obj_g.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_g;
    AOO_3K04_DW.obj_g.isSetupComplete = false;
    AOO_3K04_DW.obj_g.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(44U, 1);
    AOO_3K04_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write12' */
    AOO_3K04_DW.obj_n.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_n.isInitialized = 0;
    AOO_3K04_DW.obj_n.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_n;
    AOO_3K04_DW.obj_n.isSetupComplete = false;
    AOO_3K04_DW.obj_n.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    AOO_3K04_DW.obj_n.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write2' */
    AOO_3K04_DW.obj_h.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_h.isInitialized = 0;
    AOO_3K04_DW.obj_h.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_h;
    AOO_3K04_DW.obj_h.isSetupComplete = false;
    AOO_3K04_DW.obj_h.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    AOO_3K04_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write3' */
    AOO_3K04_DW.obj_jv.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_jv.isInitialized = 0;
    AOO_3K04_DW.obj_jv.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_jv;
    AOO_3K04_DW.obj_jv.isSetupComplete = false;
    AOO_3K04_DW.obj_jv.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    AOO_3K04_DW.obj_jv.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write4' */
    AOO_3K04_DW.obj_b.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_b.isInitialized = 0;
    AOO_3K04_DW.obj_b.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_b;
    AOO_3K04_DW.obj_b.isSetupComplete = false;
    AOO_3K04_DW.obj_b.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    AOO_3K04_DW.obj_b.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write5' */
    AOO_3K04_DW.obj_l.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_l.isInitialized = 0;
    AOO_3K04_DW.obj_l.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_l;
    AOO_3K04_DW.obj_l.isSetupComplete = false;
    AOO_3K04_DW.obj_l.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    AOO_3K04_DW.obj_l.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write6' */
    AOO_3K04_DW.obj_i.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_i.isInitialized = 0;
    AOO_3K04_DW.obj_i.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_i;
    AOO_3K04_DW.obj_i.isSetupComplete = false;
    AOO_3K04_DW.obj_i.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    AOO_3K04_DW.obj_i.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write7' */
    AOO_3K04_DW.obj_j.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_j.isInitialized = 0;
    AOO_3K04_DW.obj_j.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_j;
    AOO_3K04_DW.obj_j.isSetupComplete = false;
    AOO_3K04_DW.obj_j.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    AOO_3K04_DW.obj_j.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write9' */
    AOO_3K04_DW.obj.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj.isInitialized = 0;
    AOO_3K04_DW.obj.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj;
    AOO_3K04_DW.obj.isSetupComplete = false;
    AOO_3K04_DW.obj.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    AOO_3K04_DW.obj.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/PWM Output' */
    AOO_3K04_DW.obj_e0.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_e0.isInitialized = 0;
    AOO_3K04_DW.obj_e0.matlabCodegenIsDeleted = false;
    obj_0 = &AOO_3K04_DW.obj_e0;
    AOO_3K04_DW.obj_e0.isSetupComplete = false;
    AOO_3K04_DW.obj_e0.isInitialized = 1;
    obj_0->MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(AOO_3K04_DW.obj_e0.MW_PWM_HANDLE);
    AOO_3K04_DW.obj_e0.isSetupComplete = true;

    /* Start for MATLABSystem: '<Root>/Digital Write8' */
    AOO_3K04_DW.obj_e.matlabCodegenIsDeleted = true;
    AOO_3K04_DW.obj_e.isInitialized = 0;
    AOO_3K04_DW.obj_e.matlabCodegenIsDeleted = false;
    obj = &AOO_3K04_DW.obj_e;
    AOO_3K04_DW.obj_e.isSetupComplete = false;
    AOO_3K04_DW.obj_e.isInitialized = 1;
    obj->MW_DIGITALIO_HANDLE = MW_digitalIO_open(42U, 1);
    AOO_3K04_DW.obj_e.isSetupComplete = true;
  }
}

/* Model terminate function */
void AOO_3K04_terminate(void)
{
  /* Terminate for MATLABSystem: '<Root>/Digital Write10' */
  if (!AOO_3K04_DW.obj_g.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_g.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_g.isInitialized == 1) &&
        AOO_3K04_DW.obj_g.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_g.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write10' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write12' */
  if (!AOO_3K04_DW.obj_n.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_n.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_n.isInitialized == 1) &&
        AOO_3K04_DW.obj_n.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_n.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write12' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write2' */
  if (!AOO_3K04_DW.obj_h.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_h.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_h.isInitialized == 1) &&
        AOO_3K04_DW.obj_h.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_h.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write2' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write3' */
  if (!AOO_3K04_DW.obj_jv.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_jv.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_jv.isInitialized == 1) &&
        AOO_3K04_DW.obj_jv.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_jv.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write3' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write4' */
  if (!AOO_3K04_DW.obj_b.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_b.isInitialized == 1) &&
        AOO_3K04_DW.obj_b.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_b.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write4' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write5' */
  if (!AOO_3K04_DW.obj_l.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_l.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_l.isInitialized == 1) &&
        AOO_3K04_DW.obj_l.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_l.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write5' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write6' */
  if (!AOO_3K04_DW.obj_i.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_i.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_i.isInitialized == 1) &&
        AOO_3K04_DW.obj_i.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_i.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write6' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write7' */
  if (!AOO_3K04_DW.obj_j.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_j.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_j.isInitialized == 1) &&
        AOO_3K04_DW.obj_j.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_j.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write7' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write9' */
  if (!AOO_3K04_DW.obj.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj.isInitialized == 1) && AOO_3K04_DW.obj.isSetupComplete)
    {
      MW_digitalIO_close(AOO_3K04_DW.obj.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write9' */

  /* Terminate for MATLABSystem: '<Root>/PWM Output' */
  if (!AOO_3K04_DW.obj_e0.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_e0.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_e0.isInitialized == 1) &&
        AOO_3K04_DW.obj_e0.isSetupComplete) {
      MW_PWM_Stop(AOO_3K04_DW.obj_e0.MW_PWM_HANDLE);
      MW_PWM_Close(AOO_3K04_DW.obj_e0.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/PWM Output' */

  /* Terminate for MATLABSystem: '<Root>/Digital Write8' */
  if (!AOO_3K04_DW.obj_e.matlabCodegenIsDeleted) {
    AOO_3K04_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((AOO_3K04_DW.obj_e.isInitialized == 1) &&
        AOO_3K04_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(AOO_3K04_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<Root>/Digital Write8' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
