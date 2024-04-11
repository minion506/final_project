def knn_model(train_x, train_y, test_x, test_y):
  from sklearn.neighbors import KNeighborsClassifier as knn_c
  m_knn = knn_c()
  m_knn.fit(train_x, train_y)
  print('train_score : ',m_knn.score(train_x, train_y))
  print('test_score : ',m_knn.score(test_x, test_y))