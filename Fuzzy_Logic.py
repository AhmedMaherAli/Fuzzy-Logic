from Variable import Variable
from Inference import Inference
from Shape import Shape


def to_points(x):
    l = len(x)
    points = [[z, 0] if z == x[0] or z == x[l - 1] else [z, 1] for z in x]
    return points


def addShape(shapes):
    name, shape_type = input().split(' ')
    points = [float(x) for x in input().split(' ')]
    points = to_points(points)
    shapes[name] = Shape(name, points)
    return shapes


""" 
   if shape_type == 'triangle':
        shapes[name] = (Triangle(name, points))
    else:
        shapes[name] =(Trapezoidal(name, points))
    return shapes
"""

numberOfVariables = int(input("Enter Number Of Variable:"))
variables = {}

print("---------------------------------")
print("Fuzzification:")
for i in range(numberOfVariables):
    shapes = {}
    varName, varValue = input().split(' ')
    varValue = float(varValue)
    numOfSets = int(input())
    for j in range(numOfSets):
        addShape(shapes)
    var = Variable(varName, shapes, varValue)
    var.fuzzify()
    print("membership for var '" + varName + "' : ")
    print(var.memberships)
    variables[varName] = var

# take output variable
outputVarName = input()
outShapes = {}
for i in range(int(input())):
    addShape(outShapes)
outputVariavble = Variable(outputVarName, outShapes)

print("-----------------------------------")
print("Inference Rules outputs:")
inference = Inference(variables)
rulesOut = []
for i in range(int(input())):
    tupl = inference.doInference(input())
    rulesOut.append(tupl)
    print("Rule " + str(i + 1) + ": " + str(tupl))

print("-----------------------------------")
print("Defuzzification:")

sumValues = 0
sumVales_shapes = 0
for val_shape in rulesOut:
    print (val_shape[1])
    print (outputVariavble.shapes[val_shape[1]])
    centroid = outputVariavble.shapes[val_shape[1]].calculate_centroid()
    print(centroid)
    sumVales_shapes += centroid * val_shape[0]
    sumValues += val_shape[0]
    print("value of shape '" + val_shape[1] + "' = " + str(centroid))

print("\nPrediction of '%s': %s" % (outputVariavble.name, str(sumVales_shapes / sumValues)))
