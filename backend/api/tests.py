from django.test import TestCase
from .models import *
import pandas as pd
import requests
import json

# Create your tests here.
def create_data():
    result = pd.read_csv('../data/data_adg/최종 결과.txt', sep=",", engine='python', encoding="utf-8")
    for i in range(len(result.index)):
        # data_id = result.loc[i][0]
        # data = TotalAddress.objects.get(id=data_id)
        # data.address = result.loc[i][1]
        # data.gu = result.loc[i][2]
        # data.dong = result.loc[i][3]
        # data.mac_score = float(result.loc[i][4])
        # data.lot_score = float(result.loc[i][5])
        # data.burgerking_score = float(result.loc[i][6])
        # data.seveneleven_score = float(result.loc[i][7])
        # data.cu_score = float(result.loc[i][8])
        # data.gs25_score = float(result.loc[i][9])
        # data.starbucks_score = float(result.loc[i][10])
        # data.lottecinema_score = float(result.loc[i][11])
        # data.megabox_score = float(result.loc[i][12])
        # data.cgv_score = float(result.loc[i][13])
        # data.total_score = float(result.loc[i][14])
        #
        # data.high_oil = float(result.loc[i][15])
        # data.oil = float(result.loc[i][16])
        # data.oil2 = float(result.loc[i][17])
        # data.total = int(result.loc[i][18])
        # data.catch = int(result.loc[i][19])
        # data.percent = float(result.loc[i][20])
        #
        # data.mac_count = int(result.loc[i][21])
        # data.lot_count = int(result.loc[i][22])
        # data.burgerking_count = int(result.loc[i][23])
        # data.seveneleven_count = int(result.loc[i][24])
        # data.cu_count = int(result.loc[i][25])
        # data.gs25_count = int(result.loc[i][26])
        # data.starbucks_count = int(result.loc[i][27])
        # data.lottecinema_count = int(result.loc[i][28])
        # data.megabox_count = int(result.loc[i][29])
        # data.cgv_count = int(result.loc[i][30])
        # data.total_count = int(result.loc[i][31])

        # create_data(address=data.address, gu=data.gu, dong=data.dong, mac_score=data.mac_score, lot_score=data.lot_score,burgerking_score=data.burgerking_score,
        #             seveneleven_score=data.seveneleven_score, cu_score=data.cu_score, gs25_score=data.gs25_score, starbucks_score=data.starbucks_score,
        #             lottecinema_score=data.lottecinema_score, megabox_score=data.megabox_score, cgv_score=data.cgv_score, total_score=data.total_score,
        #             high_oil=data.high_oil, oil=data.oil, oil2=data.oil2, total=data.total, catch=data.catch, percent=data.percent,
        #             mac_count=data.mac_count, lot_count=data.lot_count, burgerking_count=data.burgerking_count,
        #             seveneleven_count=data.seveneleven_count, cu_count=data.cu_count,gs25_count=data.gs25_count,
        #             starbucks_count=data.starbucks_count,lottecinema_count=data.lottecinema_count,megabox_count=data.megabox_count,
        #             cgv_count=data.cgv_count, total_count=data.total_count)
        print(i, '/', len(result))
        # data.save()
    else:
        print("create data done")

create_data()