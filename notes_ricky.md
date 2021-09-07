# Notes for your Crazyflie2.X

## 2021-Aug-20

解决了python版本问题，安装了`python3.6.5`后`TOXENV=py36 tox`出现bug，`examples/tuning/PID_controller_tuner.py`文件中添加`import tkinter as tk`后测试通过。

Already installed `crazyflie-clients-python` `crazyflie-lib-python` and `crazyflie-firmware` on both operating systems. cfclient can run very well on Linux.

Fixed the client USB connection problem (access denied, no sufficient permission). Checkout the [Platform notes udev permission notes](https://github.com/chengliu-LR/crazyflie-lib-python/blob/master/docs/installation/install.md) for more details.

**Remember: `/` is not the same dir as `~`.**

- [x] Test cfclient and first flight on macOS (2021-Aug-23)

## 2021-Aug-19

- [x] Test tox with python3.6 succeeded on Linux, further test on macOS

---

## Development with Crazyflie2.X on macOS

### 1. Install `cflib`

- Clone the cflib

```shell
git clone git@github.com:chengliu-LR/crazyflie-lib-python.git
```

- Install the cflib in editable mode

```shell
pip3 install -e <path/to/cflib>
```

- Uninstall the cflib if you don't want it any more

```shell
pip3 uninstall cflib
```

### 2. Building and Flashing

#### Install a toolchain on macOS

```shell
brew tap PX4/homebrew-px4
brew install gcc-arm-none-eabi
```

Make sure you have the right compiler by entering the following command to show the dir of gcc-arm-none-eabi compiler

```shell
$ which arm-none-eabi-gcc
/usr/local/bin/arm-none-eabi-gcc
```

#### Cloning

This repo uses git submodules. Clone with the `--recursive` flag

```shell
git clone --recursive https://github.com/bitcraze/crazyflie-firmware.git
```

If you already have cloned the repo without the `--recursive` option, you need to get the submodules manually

```shell
cd crazyflie-firmware
git submodule init
git submodule update
```

#### Compiling

Using `-j` flag to enable multicore compiling to accelerate the compiling process

```shell
make -j
```

You should see something like this on a successful build

```shell
$ make
  CLEAN_VERSION
  CC    sensors_mpu9250_lps25h.o
  CC    sensors_bmi088_bmp388.o
  CC    main.o
  CC    nvic.o
  CC    led.o
  CC    usblink.o
  CC    ledseq.o
  CC    freeRTOSdebug.o
  CC    pm_stm32f4.o
  CC    radiolink.o
  CC    system.o
  CC    usddeck.o
  CC    cfassert.o
  VTMPL version.c
  CC    version.o
  LD    cf2.elf
  COPY  cf2.hex
  COPY  cf2.bin
  DFUse cf2.dfu
Build for the CF2 platform!
Build 11:0864ef92245a (2021.03 +11) MODIFIED
Version extracted from git
Crazyloader build!
Flash |  242184/1032192 (23%),  790008 free | text: 236372, data: 5812, ccmdata: 0
RAM   |   71128/131072  (54%),   59944 free | bss: 65316, data: 5812
CCM   |   58380/65536   (89%),    7156 free | ccmbss: 58380, ccmdata: 0
```

#### Flashing

Writing a new binary to the Crazyflie is called flashing (writing to the flash memory).

##### Prerequisites

- A Crazyradio with drivers isntalled
- `crazyflie-clients-python` placed on the same directory level in the file tree
- The firmware has been built
- The current woking directory is the root if the crazyflie-firmware project

##### Manually entering bootloader mdoe

- Turn the Crazyflie off
- Start the Crazyflie in the *bootloader mode* by **pressing the power button for 3 seconds**. Both the blue LEDs will blink
- In your terminal run `make cload` it will printouts in the “Console” window shows the progress and the LEDs on the Crazyflie flicker

```shell
$ make cload
python3 -m cfloader  flash  cf2.bin stm32-fw
Restart the Crazyflie you want to bootload in the next
 10 seconds ...
 done!
Connected to bootloader on Crazyflie 2.0 (version=0x10)
Target info: nrf51 (0xFE)
Flash pages: 232 | Page size: 1024 | Buffer pages: 1 | Start page: 88
144 KBytes of flash available for firmware image.
Target info: stm32 (0xFF)
Flash pages: 1024 | Page size: 1024 | Buffer pages: 10 | Start page: 16
1008 KBytes of flash available for firmware image.
Flashing 1 of 1 to stm32 (fw): 242639 bytes (237 pages) ..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10..........10.......7
Reset in firmware mode ...
```

> Warning! If multiple Crazyflies within range are in bootloader mode the result is unpredictable.

### 3. Interact with `cfclient`

#### Install crazyradio drivers

`libusb` is a library for USB device access from Linux, macOS, etc. It is written n C and licensed udner the GNU Lesser General Public License version 2.1.

```shell
brew install libusb
```

#### Install with `pip`

```shell
pip3 install cfclient
```
