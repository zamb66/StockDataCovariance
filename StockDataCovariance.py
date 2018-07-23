
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import numpy as np
import datetime 
import calendar

def main():

	start = datetime.date(2016, 1, 1)
	end = datetime.date(2016, 12, 31)

	ticker = ['AAPL']
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
			
	#time_array_AAPL.extend(time_array_AAPL)
	stock_prices['Date'] = time_array_AAPL
	print(stock_prices)
	all_monthly_data = month_separate(stock_prices)
	monthly_avg_prices = mean_calculator(all_monthly_data)
	print(monthly_avg_prices)

def month_separate(stock_prices):

	current_month = 0
	month_dict = {}
	month_array = [0]
	months_of_interest = [2,3,4,5,6,7,8,9,10,11,12]
	for index, row in stock_prices.iterrows():
		day_month = row['Date'].month
		print(day_month)
		print(current_month)
		day_month_name = calendar.month_name[day_month]
		if day_month == current_month:
			day_stats = pd.Series.to_frame(row)
			print(day_stats)
			month_array.append(day_stats)
		else:
			if day_month in months_of_interest:
				monthly_data = pd.concat(month_array, axis = 1)
				month_dict[last_month] = monthly_data
			month_array = []
			daily_data = pd.Series.to_frame(row)
			month_array.append(daily_data)
			current_month = day_month
			last_month = day_month_name
	
	monthly_data = pd.concat(month_array, axis = 1)
	month_dict[day_month_name] = monthly_data		
	
	return month_dict
	
def mean_calculator(all_monthly_data):

	data_per_month = list(all_monthly_data.values())
	name_of_months = list(all_monthly_data.keys())
	monthly_average_price = []
	index_mean = ["Mean Closing Price"]
	
	for i in data_per_month:
		list_end_prices = i.loc['Close',:]
		monthly_average_price.append(np.mean(list_end_prices))
	print(name_of_months)
	avg_price = pd.DataFrame(data=monthly_average_price, index = name_of_months, columns = index_mean)
	
	return avg_price
		
	
	
	
	
			
			



if __name__ == "__main__":
	main()
