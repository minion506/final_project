def load_images_from_folder(folder_path):
  images = []
  labels = []
  label_dict = {}
  label_index = 0
  for folder_name in os.listdir(folder_path):
    folder_path_class = os.path.join(folder_path, folder_name)
    label_dict[folder_name] = label_index
    for filename in os.listdir(folder_path_class):
      if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img_path = os.path.join(folder_path_class, filename)
        img = Image.open(img_path)
        img_array = np.array(img)
        images.append(img_array)
        labels.append(label_index)
    label_index += 1
  return np.array(images), np.array(labels), label_dict
