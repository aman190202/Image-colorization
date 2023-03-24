SIZE = 160
color_img = []
directory = '/content/val2017'
directory_intended= '/content/val2017_grey'
for filename in os.listdir(directory):    
      img = cv2.imread(directory + '/'+filename,1)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      img = cv2.resize(img, (SIZE, SIZE))
      img = img.astype('float32') / 255.0
      color_img.append(img_to_array(img))


gray_img = []
for filename in os.listdir(directory_intended):
      img = cv2.imread(directory_intended + '/'+filename,1)
      img = cv2.resize(img, (SIZE, SIZE))
      img = img.astype('float32') / 255.0
      gray_img.append(img_to_array(img))
