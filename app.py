from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPool2D


# Model tanımlanır
model=Sequential()
#CNN ve pooling katmanları eklenir
model.add(Conv2D(32,(5,5),activation='relu',input_shape=(32,32,3)))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(32,(5,5),activation='relu'))
model.add(Conv2D(32,(5,5),activation='relu'))
model.add(Conv2D(32,(5,5),activation='relu'))


model.add(MaxPool2D(pool_size=(2,2)))
#Flatten katmanı eklenir
model.add(Flatten( ))
model.add(Dense(1000,activation='relu') )
model.add(Dense(1,activation='softmax') )# 10 tane etiket olduğu için 10 tane sinir node uluşturuldu.


