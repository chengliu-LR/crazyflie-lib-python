# Notes for your crazyflie2.0

## 2021-Aug-19

test tox with python3.6 succeeded on Linux, further test on macOS.

## 2021-Aug-20

解决了python版本问题，安装了`python3.6.5`后`TOXENV=py36 tox`出现bug，`examples/tuning/PID_controller_tuner.py`文件中添加`import tkinter as tk`后测试通过。
