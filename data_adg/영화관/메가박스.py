import json
import urllib.request
import csv
import pandas as pd

client_id = "cGQPySd4kIgkemMRa0t7"
client_secret = "b85YEslxV7"

code = '영화관'
gu_list = ['서울특별시 종로구', '서울특별시 중구', '서울특별시 용산구', '서울특별시 성동구',
           '서울특별시 광진구', '서울특별시 동대문구', '서울특별시 중랑구', '서울특별시 성북구',
           '서울특별시 강북구', '서울특별시 도봉구', '서울특별시 노원구', '서울특별시 은평구',
           '서울특별시 서대문구', '서울특별시 마포구', '서울특별시 양천구', '서울특별시 강서구',
           '서울특별시 구로구', '서울특별시 금천구', '서울특별시 영등포구', '서울특별시 동작구',
           '서울특별시 관악구', '서울특별시 서초구', '서울특별시 강남구', '서울특별시 송파구',
           '서울특별시 강동구']

brand_list = ['메가박스']
# pandas column 지정
df = pd.DataFrame(columns=['title', 'address', 'roadAddress', 'mapx', 'mapy', 'category', 'description', 'telephone'])

# gu_list 로 서울시 내 구 for문 반복
for gu in gu_list:
    # brand_list 안을 돌면서 업체 지정
    for brands in brand_list:
        # brand 예시 : 서울특별시 강남구 CU
        brand = gu + ' ' + brands
        print(brand)
        # 정확히 그 구만 검색하기 위한 gu 뽑기
        address_list = brand.split(' ')
        real_gu = address_list[1]
        print(gu)
        indexing = []  # 총 있는 정보
        encText = urllib.parse.quote(brand)
        url = "https://openapi.naver.com/v1/search/local?display=30&query=" + encText  # json 결과

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)

        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if (rescode == 200):
            json_rt = response.read().decode('utf-8')
            py_rt = json.loads(json_rt)
            many_time = py_rt['total'] // 30  # 몇 번 반복문 돌지
            start = 1
            if many_time == 0:
                many_time = 1
            for _ in range(many_time):
                url = "https://openapi.naver.com/v1/search/local?display=30&query=" + encText + '&start=' + str(
                    start)  # json 결과

                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()

                start += 30
                # 서울특별시 강남구를 검색했을 때 다른 구도 같이 검색돼서 제외하는 코드
                if (rescode == 200):
                    json_rt = response.read().decode('utf-8')
                    py_rt = json.loads(json_rt)
                    for j in range(len(py_rt['items'])):
                        if '서울특별시' in py_rt['items'][j]['address'] and real_gu in py_rt['items'][j][
                            'address'] and code in py_rt['items'][j]['category']:
                            # print(py_rt['items'][j])
                            indexing.append(py_rt['items'][j])
                    if '서울특별시' not in py_rt['items'][0]['address']:
                        break
                else:
                    print("Error Code:" + rescode)

        else:
            print("Error Code:" + rescode)
        for i in indexing:
            # df에 indexing 안의 것들 한 줄씩 추가
            df = df.append(i, ignore_index=True)
        print(df)

# df를 모두 추가한 최종본을 txt파일로 변환
df.to_csv("메가박스.txt", mode="w")
