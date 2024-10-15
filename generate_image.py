import csv
import ast
import numpy as np
# from PIL import Image

images = np.array()
labels = np.array()
with open('dataset_eye_on_off.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  i = 0 
  for lines in csvFile:
        if(i != 0):
            lines[1] = ast.literal_eval(lines[1])
            lines[1] = np.reshape(lines[1], (26, 34)).astype(np.uint8)
            # print(lines[1])
            # print(type(lines[1]))
            # image = Image.fromarray(lines[1])
            # image.save('gorseller/gorsel_' + str(i) + '.png')
        # print(len(lines))
        # print(lines)
        i += 1
        # if(i == 2):
        #     print(type(lines))
        #     break
  print(type(csvFile))
        