import math

# Training Data Set.
D=[(170, 57, 32, 'W'), (192, 95, 28, 'M'), (150, 45, 30, 'W'), (170, 65, 29, 'M'), (175, 78, 35, 'M'), (185, 90, 32, 'M'), (170, 65, 28, 'W'), (155, 48, 31, 'W'), (160, 55, 30, 'W'), (182, 80, 30, 'M'), (175, 69, 28, 'W'), (180, 80, 27, 'M'), (160, 50, 31, 'W'), (175, 72, 30, 'M')]

# Identify the classes 
classList = []
l = len(D)
for i in range(l):
    if D[i][3] not in classList:
        classList.append(D[i][3])

# Calculate the difference for the variance 
def difference(a, b):
        return a-b

while True:
        type = int(raw_input("\nPlease input 1 for prediction WITH Age Parameter OR 2 for prediction WITHOUT Age Parameter OR -1 to Exit the program\n"))
        
        if type == '-1':
                break
        elif type == 1:
                r = 3
        else:
                r = 2 

        while True:
                # Take the input Data point from the user.
                input = raw_input("\nPlease input a data point for the prediction as: height weight age OR -1 to check with different training data \n")
                if input == '-1':
                        break
                
                inputPoint = map(int, input.split())

                # Sort the Training data sets based on classes 
                classM =[]
                classW =[]
                for i in range(l):
                        if D[i][3] == 'M':
                                classM.append(D[i])
                        elif D[i][3] == 'W':
                                classW.append(D[i])
                sampleM = len(classM) - 1
                sampleW = len(classW) - 1

                varianceM =[]
                varianceW =[]
                meanM =[]
                meanW =[]
                m = []
                w = []

                for e in range(r):

                        # Calculate the Mean of the parameters for classM
                        mM = float(sum([height[e] for height in classM]))/len(classM)
                        meanM.append(mM)

                        mW = float(sum([height[e] for height in classW]))/len(classW)
                        meanW.append(mW)
                        
                        # Calculate the variance of the parameters for classM                       
                        varM = sum((difference(i[e], meanM[e])**2) for i in classM)/sampleM
                        varianceM.append(varM)
                        
                        # Calculate the variance of the parameters for classW
                        varW = sum((difference(i[e], meanW[e])**2) for i in classW)/sampleW
                        varianceW.append(varW)  
                        
                        # #calculate Standrard Deviation of the parameter 
                        # stdM = [math.sqrt(varianceM[0]), math.sqrt(varianceM[1]), math.sqrt(varianceM[2])]
                        # stdW = [math.sqrt(varianceW[0]), math.sqrt(varianceW[1]), math.sqrt(varianceW[2])]

                        # Probality that input parameter given Male
                        p = math.exp(-1 * (( inputPoint[e] - meanM[e])**2) / (2*varianceM[e])) / (math.sqrt(2*math.pi*varianceM[e]))
                        m.append(p)
                        
                        # Probality that input parameter given Women
                        q = math.exp(-1 * (( inputPoint[e] - meanW[e])**2) / (2*varianceW[e])) / (math.sqrt(2*math.pi*varianceW[e]))
                        w.append(q)

                # Printing the intermediate Parameters. 
                print "\nThe Mean of the Male parameters"
                print meanM

                print "\nThe Mean of the Women parameters"
                print meanW

                print "\nThe Variance of the Male parameters"
                print varianceM

                print "\nThe Variance of the Women parameters"
                print varianceW
                        
                if type == 1:
                        print "\nP[ height/Male, weight/Male, age/Male] = ", m, '\n'
                        print "\nP[ height/Women, weight/Women, age/Women] = ", w, '\n'
                else:
                        print "\nP[ height/Male, weight/Male] = ", m, '\n'
                        print "\nP[ height/Women, weight/Women] = ", w,'\n'

                # Probalities of the classes 
                probM = float(len(classM))/l
                probW = float(len(classW))/l

                print "Probality of Male class ", probM,'\n', "probality of Women class", probW, '\n'

                probInputPointgivenMale = reduce((lambda x, y: x * y), m) * probM 
                probInputPointgivenWomen = reduce((lambda x, y: x * y), w) * probW

                if probInputPointgivenMale > probInputPointgivenWomen:
                        print "\nThe Person is Male"
                else:
                        print "\nThe Person is Women"
        


