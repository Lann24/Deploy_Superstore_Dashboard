# import streamlit as st

# st.set_page_config(
#     page_title = 'Mari belajar Streamlit',
#     layout='wide'
# )

# # Menulis teks di streamlit
# # st.code("Hello world!")

# st.title("Belajar Streamlit")
# st.header("Header")
# st.subheader("Subheader")
# st.text("Text")
# st.code(""" 
#     import numpy as np
#     import pandas as pd
# """)
# st.latex("y= 2x^2 + 3x + 5")
# st.markdown("# Title")
# st.markdown("## Subtitle")
# st.markdown("_italic_")
# st.markdown("__bold__")
# st.markdown("""
#     1. Pertama
#     2. Kedua
#     3. Ketiga
# """)
# st.markdown(
#     """
#     * Ini Bullet 1
#     * Ini Bullet 2
#     * Ini Bullet 3
#     """
# )
# st.markdown(
#     """
#     [google](https://google.com)
#     """
# )
# WIDGET <- Input elements
# st.header("Widget")

# ini_tombol = st.button("Tekan tombol ini")
# ini_tombol

# saya_setuju = st.checkbox("Centang jika setuju")
# if saya_setuju:
#     st.write("Anda setuju untuk belajar lebih giat")
# else:
#     st.write("Ayo belajar")

# # radio button, memilih salah satu opsi dari sekian opsi
# buah_favorit = st.radio(
#     "Pilihan buah favorit kamu",
#     ['Apel','Anggur','Jeruk','Mangga']
# )
# buah_favorit
# st.write(f"Buah kesukaanku adalah {buah_favorit}")
# # selectbox menampilkan menu dropdown untuk dipilih
# makanan = st.selectbox(
#     "Pilih makanan yang akan diorder",
#     ['Paket 1','Paket Goceng','Kids meal']
# )
# st.write(f"Anda akan mengorder {makanan}")

# # multiselect memungkinkan kita memilih multiple choices
# belanjaan = st.multiselect(
#     "Pilih item belanjaan kalian",
#     ['Terigu','Minyak goreng','Biskuit','Minuman']
# )
# belanjaan
# if len(belanjaan) > 0:
#     st.write(f"Pilihan pertama Anda adalah {belanjaan[0]}")

# # slider memungkinkan kita untuk memilih numerik input dengan range yang ditentukan
# parameter_alpha = st.slider(
#     "Insert alpha value",
#     min_value=0.0,
#     max_value=1.0,
#     step=0.1,
#     value=5.0
# )
# st.write(f"Parameter yang dipilih adalah {parameter_alpha}")
# # Jika input berupa kategorikal, kita dapat menggunakan select_slider
# ukuran_baju = st.select_slider(
#     "Ukuran baju",
#     ['SS','S','M','L','XL','XXL']
# )
# st.write(f"Ukuran baju yang dipilih adalah {ukuran_baju}")

# # number_input untuk input number
# kode_pos = st.number_input(
#     "Masukkan kode pos",
#     min_value=0,
#     max_value=999999,
#     step=1
# )
# kode_pos

# # Text input
# nama = st.text_input("Masukkan nama kalian")
# nama

# # Text area
# komentar = st.text_area("Masukkan komentar kamu")
# komentar

# # Input tanggal
# import datetime

# tanggal_lahir = st.date_input(
#     "Tanggal lahir"
# )
# tanggal_lahir

# # Input waktu
# jam_mulai = st.time_input("masukkan jam mulai", step=600)
# jam_mulai

# # Input warna
# warna = st.color_picker("masukkan warna")
# warna
# # Use HTML and inline CSS to set the color of the text
# styled_text = f'<span style="color:{warna};">Ini adalah text dengan warna yang dipilih.</span>'
# # Display the text using st.write
# st.write(styled_text, unsafe_allow_html=True)

# # Menampilkan media

# Image
# from PIL import Image

# image = Image.open("fight.jpg")
# st.image(
#     image,
#     caption="Battle of the Strongest"
# )
# Home exercise
# Tampilkan audio
# Tampilkan video

# container and layouting

# Kolom

# col1, col2, col3 = st.columns(3)

# with col1:
#     lahir_saya = st.date_input("Tanggal lahir kamu")

# with col2:
#     lahir_gebetan = st.date_input("Tanggal lahir dia")

# with col3:
#     jadian = st.date_input("Tangal jadian")

# # kolom dengan lebar custom
# kol1, kol2 = st.columns([2,6])

# with kol1:
#     lahir_aku = st.date_input("Tanggal lahir aku")

# with kol2:
#     lahir_kamu = st.date_input("Tanggal lahir dirinya")

# # sidebar
# with st.sidebar:
#     st.title("Titanic survival model explorer")
#     your_name = st.text_input("Enter your name")

#     with st.expander("Lorem ipsum"):
#         st.write("dolor sit amet")

# # Tabbing
# tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

# with tab1:
#     st.write("Tab 1: Lorem ipsum dolor sit amet")

# with tab2:
#     st.write("Tab 2: Lorem ipsum dolor sit amet")

# with tab3:
#     st.write("Tab 3: Lorem ipsum dolor sit amet")

# # Container
# custom_container = st.container(border=True)
# with custom_container:
#     st.write("ini teks di dalam container")

# st.write("SEDANGKAN teks ini di luar container")
# # Basic plotting
# import pandas as pd

# # Bar chart
# df = pd.DataFrame({
#     "name": ["A","B","C"],
#     "value": [1,2,3]
# })

# st.bar_chart(data=df, x="name", y="value")

# # Line plot
# df = pd.DataFrame({
#     "date": pd.date_range(start='2024-01-01', end='2024-01-10', freq='D'),
#     "value": [10,2,3,4,3,2,1,2,3,4]
# })

# st.line_chart(data=df, x="date", y="value")

# # scatter plot
# import numpy as np
# np.random.seed(42)
# random_numbers = np.random.uniform(0, 10, 200)

# df = pd.DataFrame({
#     "value1": random_numbers[:100],
#     "value2": random_numbers[100:]
# })

# st.scatter_chart(data=df, x="value1", y="value2")

# Home exercise: berikan centered title pada setiap plot di atas

# Selesai, tekan control+C pada terminal untuk mengakhiri app
# Lalu exit untuk turn off virtual environment
# import streamlit as st
# import pandas as pd
# import datetime as dt
# st.set_page_config(
#     page_title = "Superstore Dashboard",
#     layout="wide"
# )
# df = pd.read_csv('C:/Users/MSI GAMING/my_project/superstore.csv')
# df['order_year'] = df['order_date'].dt.year
# CURR_YEAR = df['order_year'].max()
# PREV_YEAR = CURR_YEAR - 1

# mx_data = pd.pivot_table(
#     data=df,
#     index='order_year',
#     aggfunc={
#         'sales':np.sum,
#         'profit':np.sum,
#         'order_id':pd.Series.nunique,
#         'custumoer_id':pd.Series.nunique
#     }

# ).reset_index()
# mx_data['profit_ratio'] = 100.0 * mx_data ['profit'] / mx_data ['sales']

import streamlit as st
import pandas as pd
import altair as alt
# from numerize import numerize

st.set_page_config(layout='wide')

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQMqC_6fkaH6oZweJDIIYFDdE9o3P3G1hB0OKLzkGGf0pB-FjWJoAMoYca2iXV2ID5dE7hoklCSx6hE/pub?gid=0&single=true&output=csv')

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

df['order_year'] = df['order_date'].dt.year

CURR_YEAR = max(df['order_date'].dt.year)
PREV_YEAR = CURR_YEAR - 1

st.title("Superstore Dashboard")
# st.write(CURR_YEAR)

# 1 periksa tahun terakhir dari data
# itung total sales, banyaknya order, banyaknya kosumen, profit %
# di tahun tersebut

data = pd.pivot_table(
    data=df,
    index='order_year',
    aggfunc={
        'sales':'sum',
        'profit':'sum',
        'order_id':pd.Series.nunique,
        'customer_id':pd.Series.nunique
    }
).reset_index()
data['profit_pct'] = 100.0 * data['profit'] / data['sales']
# st.dataframe(data)
def format_big_number(num):
    if num >= 1e6:
        return f"{num / 1e6:.2f} Mio"
    elif num >= 1e3:
        return f"{num / 1e3:.2f} K"
    else:
        return f"{num:.2f}"
mx_sales, mx_order, mx_customer, mx_profit_pct = st.columns(4)

with mx_sales:

    curr_sales = data.loc[data['order_year']==CURR_YEAR, 'sales'].values[0]
    prev_sales = data.loc[data['order_year']==PREV_YEAR, 'sales'].values[0]
    
    sales_diff_pct = 100.0 * (curr_sales - prev_sales) / prev_sales

    st.metric("Sales", value=format_big_number(curr_sales), delta=f'{sales_diff_pct:.2f}%')

with mx_order:

    curr_order = data.loc[data['order_year']==CURR_YEAR, 'order_id'].values[0]
    prev_order = data.loc[data['order_year']==PREV_YEAR, 'order_id'].values[0]
    
    order_diff_pct = 100.0 * (curr_order - prev_order) / prev_order

    st.metric("Order", value=format_big_number(curr_order), delta=f'{order_diff_pct:.2f}%')

with mx_customer:

    curr_customer = data.loc[data['order_year']==CURR_YEAR, 'customer_id'].values[0]
    prev_customer = data.loc[data['order_year']==PREV_YEAR, 'customer_id'].values[0]
    
    customer_diff_pct = 100.0 * (curr_customer - prev_customer) / prev_customer

    st.metric("Customer", value=format_big_number(curr_customer), delta=f'{customer_diff_pct:.2f}%')

with mx_profit_pct:

    curr_profit_pct = data.loc[data['order_year']==CURR_YEAR, 'profit_pct'].values[0]
    prev_profit_pct = data.loc[data['order_year']==PREV_YEAR, 'profit_pct'].values[0]
    
    profit_pct_diff_pct = 100.0 * (curr_profit_pct - prev_profit_pct) / prev_profit_pct

    st.metric("Profit Percentage", value=f'{curr_profit_pct:.2f}%', delta=f'{profit_pct_diff_pct:.2f}%')

st.header("Sales trend")
freq = st.selectbox("Freq", ['Harian','Bulanan'])

timeUnit = {
    'Harian':'yearmonthdate',
    'Bulanan':'yearmonth'
}

# altair membuat object berupa chart dengan data di dalam parameter
sales_line = alt.Chart(df[df['order_year']==CURR_YEAR]).mark_line().encode(
    alt.X('order_date', title='Order Date', timeUnit=timeUnit[freq]),
    alt.Y('sales', title='Revenue', aggregate='sum')
)

st.altair_chart(sales_line,use_container_width=True)

#BarChart
st.header("Category per Segment Performance")
bar_chart = alt.Chart(df[df['order_year']==CURR_YEAR]).mark_bar().encode(
    column='category:N',
    y='sum(sales):Q',
    color='segment:N',
    x='segment:N'
).properties(width=150, height=80)
st.altair_chart(bar_chart)

#ScatterPlot
st.header("Sales vs Profit Correlation")
_, midcol, _ = st.columns([1,2,1])
with midcol:
    scatter = alt.Chart(df[df['order_year']==CURR_YEAR]).mark_point().encode(
        x='sales:Q',
        y='profit:Q',
        color='region:N'
    )
st.altair_chart(scatter, use_container_width=True)

