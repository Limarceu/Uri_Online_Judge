#Circle Area
def circle(radius):
	'''
Returns the circle area.
	parameters:
		radius (float) 
	returns:
		circle area (float)
	'''
	return 3.14159*radius**2

if __name__=='__main__':
	rad = float(input())
	print('A={0:.4f}'.format(circle(rad)))
