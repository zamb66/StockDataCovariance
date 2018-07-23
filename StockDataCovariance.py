
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import numpy as np
import datetime 
import calendar

def main():

	start = datetime.date(2016, 1, 1)
	end = datetime.date(2016, 12, 31)

	ticker = ['AAPL','AMZN']
	volume = [0]
	data_source = 'morningstar'

	stock_prices_all = web.DataReader(ticker, data_source, start, end)
	stock_prices = stock_prices_all.loc[-stock_prices_all['Volume'].isin(volume)]
	index_series = stock_prices.index.values

	time_array_AAPL = []
	stock_string = 'AAPL'
	for i in index_series:
		current_string = i[0]
		if current_string == stock_string:
			time_array_AAPL.append(i[1])
			
	time_array_AAPL.extend(time_array_AAPL)
	Date_Column = pd.Series(time_array_AAPL)
	#  Date_Column not being copied to the pandas dataframe below 
	print(Date_Column)
	stock_prices['Date'] = pd.DataFrame(Date_Column, index = stock_prices.index)
	print(stock_prices)
	print(stock_prices['Date'].isnull())
	#month_separate(stock_prices)

def month_separate(stock_prices):

	current_month = 0
	month_dict = {}
	for index, row in stock_prices.iterrows():
		day_month = row['Date'].month
		day_month_name = calendar.month_name[day_month]
		if day_month == current_month:
			day_stats = pd.Series.to_frame(name = row)
			month_dict[day_month_name].append(day_stats)
		else:
			day_month_name = pd.Series.to_frame(name=row)
			month_dict[day_month_name] = day_month_name
	
	return month_dict
			
			



if __name__ == "__main__":
	main()
