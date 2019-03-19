import csv
from collections import OrderedDict
import csdparcel
import csdbeacon
import turtle

def replace_all(text, dic):
	"""Replace text strings using values from an OrderedDict.
	
	arrguments:
	text -- text string 
	dic -- an OrderedDict representing the keys and values 
	
	Returns:
	Text with the replaced words
	"""
	for i, j in dic.items():
		text = text.replace(i, j)
	return text

"""Convert the Surveyor 4 'Finalize Job' output into a csv file"""
# Create OrderedDict for the replace_all function.
c = ","
od = OrderedDict([("      ",c), ("    ",c), ("  ",c), (" ",c)])

#Prompt user for S4 file. Enter either full path or relative path.

a = []
data = []
with open(input("Please insert the path of the S4 file: "), 'r', newline='') as f:
	for line in f:
		a.append(replace_all(line, od))
	for line in a:
		data.append(line.split(','))


parcels = []
beacons = []
for line in data:
	if len(line) == 7:
		beacon = csdbeacon.Beacon(beacon_no=line[1],easting=line[2], northing=line[3])
		beacons.append(beacon)
		print(beacon.beacon_no)
	elif len(line) == 2:
		if len(line[1]) == 9:
			parcel = csdparcel.Parcel(parcel_no=line[1])
			print("parcel no. is: " + str(parcel.parcel_no))
			parcels.append(parcel)
		elif len(line[1]) > 9:
			parcel.plot_string.append(line[1])
print(parcels[0].plot_string)
for line in data:
	print("length of line is: " + str(len(line)))
	for element in line:
		print("length of element is: " + str(len(element)))