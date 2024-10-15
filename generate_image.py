import csv
import ast
import numpy as np
# from PIL import Image

images = np.empty((0, 26, 34))
labels = np.empty((0, 1))
with open('dataset_eye_on_off.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  i = 0 
  for lines in csvFile:
        if(i != 0):
            image = ast.literal_eval(lines[1])
            image = np.reshape(image, (26, 34)).astype(np.uint8)
            images = x = np.append(images, [image], axis=0)

            label = lines[0]
            if label == 'open':
              labels = np.append(labels, [1])
            else:
              labels = np.append(labels, [0])
                
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
  # print(type(csvFile))
print(type(images))
print(images.shape)

print(images[0])

print(type(labels))
print(labels.shape)

print(labels[0])

print(labels[2873])
  
        