def split_scale_sc(df_x, df_y):
  from sklearn.model_selection import train_test_split
  train_x, test_x, train_y, test_y = train_test_split(df_x,df_y,random_state=0)
  # 2. 변수 스케일링
  train_x_sc = train_x.reshape(1200, -1) / 255  # minmax scaling + 머신러닝 학습을 위한 2차원 형태 변환
  test_x_sc = test_x.reshape(400, -1) / 255
  return train_x_sc, train_y, test_x_sc, test_y 