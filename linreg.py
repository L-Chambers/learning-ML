#--------------------------
# Linear Regression #1
#--------------------------

# A linear regression is algorithm used to predict a continuous set of values for given observations.
# The algorithm finds a slope m and an offset b for the equation y = mx + b
# The motivation is to find an m and b such that the overall margin of error between  measured and predicted targets is minimized.
# Let us consider ordinary least squares in the objective function S = summation(1,n) {(yMeasured - yPredicted)^2} provide a measure of a given line's accuracy. Smaller is better.
# There are several methods to find expressions for m and b that minimize S. 
# In this example convex optimization will be used to find these expressions. 


#
# calculates slope of linear regression
# X: vector of observations
# y: vector of corresponding targets
# y = mx + b
#
def _calculate_m(X, y):
	# find mean of X and y vectors
	x_avg = 0.0
	for x in X:
		x_avg += x
	y_avg = 0.0
	for y_i in y:
		y_avg += y_i
	x_avg /= len(X)
	y_avg /= len(y)
	
	# find m
	m = 0
	#numerator
	for i in range(0, len(X)):
		m += float(X[i]*y[i] - X[i]*y_avg)
	#den
	d = 0
	for i in range(0, len(X)):
		d += float (X[i]**2 - X[i]*x_avg)
	
	m /= d
	print("m is ", m)
	return m

#
# calculates y intercept of linear regression
# X: vector of observations
# y: vector of corresponding targets
# m: fitted slope
# y = mx + b
#
def _calculate_b(X, y, m):
	# find mean of X and y vectors
	x_avg = 0.0
	for x in X:
		x_avg += x
	y_avg = 0.0
	for y_i in y:
		y_avg += y_i
	x_avg /= len(X)
	y_avg /= len(y)
	print(x_avg)
	print(y_avg)
	print("b is ",  y_avg - (m * x_avg))
	return y_avg - (m * x_avg)


class LinearRegression:
	
	# class constructor
	def __init__(self):
		self.m = None
		self.b = None
	
	# 
	# fit the linear regression model
	#
	def fit(self, X, y):
		self.m = _calculate_m(X, y)
		self.b = _calculate_b(X, y, self.m)
		
	#
	# predict target values given input observations
	# assumes fit() already called
	#
	def predict(self, X):
		Y = [0] * len(X)
		for i in range(0, len(X)):
			Y[i] = self.m * X[i] + self.b
		return Y

def main():
	X = [1, 2, 3, 4, 5, 6, 7, 8]
	y = [2, 4, 6, 8, 10, 12, 14, 16]
	
	lr = LinearRegression()
	lr.fit(X, y)
	Yhat = lr.predict(X)
	print(Yhat)
	print(lr.predict([24]))

	
# entry point
if __name__ == "__main__":
	main() # call main function
	
	

# import and parse data set
# define expressions for m and b to fit the line using the input dataset
# use new set of data to predict targets
# graph results
# matplotlib
