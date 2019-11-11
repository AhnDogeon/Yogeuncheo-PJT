from django.test import TestCase
from .models import *
import pandas as pd
import requests
import json

# Create your tests here.
def create_data():
    result = pd.read_csv('../data/data_adg/지하철_교육시설포함_최종.txt', sep=",", encoding="utf-8")
    # result = pd.DataFrame(result,columns=["result_id","address", "gu", "dong", "mac_score", "lot_score",
    #                       "burgerking_score",'seveneleven_score', 'cu_score', 'gs25_score', 'starbucks_score', 'lottecinema_score',
    #                       'megabox_score', 'cgv_score', 'total_score', 'high_oil', 'oil' 'oil2', 'total', 'catch', 'percent', 'mac_count',
    #                       'lot_count', 'burgerking_count', 'seveneleven_count','cu_count', 'gs25_count','starbucks_count','lottecinema_count','megabox_count',
    #                       'cgv_count', 'total_count','first','second', 'third'])
    # print(result.loc[5])
    # print(result.loc[5]['address'])
    for i in range(len(result.index)):
        print(result.loc[i]['address'])
        a = TotalAddress(
            address = result.loc[i]['address'],
            gu = result.loc[i]['gu'],
            dong = result.loc[i]['dong'],
            mac_score = float(result.loc[i]['mac_score']),
            lot_score = float(result.loc[i]['lot_score']),
            burgerking_score = float(result.loc[i]['burgerking_score']),
            seveneleven_score = float(result.loc[i]['seveneleven_score']),
            cu_score = float(result.loc[i]['cu_score']),
            gs25_score = float(result.loc[i]['gs25_score']),
            starbucks_score = float(result.loc[i]['starbucks_score']),
            lottecinema_score = float(result.loc[i]['lottecinema_score']),
            megabox_score = float(result.loc[i]['megabox_score']),
            cgv_score = float(result.loc[i]['cgv_score']),
            total_score = float(result.loc[i]['total_score']),

            high_oil = float(result.loc[i]['high_oil']),
            oil = float(result.loc[i]['oil']),
            oil2 = float(result.loc[i]['oil2']),
            total = int(result.loc[i]['total']),
            catch = int(result.loc[i]['catch']),
            percent = float(result.loc[i]['percent']),

            mac_count = int(result.loc[i]['mac_count']),
            lot_count = int(result.loc[i]['lot_count']),
            burgerking_count = int(result.loc[i]['burgerking_count']),
            seveneleven_count = int(result.loc[i]['seveneleven_count']),
            cu_count = int(result.loc[i]['cu_count']),
            gs25_count = int(result.loc[i]['gs25_count']),
            starbucks_count = int(result.loc[i]['starbucks_count']),
            lottecinema_count = int(result.loc[i]['lottecinema_count']),
            megabox_count = int(result.loc[i]['megabox_count']),
            cgv_count = int(result.loc[i]['cgv_count']),
            total_count = int(result.loc[i]['total_count']),
            first = result.loc[i]['first'],
            second = result.loc[i]['second'],
            third = result.loc[i]['third'],
            first_mapx = result.loc[i]['first_mapx'],
            first_mapy = result.loc[i]['first_mapy'],
            second_mapx = result.loc[i]['second_mapx'],
            second_mapy = result.loc[i]['second_mapy'],
            third_mapx = result.loc[i]['third_mapx'],
            third_mapy = result.loc[i]['third_mapy'],
            elementary_count= result.loc[i]['elementary_count'],
            middle_count=result.loc[i]['middle_count'],
            high_count=result.loc[i]['high_count'],
            park_count=result.loc[i]['park_count'],
            station=result.loc[i]['station']
        )
        print(i, '/', len(result))
        a.save()
    else:
        print("create data done")


create_data()