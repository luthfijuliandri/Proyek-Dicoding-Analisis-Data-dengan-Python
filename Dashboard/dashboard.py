import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df_day = pd.read_csv("https://raw.githubusercontent.com/luthfijuliandri/Proyek-Dicoding-Analisis-Data-dengan-Python/main/Dashboard/day_new.csv")


st.write(df_day.head())


def plot_1():

    yr_2011 = df_day[df_day['yr'] == 0]
    yr_2012 = df_day[df_day['yr'] == 1]

    mnth_2011 = yr_2011.groupby('mnth')['cnt'].sum()
    mnth_2012 = yr_2012.groupby('mnth')['cnt'].sum()

    # Plotting
    fig, bar = plt.subplots(figsize=(12, 6))
    bar.plot(mnth_2011.index, mnth_2011, label='2011', color='blue')
    bar.plot(mnth_2012.index, mnth_2012, label='2012', color='red')
    bar.set_title('Perbandingan Penyewaan Sepeda Berdasarkan Bulan pada Tahun 2011 dan 2012')
    bar.set_xlabel('Month')
    bar.set_ylabel('Total Penyewa Sepeda')
    bar.legend()
    st.pyplot(fig)

def plot_2():
 
    cnt_workingday = df_day[df_day['workingday'] == 1]['cnt'].sum()
    cnt_weekend = df_day[df_day['workingday'] == 0]['cnt'].sum()

    # Plotting
    fig, bar = plt.subplots(figsize=(8, 6))
    bar.bar(['Working Day', 'Weekend'], [cnt_workingday, cnt_weekend], color=['blue', 'green'])
    bar.set_title('Perbandingan Jumlah Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan')
    bar.set_ylabel('Total Penyewa Sepada')
    bar.set_xlabel('Hari')
    st.pyplot(fig)

def plot_3():
   
    cnt_season = df_day.groupby('season')['cnt'].sum()

    # Plotting
    fig, bar = plt.subplots(figsize=(8, 6))
    bar.bar(cnt_season.index, cnt_season, color=['blue', 'green', 'orange', 'red'])
    bar.set_title('Pengaruh Musim terhadap Penyewaan Sepeda')
    bar.set_ylabel('Total Penyewa Sepeda')
    bar.set_xlabel('Season')
    st.pyplot(fig)

def plot_4():
  
    cnt_weekday = df_day.groupby('weekday')['cnt'].sum()

    # Plotting
    fig, bar = plt.subplots(figsize=(10, 6))
    bar.bar(cnt_weekday.index, cnt_weekday, color='blue')
    bar.set_title('Distribusi jumlah penyewaan sepeda berdasarkan hari dalam seminggu')
    bar.set_ylabel('Total Penyewa Sepeda')
    bar.set_xlabel('Hari')
    st.pyplot(fig)

# Streamlit main
def main():
    st.title('Bike Rental Analysis Dashboard')

    # dropdown
    visualization_option = st.selectbox('Select Visualization', ['Perbandingan Penyewaan Sepeda Berdasarkan Bulan pada Tahun 2011 dan 2012',
                                                                'Perbandingan Jumlah Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan',
                                                                'Pengaruh Musim terhadap Penyewaan Sepeda',
                                                                'Distribusi jumlah penyewaan sepeda berdasarkan hari dalam seminggu'])

    if visualization_option == 'Perbandingan Penyewaan Sepeda Berdasarkan Bulan pada Tahun 2011 dan 2012':
        plot_1()
    elif visualization_option == 'Perbandingan Jumlah Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan':
        plot_2()
    elif visualization_option == 'Pengaruh Musim terhadap Penyewaan Sepeda':
        plot_3()
    elif visualization_option == 'Distribusi jumlah penyewaan sepeda berdasarkan hari dalam seminggu':
        plot_4()

if __name__ == '__main__':
    main()
