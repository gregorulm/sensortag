# SensorTag: Marathon Test (Testbed)
# Gregor Ulm, Chalmers University of Technology (2017);
#             Dept. of Computer Science and Engineering,
#             Distributed Computing and Systems Research Group 
# Project: Big Data Processing in Smart Buildings 
#
# This program was used to empirically determine how long the batteries
# in Texas Instruments SensorTags last in the scenario we envisioned
# for large-scale data collection.


import time
from datetime import date

# external library (bluepy)
import sensortag


def measure(tags, startTime, interval):

	FILENAME = 'outputSensorTag.txt'
	#TIMESTAMP = date.today().ctime()

	f = open(str(interval) + "_" + FILENAME, 'w')

	f.write( "Interval: " + str(interval) + "\n")	
		
    #five_min = 5 * 60
	#endTime  = startTime + five_min
	
	t       = time.time()
	
#	while t < endTime:
	while True:

		tag[0].waitForNotifications(interval)		
		
		# now poll values from all sensor tags
		for tag in tags:
		
			#x = tag.battery.read()
				
			(x, y, z) = tag.gyroscope.read()
			(a, b, c) = tag.accelerometer.read()
	
			#print "gyro:", x, y, z, "accel:", a, b, c
			line = tag + ":" \
			       + "Gyro,"   + str(x) + "," + str(y) + "," + str(z) \
			       + ",Accel," + str(a) + "," + str(b) + "," + str(c)
	
		f.write( line + "\n")	
		f.flush()
		#t = time.time()


	f.close()
	# program crashes when SensorTag battery has run out
	


def main():
	
	# TODO: change the tags to the actual device addresses 
	#       (you can get the addresses, for instance, via the tool
	#       "Bluetooth Devices")
	addresses = ['B0:B4:48:BF:DD:81', 'B0:B4:48:BF:DD:81',
	             'B0:B4:48:BF:DD:81', 'B0:B4:48:BF:DD:81']
	
	tags = []
	for address in addresses:
	
		tag = sensortag.SensorTag(address)

		tag.gyroscope.enable()
		tag.accelerometer.enable()
		
		# tag.battery.enable()
 	    # x = tag.battery.read()
		# print x
		
		tags.append(tag)

		#raw_input("Press Enter when ready.")
	
		#time.sleep(10.0)
	
	interval = 0.7
	
	startTime = time.time() # second since epoch
	measure(tags, startTime, interval)

	for tag in tags:
		tag.disconnect()


main()
