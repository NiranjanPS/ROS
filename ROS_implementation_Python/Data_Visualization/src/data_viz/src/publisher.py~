#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int64MultiArray, MultiArrayDimension, Int32MultiArray
from std_msgs.msg import MultiArrayLayout
import openpyxl as xl
import os
import numpy as np

rospy.init_node('Traffic_data_publisher', anonymous=False)
pub = rospy.Publisher('Traffic_data', Int64MultiArray, queue_size=10)
pub_array_shape = rospy.Publisher('Array_shape', Int32MultiArray, queue_size=10)

r = rospy.Rate(0.5) # 10hz
number = 0

cwd = os.getcwd()
print(cwd)
path = "/home/n/catkin_ws_1/src/data_viz/src" + "/Vehicles.xlsx"

wb_obj = xl.load_workbook(path,data_only = True)
sheet_obj = wb_obj['Sheet1']

array_shape = [9,7]
#cell_obj = 
def publish_data():
	cell_obj = []
	
	for row in range(3,12):
		
		for column in range(1,8):
			#cell_obj[row-3].append(0)
			#cell_obj.append(sheet_obj.cell(row = row, column = column).value)
			if sheet_obj.cell(row = row, column = column).value == None:
				cell_obj.append(0)
			else:
				cell_obj.append(sheet_obj.cell(row = row, column = column).value)

	publish_array_shape = Int32MultiArray(data=array_shape)
	pub_array_shape.publish(publish_array_shape)	
	r.sleep()
	
	publish_array = Int64MultiArray(data=cell_obj)
	pub.publish(publish_array)

	#print(type(np.array(publish_array.data)))
	#print(array_shape)
		
		#pub.publish('New',3)

while not rospy.is_shutdown():
	publish_data()
	r.sleep()
