import psutil
# import GPUtil
# import datetime
# from cpuinfo import get_cpu_info
# from gpiozero import CPUTemperature
# import time
# import matplotlib
#
# gpus = GPUtil.getGPUs()
#
# import wmi
#
# w = wmi.WMI(namespace="root\OpenHardwareMonitor")
# temperature_infos = w.Sensor()
# for sensor in temperature_infos:
#     if sensor.SensorType == u'Temperature':
#         print(sensor.Name)
#         print(sensor.Value)
#
# print(gpus[0].load * 100)
# print(gpus[0].driver)
# print(str(get_cpu_info()['brand_raw']))
# print(datetime.time.hour)
# print(CPUTemperature())

import matplotlib.pyplot as plt
import numpy as np

print(str(dict(psutil.virtual_memory()._asdict())['total']))