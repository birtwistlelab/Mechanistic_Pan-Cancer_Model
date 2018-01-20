
# debugging tool

import csv
import sys

test1 = []
with open('test_ydot1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x = ', '.join(row)
        x = x.split(',')
        test1.append(float(x[0]))


test2 = []
with open('test_ydot4.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x = ', '.join(row)
        x = x.split(',')
        test2.append(float(x[0]))



accurate = 0
problem_indices = []
for i in range(len(test1)):
    if abs(test1[i] - test2[i]) < 0.0000000001:
        # print(to_return[i],correct_ydot[i])
        # print("good")
        # print(i)
        accurate = accurate+1
    else:
        # print(i)
        print(test1[i],test2[i])
        print("bad")
        print(i)
        print()
        problem_indices.append(i)


print(accurate/774)

print("number wrong: " + str(774-accurate))

print()
print(problem_indices)




sys.exit("done")







python = []
# with open('python_S_PARCDL.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         x = ', '.join(row)
#         x = x.split(',')
#         data.append(float(x[0]))




with open('python_v3.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         row = [float(x.strip()) for  x in row[0].split(',')]
         python.append(row)


# print(python)

matlab = []
with open('matlab_v2.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         row = [float(x.strip()) for  x in row[0].split(',')]
         matlab.append(row)






correct = 0
wrong = 0
for i in range(len(python)):
    for j in range(len(python[i])):


        # if abs(python[i][j] - matlab[i][j]) < 0.001:
        if str(python[i][j])[0:3] == str(matlab[i][j])[0:3]:


            correct = correct + 1
        else:
            print("FUCK!")
            print(i)
            print(j)
            print("python " + str(python[i][j]))
            print("matlab " + str(matlab[i][j]))
            print()
            wrong = wrong + 1


print()
print()
print("accuracy")
print(correct/len(python))
