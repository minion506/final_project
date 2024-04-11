def cnn_model(train_x, train_y, test_x, test_y):
  from tensorflow.keras.utils import to_categorical
  from keras.models import Sequential
  from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D, AveragePooling2D
  train_y = to_categorical(train_y)
  test_y = to_categorical(test_y)

  model = Sequential()
  model.add(
      Conv2D(
          filters=32,  # mask(filter) 수*
          kernel_size=(2, 2),  # mask size
          input_shape=(100, 100, 3),  # input data size(하나의 데이터 포인트의 사이즈)
          activation='relu'))
  model.add(Conv2D(filters=32, kernel_size=(2, 2), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(2, activation='sigmoid'))

  # 4. compile(loss, metric, optimizer)
  model.compile('adam', loss='binary_crossentropy', metrics=['accuracy'])

  # 5. 정지 규칙
  from keras.callbacks import EarlyStopping

  stop1 = EarlyStopping(monitor='val_loss', patience=10)

  # 6. 학습
  model.fit(train_x, train_y, validation_split=0.25, batch_size=50, epochs=1000000, callbacks=[stop1])

  print('train : '+model.evaluate(train_x, train_y)[1])
  print('test : '+model.evaluate(test_x, test_y)[1])