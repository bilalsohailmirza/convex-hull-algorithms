import sys
import time
import csv
import numpy as np
import matplotlib.pyplot as plt


def WriteFile(data):
    header = ['Size', 'Time']

    with open('GrahamScan.csv', 'a', encoding='UTF8') as f:
        
        writer = csv.writer(f)
        # write the header
        # writer.writerow(header)
        # write the data
        writer.writerow(data)

# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return False
	return True

def plot_hulls(L, Points):
	
	plt.plot(L[:,0],L[:,1], '-', color='grey')	# Plot lines
	plt.plot(Points[:,0],Points[:,1],".", color='white')		# Plot points
	plt.axis('auto')		# Manage axis
	plt.show(block=False)	# Closing plot otherwise new window pops up
	plt.pause(0.1)	# Small pause before closing plot

def GrahamScan(Points):

	Points.sort(key = lambda x: x[1])		# Sort the set of points according to y-coordinate
	Points = np.array(Points)			# Convert the list to numpy array

	Upper_Hull = [Points[0], Points[1]] # Initialize the upper part

	# Compute the upper part of the hull
	for i in range(2,len(Points)):
		Upper_Hull.append(Points[i])
		while len(Upper_Hull) > 2 and not CCW(Upper_Hull[-1],Upper_Hull[-2],Upper_Hull[-3]):
			del Upper_Hull[-2]
		Final_Hull = np.array(Upper_Hull)

	plot_hulls(Final_Hull, Points)
		

	Lower_Hull = [Points[-1], Points[-2]]	# Initialize the lower part

	# Compute the lower part of the hull
	for i in range(len(Points)-3,-1,-1):
		Lower_Hull.append(Points[i])
		while len(Lower_Hull) > 2 and not CCW(Lower_Hull[-1],Lower_Hull[-2],Lower_Hull[-3]):
			del Lower_Hull[-2]
		Final_Hull = np.array(Upper_Hull + Lower_Hull)

	plot_hulls(Final_Hull, Points)
		
	del Lower_Hull[0]
	del Lower_Hull[-1]

	Final_Hull = Upper_Hull + Lower_Hull 		# Build the full hull
	
	return np.array(Final_Hull)

def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
		
	Points = [(np.random.randint(-1000,1000),np.random.randint(-1000,1000)) for i in range(N)]

	# print("Generated Points: ")
	# for p in Points:
	# 	print(p)

	plt.figure(facecolor='darkgrey')
	axes = plt.axes()
	axes.set_facecolor('#2f3f3f')

	start = time.time()
	Final_Hull = GrahamScan(Points)
	exec_time = time.time() - start

	print("Execution Time: ", exec_time)

	WriteFile([N, exec_time])
	plt.axis('auto')
	plt.show()
	# print('Points on Final Hull')
	# print(Final_Hull)

if __name__ == '__main__':
  
  main()
