def best_size_select(input_folder, output_folder):
  import cv2
  import os
  import numpy as np

  # 슈퍼 해상도 모델 설정
  model_path = 'C:/Users/itwill/Desktop/python/EDSR_Tensorflow-master/EDSR_Tensorflow-master/models/EDSR_x4.pb'
  sr = cv2.dnn_superres.DnnSuperResImpl_create()
  sr.readModel(model_path)
  sr.setModel('edsr', 8)  # 스케일 팩터 설정
  # 스케일 팩터는 2, 4, 8 설정가능 숫자가 올라갈수록 고해상도 단, 처리속도가 느려짐

  # 결과 폴더가 없으면 생성
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  # 폴더 내 모든 이미지 파일에 대해 슈퍼 해상도 적용
  for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
      img_path = os.path.join(input_folder, filename).replace("\\",
                                                              "/")  # 경로 수정
      img = cv2.imread(img_path)
      if img is None:
        print(f"Failed to load image at {img_path}, skipping...")
        continue
      try:
        # 슈퍼 해상도 적용
        result = sr.upsample(img)
        if result is None or not isinstance(result, np.ndarray):
          print(f"슈퍼 해상도 처리 실패: {img_path}")
          continue
        # 결과 이미지 저장
        base_name = os.path.basename(img_path)
        output_path = os.path.join(output_folder, base_name)
        save_success = cv2.imwrite(output_path, result)
        if not save_success:
          print(f"Failed to save image at {output_path}")
      except Exception as e:
        print(f"Error processing {img_path}: {e}")

  print("All images have been processed.")


# 이미지가 있는 폴더와 결과를 저장할 폴더
input_folder = 'C:/Users/itwill/Desktop/imgs/musinsa/heal'
output_folder = 'C:/Users/itwill/Desktop/imgs/musinsa/heal_dpi'
best_size_select(input_folder, output_folder)
