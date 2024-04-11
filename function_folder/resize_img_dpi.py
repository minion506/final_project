def resize_images_in_dir(source_dir, target_dir, size, dpi=(100, 100)):
  from PIL import Image
  import os
  # 타겟 디렉토리가 없으면 생성
  if not os.path.exists(target_dir):
    os.makedirs(target_dir)
  for filename in os.listdir(source_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # 지원하는 파일 형식
      img_path = os.path.join(source_dir, filename)
      img = Image.open(img_path)
      # 'P' 모드(팔레트 모드) 이미지를 'RGB' 모드로 변환
      if img.mode == 'P':
        img = img.convert('RGB')
      # 이미지 리사이징
      img_resized = img.resize(size, Image.ANTIALIAS)
      # 리사이징된 이미지 저장
      img_resized.save(os.path.join(target_dir, filename), dpi=dpi)


source_directory = 'C:/Users/itwill/Desktop/imgs/musinsa/로퍼'
target_directory = 'C:/Users/itwill/Desktop/imgs/musinsa/로퍼_dpi'
desired_size = (1600, 1600)  # 원하는 이미지 사이즈

resize_images_in_dir(source_directory, target_directory, (125, 150))
