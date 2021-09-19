import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas_datareader import data
import time
import math
import datetime
import yfinance as yf
import winsound
now = time.time()
stock_list =   ['TWOH', 'PHIL', 'TGRO', 'VIZC', 'PUGE', 'RETC', 'PLYZ', 'PBHG',
                'RTON', 'RBNW', 'VPER', 'TGGI', 'RDAR', 'RNVA', 'UBQU', 'SEEK',
                'NUUU', 'TXTM', 'RGBP', 'WNBD', 'PBYA', 'PVSP', 'TMGI', 'NSAV',
                'RSHN', 'SANP', 'TLSS', 'SGMD', 'SRMX', 'WWIO', 'NSPX', 'ONCI',
                'WTII', 'USMJ', 'PRPM', 'VISM', 'SNRY', 'WDLF', 'RITE', 'VGLS',
                'QBAN', 'WCVC', 'TBEV', 'SBES', 'SPZI', 'VGID', 'OZSC', 'ZONX',
                'PLPL', 'NTRR', 'TSOI', 'SNMN', 'PRMO', 'TONR', 'VNTH', 'WHEN',
                'VXIT', 'SWRM', 'SHOM', 'OPTI', 'PDMI', 'OTTV', 'PRDL', 'SDVI',
                'PJET', 'RMSL', 'SUTI', 'SVAD', 'USEI', 'PSRU', 'SNVP', 'WPMLF',
                'WHSI', 'NWGC', 'PASO', 'WSSE', 'VOIS', 'XTRM', 'PAOG', 'XFLS',
                'SHMN', 'TPTW', 'RDWD', 'VBHI', 'RMRK', 'SNRS', 'RCMH', 'SPOI',
                'VYON', 'SBFM', 'VNUE', 'PPJE', 'VSYM', 'TTCM', 'SVTE', 'TPNI',
                'OCLG', 'NWTT', 'SKYF', 'VDRM', 'SNDD', 'NPHC', 'QEDN', 'SEGI',
                'PHJMF', 'RLLCF', 'PFNO', 'TOMDF', 'UATG', 'WSGF', 'PFWIQ',
                'TGODF', 'TGHI', 'RIGH', 'SSOF', 'VITX', 'SMAA', 'RBDC', 'SFOR',
                'RLFTF', 'SDEC', 'SPONF', 'WLAN', 'PQEFF', 'PSWW', 'VMSI', 'PCLI',
                'PYCT', 'PDOS', 'SNPW', 'UVSE', 'PURA', 'RMTD', 'THRR', 'PENMF',
                'RXMD', 'SCIE', 'RJDG', 'VGTL', 'SFLM', 'VTMB', 'SFRX', 'TCHC',
                'VSPC', 'NUGS', 'VYST', 'SAFS', 'TGRR', 'UNQL', 'QNTA', 'SSET',
                'SAPX', 'VMHG', 'RGGI', 'WDHR', 'TEXC', 'PWLK', 'TOEYF', 'WDRP',
                'WSRC', 'PZOO', 'RIII', 'PSYC', 'SPOM', 'SYAXF', 'VTXB', 'VMRSF',
                'TRNX', 'RCHA', 'SLGWF', 'VMCS', 'TFBN', 'TSPG', 'VPOR', 'PMEA',
                'PHMB', 'NYXO', 'TEUM', 'PRED', 'RLTR', 'TAWNF', 'TRSI', 'SEAOF',
                'PHOT', 'TPII', 'PMPG', 'VIRA', 'RGBPP', 'SGDH', 'RDGL', 'PHBI']
                

'''stock_list = ['dnn','ecor','exk','expr','geg','gnw','isr','nept','opk','qtt','rig','sskn','uec','swn','trch','nok','nxtd']'''

#stock_list = input('what stock would you like:  ').split()
#stock_list.append(f)

count = 0
count1=0
low_sma9 = 0
#for i in range(5000):#
while True:
    count+=1
    print('count',count)
    #data = yf.download(stocks ,period ='1d',interval='1m')
    for stock in stock_list:
        #stock = input('what stock would you like:  ')
        
        data = yf.download(stock ,period ='10d',interval='30m')
        #print(data)
        for i in range(len(data)):
            
            sma28 =data['Close'].rolling(window=28).mean()
            volume5=data['Volume'].rolling(window=5).mean()
            close =data['Close'].rolling(window=2).mean()
            #vol_avg50=data['Volume'].rolling(window=50).mean()
            vol_avg50=data['Volume'].rolling(window=50).mean()
        print('stock it' ,stock)
        count1+=1
        print('count1',count1)
        #print(f'close {close[-1]:.2f}')
        #print('volume',volume[-1])
        #print('volume5',volume5[-1])
        #print('vol_avg50',vol_avg50[-1])
        time.sleep(.1)
        #.0001 to 
        if volume5[-1] > (vol_avg50[-1] * 4.5) and sma28[-1] > sma28[-6] and close[-1] < .0020:
            print('stock',stock)
            print(f'stock price  {close[-1]:.3f}')
            print('volume surge')
            winsound.Beep(790,200)
        
        if volume5[-1] > 6650000 and sma28[-1] > sma28[-5] and close[-1] < .0020:
            print('stock',stock)
            print(f'stock price  {close[-1]:.3f}')
            print('volume5',volume5[-1])
            winsound.Beep(2300,100)
        
        
        #time.sleep(1.1)
time.sleep(120)
