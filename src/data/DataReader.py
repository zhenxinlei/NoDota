# get data from yahoo google finance
# input { "TICKER", "strat-date", "end-date"}

from pandas_datareader import data, wb
import csv

#list of raw data

# type 1 success in W shape
# type 2 failed  in W shape

assetList = [["AAPL", "6-7-2016", "7-18-2016", "1"],
             ["AAPL", "1-7-2006", "4-5-2006", "2"],
             ["NKE", "12-21-2007", "4-5-2008", "1"],
             ["NKE", "6-21-2004", "9-8-2004", "1"],
              ["NKE", "8-10-2000", "1-12-2001", "1"],
             ["WMT", "11-26-2013", "2-14-2014", "2"],
             ["WMT", "08-1-2013", "11-27-2014", "1"],
              ["WMT", "5-5-2011", "08-16-2011", "2"],
              ["WMT", "7-30-2013", "11-8-2013", "1"],
             ["WMT", "12-4-2013", "1-29-2014", "2"],
             ["WMT", "6-13-2007", "12-11-2007", "1"],
             ["WMT", "3-2-2004", "4-13-2004", "2"],
             ["WMT", "4-23-2004", "7-8-2004", "2"],
             ["ALK", "7-21-2014", "11-4-2014", "2"],
             
             
]

for asset in assetList:
    assetData = data.DataReader(asset[0], "yahoo", asset[1], asset[2] )
    processedData = assetData[['Close','Volume']]
    print("writing data to "+asset[0]+'_'+asset[3]+'.csv')
    processedData.to_csv("./processed_data/"+asset[0]+'_'+asset[1]+'_'+asset[2]+'_'+asset[3]+'.csv')
