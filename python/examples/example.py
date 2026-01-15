'''
Author: wang yining
Date: 2025-12-29 23:56:31
LastEditTime: 2026-01-02 15:49:24
FilePath: /openarm_can/python/examples/example.py
Description: 
e-mail: wangyining0408@outlook.com
'''
# Copyright 2025 Enactic, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import openarm_can as oa
import time
# Create OpenArm instance

arm = oa.OpenArm("vcan0", False)

# Initialize arm motors
motor_types = [oa.MotorType.DM8009]
send_ids = [0x01]
recv_ids = [0x00]
arm.init_arm_motors(motor_types, send_ids, recv_ids)


arm.query_param_all(10)

arm.recv_all()

# 3. 从每个电机对象中提取获取到的参数
params = []
for m in arm.get_arm().get_motors():
    # get_param 返回的是 ParamResult 结构体
    res = m.get_param(10)
    try:
        if res.valid:
            params.append(res.value)
        else:
            params.append(None) # 或者根据需要设为 np.nan
    except Exception as e:
        params.append(res)

print(params)


        
# Initialize gripper
# arm.init_gripper_motor(oa.MotorType.DM4310, 0x7, 0x17)
# arm.set_callback_mode_all(oa.CallbackMode.IGNORE)
# # Use high-level operations
# arm.enable_all()
# arm.recv_all()


# # return to zero position
# arm.set_callback_mode_all(oa.CallbackMode.STATE)
# arm.get_arm().mit_control_all([oa.MITParam(2, 0.5, 0, 0, 0),
#                                oa.MITParam(2, 0.5, 0, 0, 0)])

# arm.recv_all()

# # torque control test

# arm.get_gripper().mit_control_all([oa.MITParam(0, 0, 0, 0, 0.15)])
# arm.get_arm().mit_control_all(
#     [oa.MITParam(0, 0, 0, 0, 0.15), oa.MITParam(0, 0, 0, 0, 0.15)])
# arm.recv_all()

# read motor position
# while True:
#     arm.refresh_all()
#     arm.recv_all()
#     for motor in arm.get_arm().get_motors():
#         print(motor.get_position())
#     for motor in arm.get_gripper().get_motors():
#         print(motor.get_position())
