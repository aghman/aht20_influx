import time
import board
import busio
import adafruit_ahtx0

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    temp_farenheight = sensor.temperature * (9/5) + 32
    print("\nTemperature: %0.1f C, %0.1f" % sensor.temperature % temp_farenheight)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
