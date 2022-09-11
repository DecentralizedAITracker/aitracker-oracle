
import requests
import json
import os
import pandas as pd
import numpy as np
from aitracker_oracle import AITrackerOracle

iexec_out = os.environ['IEXEC_OUT']
iexec_in = os.environ['IEXEC_IN']
iexec_in_filename = os.environ['IEXEC_INPUT_FILE_NAME_1']

class App:
    
    def __init__(self,):
        print("ONLINE")

class Utils:
   
    def parser(klines):
        seq_x = list()
        for row in klines:
            row[0] = int(row[0])    #open time
            row[1] = float(row[1])  #open
            row[2] = float(row[2])  #high
            row[3] = float(row[3])  #low
            row[4] = float(row[4])  #close
            row[5] = float(row[5])  #volume
            row[6] = int(row[6])    #close time
            row[7] = float(row[7])  #quote asset volume
            row[8] = int(row[8])    #number of trades
            row[9] = float(row[9])  #taker buy base asset volume
            row[10] = float(row[10])#taker buy quote asset volume
            row[11] = float(row[11])#ignore
            seq_x.append(row)
        return np.array(seq_x)

    def checkMarketTrend(seq_x,timestamp):
        for row in seq_x:
            if(int(row[0]) < int(timestamp) and int(timestamp) < int(row[6])):
                if(row[1] < row[4]):
                    return "UP"
                else:
                    return "DOWN"
    

class Binance:

    def fetchCandlesticks(symbol,unix_timestamp):
        url = 'https://api.binance.com/api/v3/klines'
        params = {
            'symbol': symbol,
            'interval': "1h",
            'limit': '500',
            'endTime' : unix_timestamp
        }
        
        json_data = requests.get(url, params=params).json()
        seq_x = Utils.parser(json_data)
        return seq_x



if __name__ == '__main__':
    
    filepath = iexec_in + "/" + iexec_in_filename
    f = open(filepath,'r')
    result_text = f.read()
    result_object = json.loads(result_text)
    f.close()

    prediction_with_signature = result_object["prediction_with_signature"]

    prediction_for_oracle = prediction_with_signature["prediction_for_oracle"]
    signature = prediction_with_signature["signature"]

    prediction_encrypted = prediction_for_oracle["prediction_encrypted"]
    symbol = prediction_for_oracle["symbol"]
    timestamp = prediction_for_oracle["timestamp"]
    
    ait_oracle = AITrackerOracle('./src/' + 'public_key_ml.pem','./src/' + 'private_key_oracle.pem')

    print(json.dumps(prediction_for_oracle))
    verify = ait_oracle.verify(json.dumps(prediction_for_oracle),signature)
    if(not verify):
        print("verification failed")

    prediction_decrypted = ait_oracle.decrypt(json.dumps(prediction_encrypted))
 
    seq_x = Binance.fetchCandlesticks(symbol,timestamp)
    markettrend = Utils.checkMarketTrend(seq_x,timestamp)
