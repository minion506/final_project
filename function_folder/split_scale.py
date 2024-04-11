def split_scale(df_x, df_y):
  from sklearn.model_selection import train_test_split
  train_x, test_x, train_y, test_y = train_test_split(df_x,df_y,random_state=0)
  train_x = train_x / 255
  test_x = test_x / 255
  return train_x, train_y, test_x, test_y
