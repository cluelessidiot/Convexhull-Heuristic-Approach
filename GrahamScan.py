import sys
import numpy as np
import matplotlib.pyplot as plt

# Function to know if we have a CCW turn
def RightTurn(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return False
	return True
	
# Main algorithm:
def GrahamScan(P):
	print ("before sort")
	for i in range(7):
	   print (P[i])
	P.sort()
	print ("after sort")			# Sort the set of points
	for i in range(7):
	   print (P[i])
	print ("l upper")
	L_upper = [P[0], P[1]]		# Initialize upper part
	# Compute the upper part of the hull
	for i in range(2,len(P)):
		L_upper.append(P[i])
		#print (L_upper[0])
		while len(L_upper) > 2 and not RightTurn(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2]
	L_lower = [P[-1], P[-2]]	# Initialize the lower part
	# Compute the lower part of the hull
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not RightTurn(L_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
	del L_lower[0]
	
	del L_lower[-1]
	L = L_upper + L_lower		# Build the full hull
	return np.array(L)


def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
	
	# By default we build a random set of N points with coordinates in [0,300)x[0,300):
	P = [(np.random.randint(0,100),np.random.randint(0,100)) for i in range(N)]
	L = GrahamScan(P)
	P = np.array(P)
	plt.figure()
	plt.plot(L[:,0],L[:,1], 'b-', picker=5)
	plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-', picker=5)
	plt.plot(P[:,0],P[:,1],".r")
	plt.axis('on')
	plt.show()
#	for j in range(N):
#	  print (P[j])
	x_min_x=float('inf')
	x_max_x=float('-inf')
	y_min_y=float('inf')
	y_max_y=float('-inf')
	for q in range(N):
	  if P[q][0]>x_max_x:
	     x_max_x=P[q][0]
	     x_max_y=P[q][1]
	  if P[q][0]<x_min_x:
	     x_min_x=P[q][0]
	     x_min_y=P[q][1]
	  if P[q][1]>y_max_y:
	     y_max_y=P[q][1]
	     y_max_x=P[q][0]
	  if P[q][1]<y_min_y:
	     y_min_y=P[q][1]
	     y_min_x=P[q][0]      	  
	
	print (x_min_x,x_min_y)
	print (x_max_x,x_max_y)
	print (y_min_x,y_min_y)
	print (y_max_x,y_max_y)
	j=0
	#preprocessing rules
	for i in range(N):
		if (P[i][0]-x_min_x)*(x_min_y-y_min_y) > (P[i][1]-x_min_y)*(x_min_x-y_min_x) and  (P[i][0]-y_min_x)*(y_min_y-x_max_y) > (P[i][1]-y_min_y)*(y_min_x-x_max_x) and (P[i][0]-x_max_x)*(x_max_y-y_max_y) > (P[i][1]-x_max_y)*(x_max_x-y_max_x) and (P[i][0]-y_max_x)*(y_max_y-x_min_y) >(P[i][1]-y_max_y)*(y_max_x-x_min_x) :
		    print ("qw")
		else:
	             j=j+1	 

	A=[(0,0) for i in range(j)]
	j=0
	for i in range(N):
		if (P[i][0]-x_min_x)*(x_min_y-y_min_y) > (P[i][1]-x_min_y)*(x_min_x-y_min_x) and  (P[i][0]-y_min_x)*(y_min_y-x_max_y) > (P[i][1]-y_min_y)*(y_min_x-x_max_x) and (P[i][0]-x_max_x)*(x_max_y-y_max_y) > (P[i][1]-x_max_y)*(x_max_x-y_max_x) and(P[i][0]-y_max_x)*(y_max_y-x_min_y) > (P[i][1]-y_max_y)*(y_max_x-x_min_x) :
		    print (P[i])
		else:
	             A[j]=P[i][0],P[i][1]
	             j=j+1	     	  
      	# Plot the computed Convex Hull:
	print("Number of pints pre processed:")
	print (N-j)
#	for q in range (j):
#	      print (A[q])
	np.array(A)
	X=GrahamScan(A)
	A = np.array(A)
	#for q in range (j):
	 #     print (A[q])
	plt.figure()
	plt.plot(X[:,0],X[:,1], 'b-', picker=5)
	plt.plot([X[-1,0],X[0,0]],[X[-1,1],X[0,1]], 'b-', picker=5)
	plt.plot(A[:,0],A[:,1],".r")
	plt.axis('on')
	plt.show()

if __name__ == '__main__':
	main()
