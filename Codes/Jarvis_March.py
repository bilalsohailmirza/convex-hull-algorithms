import sys
import time
import csv
import numpy as np
import matplotlib.pyplot as plt



def WriteFile(data):
    header = ['Size', 'Time']

    with open('JarvisMarch.csv', 'a', encoding='UTF8') as f:
        
        writer = csv.writer(f)
        # write the header
        # writer.writerow(header)
        # write the data
        writer.writerow(data)

		
# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	
	return False

def plot_hulls(JarvisMarch, Points):
	
	plt.title("Jarvis March")
	plt.plot(JarvisMarch[:,0],JarvisMarch[:,1], '-', color='grey')   # Plot lines
	plt.plot(Points[:,0],Points[:,1],'.', color='white')              # Plot points
	plt.axis('auto')         # No axis
	plt.show(block=False)   # Close plot
	plt.pause(0.1)    # Small pause before closing plot

def JarvisMarch(Points):
	index = 0
	Points = list(Points)
	Points.sort(key = lambda x: x[1])	# Sort the set of points according to y-coordinate

	Points = np.array(Points)

	print("\nSorted List of Points: ")
	print(Points, end='\n\n')
	
	n = len(Points)
	FinalHull = [None] * n
	l = np.where(Points[:,1] == np.min(Points[:,1]))
	pointOnHull = Points[l[0][0]]
	i = 0
	while True:
		FinalHull[i] = pointOnHull
		endpoint = Points[0]
		for j in range(1,n):
			if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(Points[j],FinalHull[i],endpoint):
				endpoint = Points[j]
		i = i + 1
		pointOnHull = endpoint
		JarvisMarch = np.array([FinalHull[k] for k in range(n) if FinalHull[k] is not None])
		
		plot_hulls(JarvisMarch, Points)
		
		index += 1
		
		if endpoint[0] == FinalHull[0][0] and endpoint[1] == FinalHull[0][1]:
			break
		
	for i in range(n):
		if FinalHull[-1] is None:
			del FinalHull[-1]
	FinalHull = np.array(FinalHull)
	
	return FinalHull

def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
  
	
	Points = np.array([(np.random.randint(-1000,1000),np.random.randint(-1000,1000)) for i in range(N)])


	plt.figure(facecolor='darkgrey')
	axes = plt.axes()
	axes.set_facecolor('#2f3f3f')

	start = time.time()
	Final_Hull = JarvisMarch(Points)
	exec_time = time.time() - start

	WriteFile([N, exec_time])
	print("Execution Time: ", exec_time)
	# print("Points in the Hull:")
	# print(Final_Hull)
	
	# We use the predefined figure
	plt.title("Jarvis March")
	plt.plot(Points[:,0],Points[:,1],'.', color='white')
	plt.plot(Final_Hull[:,0],Final_Hull[:,1], '-', color='grey')
	plt.plot([Final_Hull[-1,0],Final_Hull[0,0]],[Final_Hull[-1,1],Final_Hull[0,1]], '-', color='grey')
	plt.axis('auto')
	plt.show()

if __name__ == '__main__':
	
	main()