import csv
import ast
import numpy as np
from sklearn.model_selection import train_test_split

# from PIL import Image

images = np.empty((0, 26, 34), dtype=np.uint8)
labels = np.empty((0), dtype=np.uint8)
with open('dataset_eye_on_off.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  i = 0 
  lineSize = 884
  for lines in csvFile:
        if(i != 0):
            
            image = ast.literal_eval(lines[1])
            if(lineSize != len(image)):
               print("line satır %s, size: %f", str(i),len(image))
            
            has_none = np.any(image == None)
            if has_none:
               print("none satır %s, size: %f", str(i),len(image))
            image = np.reshape(image, (26, 34)).astype(np.uint8)  
            
            images = x = np.append(images, [image], axis=0)

            label = lines[0]
            if label == 'open':
              labels = np.append(labels, 1)
            else:
              labels = np.append(labels, 0)
                
            # print(lines[1])
            # print(type(lines[1]))
            # image = Image.fromarray(lines[1])
            # image.save('gorseller/gorsel_' + str(i) + '.png')
        # print(len(lines))
        # print(lines)
        i += 1
        # if(i == 2):
        #     print(lines[1])
        #     print(type(lines[1]))
        #     break
  # print(type(csvFile))
# images = images.reshape((2874, 26, 34, 1))
print(type(images))

print(images[0])

print(type(labels))

print(labels[0])

# print(labels[2873])
  
print(labels)
print(images.shape)
print(labels.shape)

# np.savetxt('output.txt', images[0], fmt='%d', delimiter=',')
  # %80 eğitim ve %20 test olacak şekilde ayırıyoruz
train_data, test_data, train_labels, test_labels = train_test_split(images, labels, test_size=1, random_state=42
)

# Eğitim ve test verilerinin boyutlarını kontrol edelim
print(f"Train data shape: {train_data.shape}")
print(f"Test data shape: {test_data.shape}")
print(f"Train labels shape: {train_labels.shape}")
print(f"Test labels shape: {test_labels.shape}")
        