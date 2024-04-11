def knn_pca(train_X, train_y, test_x, test_y):
  from sklearn.decomposition import PCA
  from sklearn.neighbors import KNeighborsClassifier as knn_c
  from sklearn.pipeline import make_pipeline
  pipe = make_pipeline(PCA(100), knn_c(5))
  pipe.fit(train_X, train_y)
  print('train score : %s' % pipe.score(train_X, train_y))
  print('test score : %s' % pipe.score(test_x, test_y))
