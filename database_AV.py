import sqlite3
import queries
import api_data

# conecta e cria um database na memóra
con = sqlite3.connect("database.db")
c = con.cursor()



#### PARTE I  ##### (PRIMEIRAS QUERIES)
# # cria as tabelas
# c.execute(queries.queryCreateStocksTable())
# c.execute(queries.queryCreatePricesTable())
#
# # preenche a tabela de ações
# c.execute(queries.insertIntoStocks('B3SA3', 'Brasil Bolsa Balcao', '1'))  # adiciona a ação B3SA3
# c.execute(queries.insertIntoStocks('PETR4', 'Petroleo Brasileiro SA Petrobras Preference Shares', '1'))  # adiciona a ação PETR4



#### PARTE II ####  (PREENCHE BANCO DE DADOS COM OS 7 ÚLTIMOS DIAS)
# dfB3SA3 = api_data.getDailyDataAV('B3SA3.SAO', 7)
# dfPETR4 = api_data.getDailyDataAV('PETR4.SAO', 7)
#
#
# for i in range(7):
#     c.execute(queries.insertIntoPrices(dfB3SA3, 1, i))
#     c.execute(queries.insertIntoPrices(dfPETR4, 2, i))



### PARTE III ####  (ATUALIZAÇÕES DIÁRIA DAS AÇÕES)
dfB3SA3 = api_data.getDailyDataAV('B3SA3.SAO', 1)
dfPETR4 = api_data.getDailyDataAV('PETR4.SAO', 1)

c.execute(queries.insertIntoPricesDaily(dfB3SA3, 1))
c.execute(queries.insertIntoPricesDaily(dfPETR4, 2))

c.execute(queries.selectFromPrices())
print(c.fetchall())




con.commit()
con.close()

