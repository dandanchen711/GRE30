import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


BrokerList=['FXTM','FXCM','GKFX','IC','IG','Gain']
DateList = ['03232020','03242020','03252020']
HOUR=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','']

Datehour=[]
FXTM_MeanSpread_list=[]
FXCM_MeanSpread_list=[]
GKFX_MeanSpread_list=[]
IC_MeanSpread_list=[]
IG_MeanSpread_list=[]
Gain_MeanSpread_list=[]

for Date in DateList:
    for i in HOUR:
        datehour = Date + "-" + str(i)
        Datehour.append(datehour)


for Date in DateList:
    for Broker in BrokerList:
        file="E:/GER30/GER30/{0}-{1}.csv".format(Broker,Date)
        roughdata = pd.read_csv(file,sep=',')
        roughdata['Spread']=roughdata['Ask'] - roughdata['Bid']
        roughdata['hour']=[t[:2] for t in roughdata['Time']]
      #  roughdata.drop(['Swap Long', 'Swap Short','Time','Bid','Ask'], axis=1, inplace=True)
        Spreaddict= dict(roughdata.groupby(['hour'])['Spread'].mean())
        for h in HOUR:
            if Broker == 'FXTM':
                if  h in Spreaddict.keys():
                    for key,value in Spreaddict.items():
                        if key == h:
                            FXTM_MeanSpread_list.append(value)
                else:
                    FXTM_MeanSpread_list.append("")
            elif Broker == 'FXCM':
                if h in Spreaddict.keys():
                    for key, value in Spreaddict.items():
                        if key == h:
                            FXCM_MeanSpread_list.append(value)
                else:
                    FXCM_MeanSpread_list.append("")
            elif Broker == 'GKFX':
                if h in Spreaddict.keys():
                    for key, value in Spreaddict.items():
                        if key == h:
                            GKFX_MeanSpread_list.append(value)
                else:
                    GKFX_MeanSpread_list.append("")
            elif Broker == 'IC':
                if h in Spreaddict.keys():
                    for key, value in Spreaddict.items():
                        if key == h:
                            IC_MeanSpread_list.append(value)
                else:
                    IC_MeanSpread_list.append("")
            elif Broker == 'IG':
                if h in Spreaddict.keys():
                    for key, value in Spreaddict.items():
                        if key == h:
                            IG_MeanSpread_list.append(value)
                else:
                    IG_MeanSpread_list.append("")
            elif Broker == 'Gain':
                if h in Spreaddict.keys():
                    for key, value in Spreaddict.items():
                        if key == h:
                            Gain_MeanSpread_list.append(value)
                else:
                    Gain_MeanSpread_list.append("")
print(FXTM_MeanSpread_list)
print(FXCM_MeanSpread_list)
print(GKFX_MeanSpread_list)
print(IC_MeanSpread_list)
print(IG_MeanSpread_list)
print(Gain_MeanSpread_list)
zip1= zip(Datehour,
          FXTM_MeanSpread_list,
          FXCM_MeanSpread_list,
          GKFX_MeanSpread_list,
          IC_MeanSpread_list,
          IG_MeanSpread_list,
          Gain_MeanSpread_list,)


with open('E:/finaldata1.csv','w',newline='') as csvfile:
    #创建一个写入对象
    FD = csv.writer(csvfile)         #声明文件csvfile是可写入的
    FD.writerow(["Datehour",'FXTM','FXCM','GKFX','IC','IG','Gain'])   #新建列名
    for row in zip1:
        FD.writerow(row)


#画图
df=pd.read_csv(r'E:/finaldata1.csv',sep=',')
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.plot(df['Datehour'],df['FXTM'],label='FXTM',linewidth=2,color='red',c='y',linestyle='--',marker='o')
ax.plot(df['Datehour'], df['FXCM'], label='FXCM', linewidth=2, color='blue', c='y', linestyle='--',marker='o')
ax.plot(df['Datehour'], df['GKFX'], label='GKFX', linewidth=2, color='yellow', c='y', linestyle='--',marker='o')
ax.plot(df['Datehour'], df['IC'], label='IC', linewidth=2, color='green', c='y', linestyle='--',marker='o')
ax.plot(df['Datehour'], df['IG'], label='IG', linewidth=2, color='black', c='y', linestyle='--',marker='o')
ax.plot(df['Datehour'], df['Gain'], label='Gain', linewidth=2, color='orange', c='y', linestyle='--',marker='o')
HOUR1=df['Datehour']
HOUR=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','',
      '00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','',
      '00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','']
_=plt.xticks(HOUR1,HOUR)
# ax.set_xlim(['03/23','03/24','03/25'])
ax.set_ylim([0,35])
ax.set_xlabel('03/23                                                                         03/24                                                                          03/25')
ax.set_ylabel('spread')
ax.set_title("03/23-03/25 Six Brokers Spread by Hours")
plt.legend()
# plt.title("03/23-03/25 Six Brokers Spread by Hours")
plt.show()


