# aht20_influx
Python script to repeatedly read from an AHT20 sensor and save the temperature and humidity data to a configured InfluxDB instance

## Setup

### Turn on SPI and I2C
```
sudo raspi-config
```
Select "Interface Options" and select I2C and SPI, enabling each. Back out and finish. 

### Install python dependencies
```
make deps
```
