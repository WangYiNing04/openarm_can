#可多个电机一起设置零点
import openarm_can as oa
import time
arm = oa.OpenArm("vcan0", False)
motor_types = [oa.MotorType.DM4310]
send_ids = [0x08]
recv_ids = [0x18]
arm.init_arm_motors(motor_types, send_ids, recv_ids)
for m in arm.get_arm().get_motors():
    print("pos:", m.get_position())
arm.enable_all()
# 1️⃣ 人工/程序把机械臂移动到“机械零位”
#    （例如：所有关节物理对齐刻线）

# 2️⃣ 设零点（写入电机）
arm.set_zero_all()

# 3️⃣ 建议重新 refresh / disable / enable
arm.refresh_all()
arm.disable_all()
arm.enable_all()

for m in arm.get_arm().get_motors():
    print("pos:", m.get_position())
