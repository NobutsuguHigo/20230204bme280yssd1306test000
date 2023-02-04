BME280.Address(BME280_I2C_ADDRESS.ADDR_0x76)
BME280.PowerOn()
MuseOLED.init()
MuseOLED.writeStringNewLine("Hello World!")
loops.everyInterval(2000, function () {
    MuseOLED.clear()
    MuseOLED.writeStringNewLine("Temp:" + BME280.temperature(BME280_T.T_C) + " Deg")
    MuseOLED.writeStringNewLine("Hum:" + BME280.humidity() + " %")
    MuseOLED.writeStringNewLine("Pa:" + BME280.pressure(BME280_P.hPa) + " hPa")
})
basic.forever(function () {
	
})
