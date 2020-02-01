from alpha_vantage.timeseries import TimeSeries
import pandas as pd


def getDailyDataAV (ticker, number_of_days):

    ts = TimeSeries(key='UN801AMDJDRWRIE5')

    try:
        data, meta_data = ts.get_daily(ticker)
        df = pd.DataFrame(data)

        df = ((pd.DataFrame(data).transpose()).head(number_of_days)).transpose()
        df = df.drop(['1. open', '2. high', '3. low', '5. volume'], axis=0)
        return df

    except:
        print("An exception occurred")
