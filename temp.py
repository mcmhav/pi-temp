from datetime import datetime
from sense_hat import SenseHat
import psutil

sense = SenseHat()

# epoch, temp, temp_hum, temp_pres, pressure, humidity, temp_calibrated, cpu_tmp
epoch = int(datetime.now().timestamp() * 1000)
temp = sense.get_temperature()
temp_hum = sense.get_temperature_from_humidity()
temp_pres = sense.get_temperature_from_pressure()
pressure = sense.get_pressure()
humidity = sense.get_humidity()
temp_calibrated = ''

psutil_temp = psutil.sensors_temperatures()

cpu_tmp = ''
for key in psutil_temp.keys():
    if key.startswith('cpu') and key.endswith('thermal'):
        cpu_tmp = psutil.sensors_temperatures()[key][0].current

cpu_tmp = '41.16'

def zero_to_empty_string(value):
    return value if value != 0 else ''

temp = zero_to_empty_string(temp)
temp_hum = zero_to_empty_string(temp_hum)
temp_pres = zero_to_empty_string(temp_pres)
pressure = zero_to_empty_string(pressure)
humidity = zero_to_empty_string(humidity)

print(f'{epoch},{temp},{temp_hum},{temp_pres},{pressure},{humidity},{temp_calibrated},{cpu_tmp}')
