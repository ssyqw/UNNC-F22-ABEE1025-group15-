import pandas as pd 
import datetime as dt
import matplotlib.date as mdates 
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str)
     if date_str[-8:-6] != '24':
     	dt_obj = pd.to_datetime(date_str)
     else:
     	date_str = date_str[0: -8] + '00' + date_str[-6:]
     	dt_obj = pd.to_datetime(date_str) + dt.timedelta(days=1)
     return dt_obj

def plot_1D_results(output_paths, plot_column_name,
					y_axis_title, plot_title):
	fig, axs =plt.subplots(1, 1, figsize=(20,10))
	fontsize = 20
	for key in output_paths           
		this_path =
		this_df = pd.read_csv(this_path)
		this_df['Date/Time'] = '2002' + this_df['Date/Time']
		this_df['Datetime'] = this_df['Date/Time'].apply(eplus_to_datetime)
		date_st_date = this_df.iloc[0]['Date/Time']
		date_ed_date = this_df.iloc[-1]['Date/Time']
		date_list = this_df['Date/Time']
		this_y = this_df[plot_column_name].values
		axs_plot(date_list)
