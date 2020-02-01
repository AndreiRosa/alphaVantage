def queryCreateStocksTable():
    return "CREATE TABLE STOCKS (StocksID integer PRIMARY KEY AUTOINCREMENT, Ticker text, Name text, Enabled binary)"

def queryCreatePricesTable():
    return ("CREATE TABLE PRICES (PriceID integer PRIMARY KEY AUTOINCREMENT, Date text, Assets integer, Price real, FOREIGN KEY (Assets) REFERENCES stocks(StocksID))")

def insertIntoStocks(ticker, name, enabled):
    return ("INSERT INTO STOCKS (Ticker, Name, Enabled) VALUES ('%s', '%s', '%s')" % (ticker, name, enabled))

def insertIntoPrices(df, id, i):
    return ("INSERT INTO PRICES (Date, Assets, Price) VALUES ('%s', '%s', %s)" % (str(df.columns[i]), id, (df[str(df.columns[i])]['4. close'])))

def insertIntoPricesDaily(df, id):
    return ("INSERT INTO PRICES (Date, Assets, Price) VALUES ('%s', '%s', %s) ON CONFLICT (Date) DO UPDATE SET Price = %s" % (str(df.columns[0]), id, df[str(df.columns[0])]['4. close'], df[str(df.columns[0])]['4. close']))

def selectFromPrices():
    return ("SELECT P.Date[Data], S.Ticker AS [Nome], P.Price[Preco]FROM PRICES AS P INNER JOIN STOCKS AS S ON P.Assets = S.StocksID")