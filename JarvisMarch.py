import sys
import numpy as np
import matplotlib.pyplot as plt

# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	return False

# Main function:
def GiftWrapping(S):
	n = len(S)
	P = [None] * n
	l = np.where(S[:,0] == np.min(S[:,0]))
	#print (S[l[0][0]])
	pointOnHull = S[l[0][0]]
	i = 0
	while True:
		P[i] = pointOnHull
		endpoint = S[0]
		for j in range(1,n):
			if (endpoint[0] == pointOnHull[0] and endpoint[1] == pointOnHull[1]) or not CCW(S[j],P[i],endpoint):
				endpoint = S[j]
		i = i + 1
		pointOnHull = endpoint
		if endpoint[0] == P[0][0] and endpoint[1] == P[0][1]:
			break
	P=list(filter(None.__ne__,P))
	return np.array(P)

def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
	
	# By default we build a random set of N points with coordinates in [0,300)x[0,300):
	P = np.array([(np.random.randint(0,300),np.random.randint(0,300)) for i in range(N)])
	#L = GiftWrapping(P)
	
	# Plot the computed Convex Hull:
	#plt.figure()
	#plt.plot(L[:,0],L[:,1], 'b-', picker=5)
	#plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-', picker=5)
	#plt.plot(P[:,0],P[:,1],".r")
	#plt.axis('off')
	#plt.show()
	######################################################################33
	for j in range(N):
	  print (P[j])
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
	for i in range(N):
		if (P[i][0]-x_min_x)*(x_min_y-y_min_y) > (P[i][1]-x_min_y)*(x_min_x-y_min_x) and  (P[i][0]-y_min_x)*(y_min_y-x_max_y) > (P[i][1]-y_min_y)*(y_min_x-x_max_x) and (P[i][0]-x_max_x)*(x_max_y-y_max_y) > (P[i][1]-x_max_y)*(x_max_x-y_max_x) and (P[i][0]-y_max_x)*(y_max_y-x_min_y) >(P[i][1]-y_max_y)*(y_max_x-x_min_x) :
		    #print (P[i])
		    print ("EXCLUDING  point")
		else:
	             j=j+1	 

	A=[(0,0) for i in range(j)]
	j=0
	for i in range(N):
		if (P[i][0]-x_min_x)*(x_min_y-y_min_y) > (P[i][1]-x_min_y)*(x_min_x-y_min_x) and  (P[i][0]-y_min_x)*(y_min_y-x_max_y) > (P[i][1]-y_min_y)*(y_min_x-x_max_x) and (P[i][0]-x_max_x)*(x_max_y-y_max_y) > (P[i][1]-x_max_y)*(x_max_x-y_max_x) and(P[i][0]-y_max_x)*(y_max_y-x_min_y) > (P[i][1]-y_max_y)*(y_max_x-x_min_x) :
		    print (P[i])
		   # print ("qw")
		else:
	             A[j]=P[i][0],P[i][1]
	             j=j+1	     	  
       
	# Plot the computed Convex Hull:
	print("Number of points pre processed:")
	print (N-j)
#	for q in range (j):
#	      print (A[q])
	A=np.array(A)
	X=GiftWrapping(A)
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
