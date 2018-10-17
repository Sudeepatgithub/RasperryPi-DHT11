import random
import datetime
import threading
import Adafruit_DHT


def get_data():
    threading.Timer(5.0, get_data).start()  # Used for scheduling function calls, every 5 seconds
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) #GPIO4
    file = open("log.txt", "a")
    string = "{}\tHumidity = {} %; Temperature = {} C\n".format(datetime.datetime.now(), humidity, temperature)
    print(string)
    file.write(string)
    if temperature > 24:
        string = "{}\tIt is very Hot\n".format(datetime.datetime.now())
        print(string)
        file.write(string)
    if temperature < 18:
        string = "{}\tIt is Cold\n".format(datetime.datetime.now())
        print(string)
        file.write(string)
    if 30 <= humidity < 50:
        string = "{}\tHumidity is High\n".format(datetime.datetime.now())
        print(string)
        file.write(string)
    if 50 <= humidity <= 100:
        string = "{}\tHumidity is very High\n".format(datetime.datetime.now())
        print(string)
        file.write(string)
    file.close()


get_data()
