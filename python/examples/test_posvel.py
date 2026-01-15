'''
Author: wang yining
Date: 2025-12-29 23:56:31
LastEditTime: 2025-12-31 04:40:55
FilePath: /openarm_can/python/examples/test_posvel.py
Description: 
e-mail: wangyining0408@outlook.com
'''
import openarm_can as oa
import time

arm = oa.OpenArm("vcan0", False)

motor_types = [oa.MotorType.DM8009, oa.MotorType.DM8009]
send_ids = [0x01, 0x02]
recv_ids = [0x11, 0x12]

arm.init_arm_motors(motor_types, send_ids, recv_ids)

arm.set_callback_mode_all(oa.CallbackMode.STATE)
arm.enable_all()
# arm.disable_all()
target_pos = 2.0  # rad，给远一点

while True:
    arm.get_arm().posvel_control_one(
        1,
        oa.PosVelParam(target_pos, 10)
    )

    arm.refresh_all()
    arm.recv_all()

    for motor in arm.get_arm().get_motors():
        print("pos:", motor.get_position())

    time.sleep(0.01)
