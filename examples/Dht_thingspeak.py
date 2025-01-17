"""
dht11_thingspeak.py

Temperature/Humidity monitor using Raspberry Pi and DHT11.
Data is displayed at thingspeak.com

Author: fasil.kv
"""
import sys
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
def getSensorData():
    RH, T = Adafruit_DHT.read_retry(11, 4)
    RH, T = 50,50
    # return dict
    return (str(RH), str(T))

# main() function
def main():
    # use sys.argv if needed
    if len(sys.argv) < 2:
        print('Usage: python tstest.py PRIVATE_KEY')
        exit(0)
    print('starting...')

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % sys.argv[1]

    while True:
        try:
            RH, T = getSensorData()
            f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (RH, T))
            print(f.read())
            f.close()
            sleep(15)
        except:
            print('exiting.')
            break

# call main
if __name__ == '__main__':
    main()
