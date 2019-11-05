# -*- coding: utf-8 -*-

from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
import json

print('도로명주소 검색API 서비스를 이용한 주소검색결과를 보여줍니다.')
keystr = '서울특별시 강남구 논현로 640'
resulttype = 1

if resulttype == '1':
    resulttype = 'json'
else:
    resulttype = 'xml'

# print(resulttype)

url = 'http://www.juso.go.kr/addrlink/addrLinkApi.do'
queryParams = '?' + urlencode(
    {quote_plus('currentPage'): '1', quote_plus('countPerPage'): '10', quote_plus('resultType'): resulttype,
     quote_plus('keyword'): keystr, quote_plus('confmKey'): 'devU01TX0FVVEgyMDE5MTAyOTE1NTExMjEwOTE0NzY='})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

# print(response_body.decode('utf-8'))

print("url = " + url)
print("keyword = " + keystr)
print("=" * 100)

if resulttype == 'json':
    root_json = json.loads(response_body)
    print('<< results >>')
    print('totalCount   : ' + root_json['results']['common']['totalCount'])
    print('currentPage  : ' + root_json['results']['common']['currentPage'])
    print('countPerPage : ' + root_json['results']['common']['countPerPage'])
    print('errorCode    : ' + root_json['results']['common']['errorCode'])
    print('errorMessage : ' + root_json['results']['common']['errorMessage'])
    for child in root_json['results']['juso']:
        print('-' * 100)
        print('[' + child['zipNo'] + '] ' + child['roadAddr'])
        print('    지번주소     = ' + child['jibunAddr'])
        print('    영문주소     = ' + child['engAddr'])
        print('    도로명코드   = ' + child['rnMgtSn'])
        print('    건물관리번호 = ' + child['bdMgtSn'])
        print('    법정동코드   = ' + child['admCd'])
        print('    상세건물명   = ' + child['detBdNmList'])
        print('')


else:
    root_xml = ET.fromstring(response_body)

    print('<< ' + root_xml.tag + ' >>')

    print('totalCount   : ' + root_xml.find('common').findtext('totalCount'))
    print('currentPage  : ' + root_xml.find('common').findtext('currentPage'))
    print('countPerPage : ' + root_xml.find('common').findtext('countPerPage'))
    print('errorCode    : ' + root_xml.find('common').findtext('errorCode'))
    print('errorMessage : ' + root_xml.find('common').findtext('errorMessage'))

    for child in root_xml.findall('juso'):
        print('-' * 100)
        print('[' + child.findtext('zipNo') + '] ' + child.findtext('roadAddr'))
        print('    지번주소     = ' + child.findtext('jibunAddr'))
        print('    영문주소     = ' + child.findtext('engAddr'))
        print('    도로명코드   = ' + child.findtext('rnMgtSn'))
        print('    건물관리번호 = ' + child.findtext('bdMgtSn'))
        print('    법정동코드   = ' + child.findtext('admCd'))
        print('    상세건물명   = ' + child.findtext('detBdNmList'))
        print('')