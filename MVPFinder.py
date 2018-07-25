import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import numpy as np
import datetime 
import calendar
import math

def main():

	start = datetime.date(2015, 7, 24)
	end = datetime.date(2018, 7, 24)

	ticker = ['TSLA','GM']
	volume = [0]
	data_source = 'morningstar'
	stock_data = []
	close_price_columns = []
	better_close_price_columns = []
	final_close_price_columns = []
	banana = 0
	celery = []
	cabbage = []
	stock_matrix = []
	period_return = []
	individual_stock_std_dev = []
	stock_std_devs = []
	better_stock_std_devs = []
	muppet = 0
	standard_deviation_portfolio = .01
	
	
	
	for i in ticker:
		stock_prices_all = web.DataReader(i, data_source, start, end)
		stock_prices = stock_prices_all.loc[-stock_prices_all['Volume'].isin(volume)]
		stock_data.append(stock_prices)
			
	for b in stock_data:
		close_price_columns.append(b['Close'])
		banana = banana + 1
		
	for c in close_price_columns:
		koala = c.reset_index()
		better_close_price_columns.append(koala)
		
	for d in better_close_price_columns:
		candy = d['Close']
		final_close_price_columns.append(candy)
		
	for e in final_close_price_columns:
		honey = e.values
		cabbage.append(honey)
		
	for f in cabbage:
		f = f/f[0]
		celery.append(f)
		
	for g in celery:
		period_return.append(g[-1])
		
	

	temp_stock_matrix = np.vstack(celery)
	stock_matrix = temp_stock_matrix

	cov_matrix = np.cov(stock_matrix)
	inv_matrix = np.linalg.inv(cov_matrix)
	final_col = np.sum(inv_matrix, axis = 0)
	
	standardizing_factor = sum(final_col)
	weights = final_col/standardizing_factor
	print(weights)
	
	kangaroo = float(weights.size)
	joey = float(1/kangaroo)
	equal_portfolio = np.empty(weights.size); equal_portfolio.fill(joey)

	
	for item in stock_matrix:
		h = item * weights[muppet]
		individual_stock_std_dev.append(h)
		muppet +=1
			
	
	temp_stocks_std_devs = np.vstack(individual_stock_std_dev)
	stock_std_devs = temp_stocks_std_devs
	better_stock_std_devs = np.sum(stock_std_devs, axis = 0)
	standard_deviation_portfolio = np.std(better_stock_std_devs, axis = 0)
	total_MVP_return = np.dot(weights, period_return)
	print("Return of MVP portfolio: " + str(total_MVP_return))
	print("Volatility of MVP portfolio: " + str(math.sqrt(1/standardizing_factor)))
	total_equal_return = np.dot(equal_portfolio, period_return)
	print("Return of equally weighted portfolio: " + str(total_equal_return))
	print("Volatility of equally weighted portfolio: " + str(standard_deviation_portfolio))
	
	

	
	
if __name__ == "__main__":
	main()
