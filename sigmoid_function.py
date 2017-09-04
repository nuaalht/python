import numpy as np
import time
def sigmoid(z):
    """compute the sigmoid of z
    return s = sigmoid(z)
    """
    s = 1./(1. + np.exp(-z))

    return s

print("sigmoid(0) = ", str(sigmoid(0)))
print("sigmoid(1) = ", str(sigmoid(1)))
print("sigmoid(100) = ", str(sigmoid(100)))
x = np.array([1,2,3])
y = sigmoid(x).reshape(3,1) # vetormize calaulation
print("y = ", y)
print(y.shape)

def sigmoid_derivative(z):
    """calculate the derivative
    value of sigmoid function
    """
    s = 1./(1. + np.exp(-z))
    ds = s * (1 - s)
    return ds

a = np.array([1,2,3])
b = sigmoid_derivative(a).reshape(3,1)
print("b = ", b)
print(b.shape)
test = "hello world!"
print("test: " + test)

image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

print(image.shape[0], image.shape[1], image.shape[2])

def image2vector(image):

    """
    image : a number of array of shape(length, width, depth)

    return: a vector of shape(length*height*depth,1)
    """
    v = image.reshape(image.shape[0]*image.shape[1]*image.shape[2],1)
    return v

print("image2vector(image) = ", image2vector(image))
print("image reshape = " + str(image2vector(image)))

x = np.array([[0,3,4],[1,6,4]])
def normalizerows(x):
    """
    implement a fuction that normalizes each row of the matrix(to have unit length)

    Argument:
    x--A numpy matrix of shape(n,m)
    """
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord=2, axis= ..., keepdims=True)
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)

    #Divide x by norm
    x = x / x_norm

    return x
print(np.linalg.norm(x, ord=2, axis=1, keepdims=True))
print("normalizeRows(x) = " + str(normalizerows(x)))

def softmax(x):
    """
    Calculats the softmax for each row of input

    Argument:
    x -- A numpy matrix of shape(n,m)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape(n,m)
    """
    x_exp = np.exp(x)

    x_sum = np.sum(x_exp, axis=1, keepdims=True)

    s = x_exp/x_sum

    return s
print("softmax(x) = " + str(softmax(x)))

# vectorization
x1 = [9,2,5,0,0,7,5,0,0,0,9,2,5,0,0]
x2 = [9,2,2,9,0,9,2,5,0,0,9,2,5,0,0]

tic = time.process_time()
print("tic = ",tic)
dot = 0
for i in range(len(x1)):
    dot += x1[i]*x2[i]
toc = time.process_time()
print("toc = ",toc)
print("dot="+str(dot)+"\n-----Compution time ="+str(1000*(toc-tic))+"ms")

tic = time.process_time()
outer = np.zeros((len(x1), len(x2)))  # we create a len(x1)*len(x2) matrix with only zeros
for i in range(len(x1)):
    for j in range(len(x2)):
        outer[i,j] = x1[i]*x2[j]
toc = time.process_time()
print("outer="+str(outer)+"\n----Computation time = " + str(1000*(toc - tic)) + "ms")

tic = time.process_time()
mul = np.zeros(len(x1))
for i in range(len(x1)):
    mul[i] = x1[i]*x2[i]
toc = time.process_time()
print("elementwise multiplication="+str(mul)+"\n----Computation time="+str(1000*(toc - tic)) +"ms")

W = np.random.rand(3,len(x1)) # Random 3*len(x1) numpy array
tic = time.process_time()
gdot = np.zeros(W.shape[0])
for i in range(W.shape[0]):
    for j in range(len(x1)):
        gdot[i] += W[i,j]*x1[j]
toc = time.process_time()
print("gdot="+str(gdot)+"\n-----Computation time" + str(1000*(toc - tic)) + "ms")

x1 = [9,2,5,0,0,7,5,0,0,0,9,2,5,0,0]
x2 = [9,2,2,9,0,9,2,5,0,0,9,2,5,0,0]

tic = time.process_time()
dot = np.dot(x1, x2) # 内积
toc = time.process_time()
print("dot="+str(dot)+"\n-----Computation time="+str(1000*(toc - tic))+"ms")

tic = time.process_time()
outer = np.outer(x1, x2) # 外积
toc = time.process_time()
print("outer="+str(outer)+"\n----Computation time="+str(1000*(toc - tic))+"ms")

tic = time.process_time()
mul = np.multiply(x1, x2) # 乘法
toc = time.process_time()
print("elementwise multiplication="+str(mul)+"\n----Computation time="+str(1000*(toc - tic))+"ms")

print("W = ",W)
tic = time.process_time()
dot = np.dot(W,x1)
toc = time.process_time()
print("gdot="+str(dot)+"\n----Computation time"+str(1000*(toc - tic))+"ms")

# implement the L1 and L2 loss function
# the bigger your loss is, the more different your prediction yhat are from the y
def L1(yhat,y):
    """
    Arguments:
    yhat ----vector of size m(predicted labels)
    y    ----vector of size m(true labels)
    Returns:
    loss -----the value of the L1 loss function defined above

    """
    loss = np.sum(np.abs(yhat - y))
    return loss
yhat = np.array([0.9, 0.2, 0.1, 0.4, 0.9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = "+str(L1(yhat,y)))

def L2(yhat, y):
    """
    :param yhat: vector of size m (predicted labels)
    :param y: vector of size m (true labels)
    :return: loss --- the value of L2 loss function defined above
    """
    loss = np.dot(yhat-y, yhat-y)
    return loss
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 1, 1, 1])
print("L2 = "+str(L2(yhat,y)))

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2],[3,4],[5,6]])
print(np.dot(a, b).shape)