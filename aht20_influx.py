import time
import board
import busio
import adafruit_ahtx0

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "U6weeGnzUsmhiALh2pZl-1NmK6HishVa9IidtuL1o12MGC4HgKu23Iot_Ow5qFLH_kIG3Pd2ga_T1QKvFPM4NA=="
org = "home"
bucket = "environmental"

client = InfluxDBClient(url="http://es:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS) 


# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    temp_farenheight = sensor.temperature * (9/5) + 32
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Temperature: %0.1f F" % temp_farenheight)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    temp_point = Point("temperature")\
        .tag("location", "under_house_nw")\
        .field("celsius", sensor.temperature)\
        .time(datetime.utcnow(), WritePrecision.NS)
    humidity_point = Point("humidity")\
        .tag("location", "under_house_nw")\
        .field("percentage", sensor.relative_humidity)\
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, temp_point)
    write_api.write(bucket, org, humidity_point)
    time.sleep(2)
