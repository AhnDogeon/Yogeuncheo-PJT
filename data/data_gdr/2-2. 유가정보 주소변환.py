import json
import urllib.request
import requests
import csv
client_id = '738e112ffc94cfbac927c9db1e73b633'

oil_file = open("./2-1. 유가 정보(10월 4주차).txt", 'r', encoding='UTF-8')

oil_data = oil_file.readlines()
new_oil_data = open('./2-3. 유가 정보(10월 4주차) 주소변환.txt', 'a', encoding='UTF-8')
new_oil_data.write('\t'.join(['변환한 주소', '시', '구', '동', '상호명', '유가 정보 기간', '상표', '셀프여부', '고급휘발유', '휘발유', '경유']))
new_oil_data.write('\n')

for index in range(1, len(oil_data)):

    oil = oil_data[index].split('\t')
    address = oil[3]

    url = 'https://dapi.kakao.com/v2/local/search/address'
    queryString = {"query": address}
    header = {'authorization': 'KakaoAK 738e112ffc94cfbac927c9db1e73b633'}

    trans = requests.get(url, headers=header, params=queryString)

    address = json.loads(trans.text)['documents'][0]['address']['address_name']  # 지번으로 변환한 주소
    si = json.loads(trans.text)['documents'][0]['address']['region_1depth_name'] # 시
    gu = json.loads(trans.text)['documents'][0]['address']['region_2depth_name']# 구
    dong = json.loads(trans.text)['documents'][0]['address']['region_3depth_name'] # 동
    store_name = oil[2] # 상호명
    data_range = oil[4] # 기간
    oil_name = oil[5] # 상표
    self = oil[6] # 셀프여부
    oil1 = oil[7] # 고급 휘발유
    oil2 = oil[8] # 휘발유
    oil3 = oil[9] # 경유

    one_oil = [address, si, gu, dong, store_name, data_range, oil_name, self, oil1, oil2, oil3]

    new_oil_data.write('\t'.join(one_oil))
    new_oil_data.write('\n')

new_oil_data.close()
oil_file.close()