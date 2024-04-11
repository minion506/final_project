def url_find(keyword,pagenum):
  url = ''
  if keyword == '로퍼':
      url = f'https://www.musinsa.com/categories/item/005015?d_cat_cd=005015&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=100&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '플랫슈즈'):
      url = f'https://www.musinsa.com/categories/item/005017?d_cat_cd=005017&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=100&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '구두'):
      url = f'https://www.musinsa.com/categories/item/005014?d_cat_cd=005014&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=100&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '힐')|(keyword == '펌프스'):
      url = f'https://www.musinsa.com/categories/item/005012?d_cat_cd=005012&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=100&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='    
  elif (keyword == '운동화') | (keyword == '스니커즈'):
      url = f'https://www.musinsa.com/categories/item/018?d_cat_cd=018&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=100&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '전자기기'):
      url = f'https://www.musinsa.com/categories/item/012?d_cat_cd=012&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=100&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '리빙'):
      url = f'https://www.musinsa.com/categories/item/058?d_cat_cd=058&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '반려동물'):
      url = f'https://www.musinsa.com/categories/item/021?d_cat_cd=021&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '상의'):
      url = f'https://www.musinsa.com/categories/item/001?d_cat_cd=001&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '원피스'):
      url = f'https://www.musinsa.com/categories/item/020?d_cat_cd=020&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '가방'):
      url = f'https://www.musinsa.com/categories/item/004?d_cat_cd=004&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '모자'):
      url = f'https://www.musinsa.com/categories/item/007?d_cat_cd=007&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '액세서리'):
      url = f'https://www.musinsa.com/categories/item/011?d_cat_cd=011&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '시계'):
      url = f'https://www.musinsa.com/categories/item/006?d_cat_cd=006&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  elif (keyword == '컬처'):
      url = f'https://www.musinsa.com/categories/item/014?d_cat_cd=014&brand=&list_kind=small&sort=pop_category&sub_sort=&page={pagenum}&display_cnt=90&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&plusDeliveryYn=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=&measure='
  else:
      print('non keyword')
  return url


def musinsa_shoes(keyword,start_page = 1, end_page=1):# page_size는 1부터 시작 
  from selenium import webdriver
  from bs4 import BeautifulSoup
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from urllib.request import urlretrieve
  import time
  import os 
  result = []
  driver = webdriver.Chrome()
  driver.maximize_window()   # 창 최대화
  for page in range(start_page,end_page+1):
      url = url_find(keyword,page)
      driver.get(url)
      time.sleep(5)
      driver.execute_script("window.scrollBy(268, 0);")
      time.sleep(5)
      # 페이지 높이를 가져옴
      last_height = driver.execute_script("return document.body.scrollHeight")
      print(last_height)
      i = 1
      while True:
          # 현재 높이에서 355 픽셀만큼 스크롤 다운
          driver.execute_script("window.scrollBy(0, 700);")
  
          # 스크롤 사이에 적절한 대기 시간 추가
          time.sleep(5)  # 필요에 따라 조정
          print(700*i)
          if last_height <= (700*i):
              break    
          i += 1
      imgs = driver.find_elements(By.CSS_SELECTOR,'div.li_inner > div.list_img > a.img-block > img.lazyload.lazy')
      for img in imgs:
          if img != 'https://image.msscdn.net/images/no_image_125.png':
              result.append(img.get_attribute('src'))
      print(result)
      time.sleep(10)
  #폴더생성
  img_folder_path = 'C:/Users/itwill/Desktop/imgs/musinsa/'+keyword    #이미지 저장 폴더
  if not os.path.isdir(img_folder_path):      #없으면 새로 생성
      os.mkdir(img_folder_path)
  
      #이미지 다운로드
  for index, link in enumerate(result):
      if link != 'https://image.msscdn.net/images/no_image_125.png':
          urlretrieve(link, 'C:/Users/itwill/Desktop/imgs/musinsa/'+keyword+'/{}'.format(index)+'.jpg')       
  
      # 작업이 완료되면 드라이버 종료
  driver.quit()