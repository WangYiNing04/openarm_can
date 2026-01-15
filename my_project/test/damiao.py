'''
Author: wang yining
Date: 2025-12-29 23:57:02
LastEditTime: 2025-12-31 19:25:33
FilePath: /openarm_can/my_project/test/damiao.py
Description: 
e-mail: wangyining0408@outlook.com
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/12/29 12:47
# @Author : ZhangXi
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

# # Initialize arm motors
motor_types = [oa.MotorType.DM8009]
# motor_types = [oa.MotorType.DM8009,oa.MotorType.DM8009]
# # send_ids = [0x09,0x07]
# # recv_ids = [0x19,0x17]
send_ids = [0x01]
recv_ids = [0x11]
arm.init_arm_motors(motor_types, send_ids, recv_ids)

# #arm.enable_all()
# arm.disable_all()
# #arm.enable_all()
# # arm.get_arm().mit_control_one(1,oa.MITParam(0,0,0,0,-1))
# arm.get_arm().mit_control_all([oa.MITParam(0,0,0,0,-1),oa.MITParam(0,0,0,0,-1)])
# arm.get_arm().mit_control_all([oa.MITParam(0,0,0,0,0.8)])
# arm.refresh_all()
# arm.recv_all()
# for m in arm.get_arm().get_motors():
#     print("pos:", m.get_position(), "tau:", m.get_torque())


# for i, m in enumerate(arm.get_arm().get_motors()):
#     print(i, hex(m.get_send_id()))


# read motor position
# while True:
#     arm.refresh_all()
#     arm.recv_all()
#     for motor in arm.get_arm().get_motors():
#         print(motor.get_position())



for m in arm.get_arm().get_motors():
    print("pos:", m.get_position(), "tau:", m.get_torque())

arm.enable_all()
# arm.disable_all()
# # 1️⃣ 人工/程序把机械臂移动到“机械零位”
# #    （例如：所有关节物理对齐刻线）
# #input("确认机械臂已在零位，按回车继续")

# # 2️⃣ 设零点（写入电机）
# arm.set_zero_all()

# # 3️⃣ 建议重新 refresh / disable / enable
# arm.refresh_all()
# arm.disable_all()
# arm.enable_all()

# for m in arm.get_arm().get_motors():
#     print("pos:", m.get_position(), "tau:", m.get_torque())
