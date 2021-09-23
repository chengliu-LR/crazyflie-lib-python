# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2016 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.
"""
This demo shows how to connect to your Crazyflie through the
Crazyflie python library and basic of logging and parameters.
Change the URI variable to your Crazyflie configuration.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.utils import uri_helper

# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7EC')

logging.basicConfig(level=logging.ERROR)


# sync log
def simple_log_sync(scf, logconf):
    with SyncLogger(scf, log_stab) as logger:
        for log_entry in logger:
            timestamp = log_entry[0]
            data = log_entry[1]
            logconf_name = log_entry[2]
            print('[{}][{}]: {}'.format(timestamp, logconf_name, data))


# async log working with call_back
def simple_log_async(scf, logconf):
    cf = scf.cf
    cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_stab_callback)
    logconf.start()
    time.sleep(5)
    logconf.stop()


# async log call back function
def log_stab_callback(timestamp, data, logconf):
    print('[{}][{}]: {}'.format(timestamp, logconf.name, data))


# async param
def simple_param_async(scf, groupstr, namestr):
    cf = scf.cf
    full_name = groupstr + '.' + namestr
    cf.param.add_update_callback(group=groupstr, name=namestr, cb=param_stab_est_callback)

    time.sleep(1)
    cf.param.set_value(full_name, 3)
    time.sleep(1)
    cf.param.set_value(full_name, 1)
    time.sleep(1)


# async param call back
def param_stab_est_callback(complete_name, value):
    print('The crazyflie has parameter ' + complete_name + ' set at number: ' + value)


if __name__ == '__main__':
    cflib.crtp.init_drivers()
    log_stab = LogConfig(name='Stabilizer', period_in_ms=200)
    log_stab.add_variable('stabilizer.roll', 'float')
    log_stab.add_variable('stabilizer.pitch', 'float')
    log_stab.add_variable('stabilizer.yaw', 'float')

    group = 'stabilizer'
    name = 'estimator'

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        #simple_log_sync(scf, log_stab)
        #simple_log_async(scf, log_stab)
        simple_param_async(scf, group, name)
