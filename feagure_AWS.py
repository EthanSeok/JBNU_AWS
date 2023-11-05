import pandas as pd
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import seaborn as sns
import os

## windows
font_path = "C:/Windows/Fonts/KoPubDotumMedium.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['axes.unicode_minus'] = False
rc('font', family=font)

## mac
# rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False

size = 11.5
params = {'legend.fontsize': size,
          'axes.labelsize': size * 1.5,
          'axes.titlesize': size * 1.2,
          'xtick.labelsize': size,
          'ytick.labelsize': size,
          'axes.titlepad': 12}
plt.rcParams.update(params)

def daily_temperature_diff(df):
    daily_temperature_diff = df['Temp'].resample('D').apply(lambda x: x.max() - x.min())
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=daily_temperature_diff.index, y=daily_temperature_diff.values, linewidth=2.5)
    plt.title('일교차')
    plt.xlabel('Date')
    plt.ylabel('일교차(°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_dir_txt = "./output/fig"
    if not os.path.exists(output_dir_txt):
        os.makedirs(output_dir_txt)
    plt.savefig(f'{output_dir_txt}/daily_temperature_diff.png')
    plt.close()

def temp_total(df):
    daily_avg_temp = df['Temp'].resample('D').mean()
    daily_max_temp = df['Temp'].resample('D').max()
    daily_min_temp = df['Temp'].resample('D').min()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=daily_avg_temp.index, y=daily_avg_temp.values, label='평균 온도', linewidth=2.5)
    sns.lineplot(x=daily_max_temp.index, y=daily_max_temp.values, label='최대 온도', linewidth=2.5)
    sns.lineplot(x=daily_min_temp.index, y=daily_min_temp.values, label='최저 온도', linewidth=2.5)

    plt.title('날짜별 온도 통계')
    plt.xlabel('Date')
    plt.ylabel('온도(°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()

    output_dir_txt = "./output/fig"
    if not os.path.exists(output_dir_txt):
        os.makedirs(output_dir_txt)
    plt.savefig(f'{output_dir_txt}/temp_total.png')
    plt.close()

def rainfall(df):
    daily_rainfall = df['Rainfall'].resample('D').sum()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=daily_rainfall.index.date, y=daily_rainfall.values, color='blue')
    plt.title('날짜별 강수량')
    plt.xlabel('Date')
    plt.ylabel('강수량($mm$)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_dir_txt = "./output/fig"
    if not os.path.exists(output_dir_txt):
        os.makedirs(output_dir_txt)
    plt.savefig(f'{output_dir_txt}/rainfall.png')
    plt.close()

def radn_plot(df):
    daily_radn = df['Radn'].resample('D').max()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=daily_radn.index, y=daily_radn.values, linewidth=2.5, color='orange')
    plt.title('날짜별 광량')
    plt.xlabel('Date')
    plt.ylabel('광량($W/m^2$)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_dir_txt = "./output/fig"
    if not os.path.exists(output_dir_txt):
        os.makedirs(output_dir_txt)
    plt.savefig(f'{output_dir_txt}/radn_plot.png')
    plt.close()


def humid(df):
    print(df['Humid'])
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Time', y='Humid', data=df, linewidth=2.5, color='purple')
    plt.title('시간별 습도')
    plt.xlabel('Time')
    plt.ylabel('습도 (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_dir_txt = "./output/fig"
    if not os.path.exists(output_dir_txt):
        os.makedirs(output_dir_txt)
    plt.savefig(f'{output_dir_txt}/humid.png')
    plt.close()

def main():
    df = pd.read_csv('check.csv')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Time'] = pd.to_datetime(df['Timestamp']).dt.hour
    df = df[df['Timestamp'].dt.month >= 10]
    df.set_index('Timestamp', inplace=True)

    print(df.describe())
    print(df.info())
    daily_temperature_diff(df)
    temp_total(df)
    rainfall(df)
    radn_plot(df)
    humid(df)

if __name__=='__main__':
    main()