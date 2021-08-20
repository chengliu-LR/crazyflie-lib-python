# Notes for your crazyflie2.0

## 2021-Aug-19

- [x] Test tox with python3.6 succeeded on Linux, further test on macOS.

## 2021-Aug-20

解决了python版本问题，安装了`python3.6.5`后`TOXENV=py36 tox`出现bug，`examples/tuning/PID_controller_tuner.py`文件中添加`import tkinter as tk`后测试通过。

Already installed `crazyflie-clients-python` `crazyflie-lib-python` and `crazyflie-firmware` on both operating systems. cfclient can run very well on Linux.

Fixed the client USB connection problem (access denied, no sufficient permission). Checkout the [Platform notes udev permission notes](https://github.com/chengliu-LR/crazyflie-lib-python/blob/master/docs/installation/install.md) for more details.

**Remember: `/` is not the same dir as `~`.**

- [] Test cfclient and first flight on macOS.
