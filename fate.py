#!/usr/bin/python3.9
# -*- coding: utf-8 -*- 
# Fortunetelling based on https://kknews.cc/astrology/ov3ze2m.html
# 諸葛亮三世書，自測財運（非常神奇）
# Usage: ./fate.py <Input.json>

import sys
import json

# Assign an alphabet to each fortune type:
# A = 正 
# B = 逐 
# C = 背 
# D = 耗 
# E = 困 
# F = 天 
# G = 向 
# H = 煞 
# I = 才 
# J = 旺 
# K = 暗 
# L = 病

yearList0 = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

# yearLastDigit
# 0 正 逐 背 耗 困 天 向 煞 才 旺 暗 病
# 1 病 正 逐 背 耗 困 天 向 煞 才 旺 暗
# 2 暗 病 正 逐 背 耗 困 天 向 煞 才 旺
# 3 旺 暗 病 正 逐 背 耗 困 天 向 煞 才
# 4 向 煞 才 旺 暗 病 正 逐 背 耗 困 天
# 5 天 向 煞 才 旺 暗 病 正 逐 背 耗 困
# 6 困 天 向 煞 才 旺 暗 病 正 逐 背 耗
# 7 耗 困 天 向 煞 才 旺 暗 病 正 逐 背
# 8 背 耗 困 天 向 煞 才 旺 暗 病 正 逐
# 9 逐 背 耗 困 天 向 煞 才 旺 暗 病 正

# To rotate the fortune list for each year's last digit (table shown above)
def rotateList(inputList, num):
    return inputList[-num:] + inputList[:-num]

# To determine the fortune type based on birth year and birth month
def fateCheck(yearLastDigit, month):
    if yearLastDigit >= 4:
        return rotateList(yearList0, yearLastDigit + 2)[month - 1]
    else:
        return rotateList(yearList0, yearLastDigit)[month - 1]

# Corresponding fortune description for each fortune type
def descript(letter):
    switcher = {
        'A': "正祿 勤儉成富，祖業福祿十分弱，所得一分一毫需靠勞力賺取，可是財運極佳，皆因個性克勤克儉，不放過搵銀良機，積少成多，發達都無人知。唯獨姻緣欠順，可能不止一次嫁娶。",
        'B': "逐祿 孤寒斂財，金錢不缺，雖不是超級富豪，但一生財政充裕，要乜有乜。缺點是喜歡追名逐利，永遠貪不知足，但又非常吝嗇，搵埋多多錢卻不捨得花費，「孤寒財主」正是他們的寫照。",
        'C': "背祿 離鄉別井，註定奔波勞碌到外地搵食，以前中國人重視鄉土親情，迫不得已才會離鄉別井。但時勢轉變，周圍走才得四方財，有邊個商家不是搭飛機多過行路？總之搵到錢便屬貴格。",
        'D': "耗祿 快來快去，一生中有多次大筆金錢過手的機會，即使如此，也不能算是富貴命。因為錢財來得快去得快，如不能妥善理財，最後千金散盡，晚景孤苦淒涼。",
        'E': "困祿 知足常樂，所謂「知足者貧亦樂」，無論出生和財祿也平平無奇，但知足的個性令他們不以為苦。這種人福氣不薄，多數擁有無憂的晚年，年紀愈大愈富貴。",
        'F': "天祿 祖蔭豐厚，前世做得好事多，今世可在富裕環境長大，祖蔭豐厚，名副其實含住金鎖匙出生。他們只要守住祖業，一生衣食無憂，不宜太刻意鑽營求財，否則招至失敗。",
        'G': "向祿 超級巨富，十二財祿中，以向祿最好。正財、橫財兩可兼得，一生與金錢結下不解緣，創業做老闆固然有機會成巨富，即使幫人打工亦屬令人稱羨的「打工皇帝」。離開出生地往外地發展，成就更大。",
        'H': "煞祿 奔波勞碌，半生奔波，只因優柔寡斷的性格所累，想做又不夠勇氣，到立下決心時又為時已晚，因此在年輕時錯過不少發達契機。補救方法是學一門技能傍身，努力工作自然衣食無憂。",
        'I': "才祿 親力親為，財運不過不失，所得的金錢與付出的努力成正比，想賺錢必須親力親為。而才祿的人，一般比人聰明、有學識，適宜從事專業行頭，例如醫生、律師、藝術家等，下半生生活過得充裕。",
        'J': "旺祿 大富大貴，財格拍得住「向祿」，同屬大富大貴命。致富之道是穩守突擊，不宜投資高風險項目，穩穩陣陣反而可望財源廣進。財運主要由貴人帶挈，適宜拓闊人際網絡和社交圈子。",
        'K': "暗祿 先苦後甜，受前世影響，今生與家人難和睦相處，別奢望可以靠屋企發達。財運先苦後甜，需依賴朋友致富，不妨找個有信用的拍檔做生意。晚景甚佳，積落不少金錢，長壽而健康。",
        'L': "病祿 好食懶做，你並非能力遜於人，只系自己好食懶做，機會送上門都白白流失，想發達的話切忌貪圖安逸，所謂「力不到不為財」。此外，他們天生體質較差，沒有良好體魄，競爭力難免被削弱。"
    }
    return switcher.get(letter, None)

# Read in the users' info(Name, Birth year, Birth month)
with open(sys.argv[1], 'r') as input:
    data = json.load(input)
    group = 'friends'
    for i in data[group]:
        name = f"Name(名字):     {i['Name']}\n"
        year = f"Year(農曆年份): {i['Year']}\n"
        month = f"Month(農曆月份): {i['Month']}\n"
        fateText = f"Fortune(今世財運): {descript(fateCheck(i['Year'] % 10, i['Month']))}\n" 
        line = "-----------------\n"
        display = name + year + month + fateText + line
        print(display)
        with open('output', 'a') as output:
            output.write(display)
