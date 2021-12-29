Company=['Apple','IBM','Google','Tesla','Intel','Facebook','Amazon','HP','Cisco'] #公司名稱

Stockprice=[128.10,145.22,2314.77,670.94,56.85,315.02,3270.54,34.45,51.13] #公司股價
anw={} #建立一個空字典儲存答案
print('利用for迴圈:')
for i in range(0,len(Stockprice),1):
  anw[Company[i]]=Stockprice[i]
for i in anw: #用for迴圈建立字典
  if anw[i]>=300:
    print("%s:%.2f"%(i,anw[i]))

CompanyStockprice={'Apple':128.10,'IBM':145.22,'Google':2314.77,'Tesla':670.94,'Intel':56.85,'Facebook':315.02,'Amazon':3270.54,'HP':34.45,'Cisco':53.13} #公司股價字典
print('利用字典生成式:',{k:v for k,v in CompanyStockprice.items() if v > 300}) #利用字典生成式