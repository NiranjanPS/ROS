#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int64MultiArray, MultiArrayDimension, Int32MultiArray
import matplotlib.pyplot as plt
import numpy as np


class representer:
	def __init__(self):
		self.Sl_No_array = 0
		self.year = 1900
		self.heavy_vehicles = 0
		self.array_shape = []
		self.array = []
		self.data_array = []
		

	def callback(self,array):
		if array.data != None:
			self.array = array.data
			#print(self.array)
		#self.array = array.data
		#rospy.sleep(0.1)
		#print(self.array)
		#print('callback')
		#self.Sl_No_array = array.data[0]
		#self.year = array.data[1]
		#print(self.Sl_No_array)
		#print(self.year)

	def callback_shape(self,array_shape):
		#print(array_shape)
		if array_shape.data != None:
			self.array_shape = array_shape.data
			#print(self.array_shape)
		#rospy.sleep(0.1)
	
	def data_representer(self):
		self.subscriber_fn()
		#global Sl_No_array
		rospy.sleep(3)
		print('data_representer')
		#print(self.array)
		#print(np.array(self.array))
		#rospy.sleep(3)
		dummy = np.array(self.array)
		#print(dummy.shape)
		reshaped_data = (dummy.reshape(9,7))
		#print(reshaped_data)
		while not rospy.is_shutdown():
			key = self.take_input()
			if key == 'q':
				break
			else:
				self.plot_graph(key,reshaped_data)

	def plot_graph(self,key,reshaped_data):
		if key == 'p':
			self.pie_chart(reshaped_data)
		elif key == 'b':
			self.bar_chart(reshaped_data)
		elif key == 'l':
			self.line_graph(reshaped_data)
		else:
			print('ERROR Occured')
		
	def take_input(self):
		print('Select data representer you want:')
		print('p - Pie chart, b - bar graph, l - line graph, q - quit')
		key_list = ['p', 'P', 'b', 'B', 'l', 'L', 'q', 'Q']
		
		while True:
			key = raw_input()
			#print(key)
			if (key in key_list):
				return (key.lower())
				break
			else:
				print('Invalid graph selection, press one of the key below')
				print('p - Pie chart, b - bar graph, l - line graph, q - quit')

	def split_data(self):
		#global new_data
		counter = 0
		for row in range(0,self.array_shape[0]):
			self.data_array.append([])
			for column in range(0,self.array_shape[1]):
				self.data_array[row].append(self.array[counter])
				counter = counter + 1
		print('split data')
		#data_array = self.array.reshape(self.array_shape)
		#new_data = np.asarray(self.data_array)
		#print(new_data)
		#re = new_data.reshape(9,7)
		#print(type(new_data))
		#print(self.data_array)

	def pie_chart(self,data):
		labels = ['HV', 'LV', 'SMV', 'PCU']
		sizes = data[8,2:6]
		#print(self.data_array[8][2:6])
		#print(self.data_array[:,3])
		colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
		patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
		plt.legend(patches, labels, loc="upper left")
		#plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

		plt.axis('equal')
		plt.tight_layout()
		plt.show()
	
	def bar_chart(self,data):
		n_groups = 9

		HV = data[:,2]
		LV = data[:,3]
		SMV = data[:,4]
		PCU = data[:,5]
		# create plot
		fig, ax = plt.subplots()
		index = np.arange(n_groups)
		bar_width = 0.15
		opacity = 0.8

		rects2 = plt.bar(index + bar_width, HV, bar_width,
		alpha=opacity,
		color='g',
		label='Heavy Vehicles')
		rects2 = plt.bar(index + 2*bar_width, LV, bar_width,
		alpha=opacity,
		color='b',
		label='Light Vehicles')
		rects2 = plt.bar(index + 3*bar_width, SMV, bar_width,
		alpha=opacity,
		color='y',
		label='Slow Moving Vehicles')
		rects2 = plt.bar(index + 4*bar_width, PCU, bar_width,
		alpha=opacity,
		color='r',
		label='Passenger Cars')

		plt.xlabel('year')
		plt.ylabel('number of vehicles')
		plt.title('Traffic')
		plt.xticks(index + bar_width, ('1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010'))
		plt.legend(loc="upper left")
		plt.show()

	def line_graph(self,data):
		year = ['1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010']
		HV = data[:,2]
		LV = data[:,3]
		SMV = data[:,4]
		PCU = data[:,5]
		r = plt.plot(year, HV, color='g',label = 'Heavy Vehicles')
		r = plt.plot(year, LV, color='orange',label='Light Vehicles')
		r = plt.plot(year, SMV, color='r',label='Slow Moving Vehicles')
		r = plt.plot(year, PCU, color='y',label='Passenger Cars')
		plt.xlabel('year')
		plt.ylabel('number of vehicles')
		plt.legend(loc="upper left")
		plt.title('Traffic')
		#plt.axis('equal')
		plt.show()
		
	def subscriber_fn(self):
		rospy.Subscriber("Traffic_data", Int64MultiArray, self.callback)
		rospy.sleep(0.5)
		rospy.Subscriber('Array_shape', Int32MultiArray, self.callback_shape)
		rospy.sleep(0.5)
		#print('subscriber_fn')
	
	
	
if __name__=="__main__":
	representer_1 = representer()
	rospy.init_node('Traffic_data_representer', anonymous=False)
	#rospy.Subscriber("Traffic_data", Int64MultiArray, callback)
	
	try:
       		representer_1.data_representer()#start the logic
		rate = rospy.Rate(0.5) # 1hz
		rate.sleep()
		#rospy.spin()
		rate = rospy.Rate(0.5) # 1hz
		rate.sleep()
   	except rospy.ROSInterruptException:
        	pass
	finally:	
		print('END of representation')

