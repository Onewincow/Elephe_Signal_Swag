# -*- coding: utf-8 -*-

### 2. 환율 계산

def yen2usdollar(yen,jpywon,usdwon):
    return round(yen*(jpywon/100)*(1/usdwon),2)

print(yen2usdollar(10000,1107.15,1138.95)) # 97.21
print(yen2usdollar(50000,1107.15,1138.95)) # 486.04
