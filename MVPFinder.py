import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import numpy as np
import datetime 
import calendar
import math
import time
import scipy.stats as st

def main():

	program_start = time.time()
	start = datetime.date(2018, 1, 1)
	end = datetime.date(2018, 7, 26)

	ticker = ['TSLA','GM','F','NFLX','FB','PYPL','NVDA','V','GE','TWTR','CE','FIT','GPRO','XXII','GRPN','WMT','KO','COKE','BA','VZ']
	volume = [0]
	data_source = 'morningstar'
	stock_data = []
	close_price_columns = []
	better_close_price_columns = []
	final_close_price_columns = []
	celery = []
	cabbage = []
	stock_matrix = []
	period_return = []
	individual_stock_std_dev = []
	stock_std_devs = []
	better_stock_std_devs = []
	probability_positive_returns = []
	muppet = 0
	banana = 0
	standard_deviation_portfolio = .01
	
	
	
	temp_stock_prices_all = web.DataReader(ticker, data_source, start, end)
	stock_prices_all = temp_stock_prices_all.reset_index()
	stock_prices = stock_prices_all.loc[-stock_prices_all['Volume'].isin(volume)]
	stock_tickers = stock_prices['Symbol'].unique()
	
	for i in stock_tickers:
		individual_stock_prices = stock_prices.loc[stock_prices['Symbol']==i] 
		stock_data.append(individual_stock_prices)
		close_price_columns.append(stock_data[banana]['Close'])
		koala = close_price_columns[banana].reset_index()
		candy = koala['Close']
		final_close_price_columns.append(candy)
		honey = final_close_price_columns[banana].values
		cabbage.append(honey)
		apple = cabbage[banana]
		apple = (apple/apple[0])-1
		celery.append(apple)
		period_return.append(apple[-1])
		print(period_return)
		banana +=1

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
		h = item * equal_portfolio[muppet]
		individual_stock_std_dev.append(h)
		muppet +=1
			
	
	temp_stocks_std_devs = np.vstack(individual_stock_std_dev)
	stock_std_devs = temp_stocks_std_devs
	better_stock_std_devs = np.sum(stock_std_devs, axis = 0)
	standard_deviation_portfolio = np.std(better_stock_std_devs, axis = 0)
	total_MVP_return = np.dot(weights, period_return)
	total_MVP_volatility = math.sqrt(1/standardizing_factor)
	print("Return of MVP portfolio: " + str(total_MVP_return))
	print("Volatility of MVP portfolio: " + str(total_MVP_volatility))
	total_equal_return = np.dot(equal_portfolio, period_return)
	print("Return of equally weighted portfolio: " + str(total_equal_return))
	print("Volatility of equally weighted portfolio: " + str(standard_deviation_portfolio))
	MVP_positive_probability = prob_positive(total_MVP_return, total_MVP_volatility)
	Equal_positive_probability = prob_positive(total_equal_return, standard_deviation_portfolio)
	print("Probability of positive returns of MVP portfolio: " + str(MVP_positive_probability))
	print("Probability of positive returns of the equally weighted portfolio: " + str(Equal_positive_probability))

def prob_positive(calculated_mean, calculated_std):
	probability_positive = 1-st.norm(calculated_mean, calculated_std).cdf(0)
	return probability_positive
		
	
if __name__ == "__main__":
	main()
