BME280.address(BME280_I2C_ADDRESS.ADDR_0X76)
BME280.power_on()
MuseOLED.init()
MuseOLED.write_string_new_line("Hello World!")

def on_every_interval():
    MuseOLED.write_string("Temp:" + str(BME280.temperature(BME280_T.T_C)) + "Deg")
    MuseOLED.write_string_new_line("Hum:" + str(BME280.humidity()) + "%")
    MuseOLED.write_string_new_line("Pa:" + str(BME280.pressure(BME280_P.H_PA)) + "hPa")
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
