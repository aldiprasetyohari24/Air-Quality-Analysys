import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Dashboard",
    layout="wide",  # Set layout to 'wide' untuk tampilan lebar
    initial_sidebar_state="expanded"
)

PRSA_DataAvg_ModePerMonth = pd.read_csv("dashboard/PRSA_DataAvg_ModePerMonth.csv", sep=",", encoding="utf-8")
# PRSA_DataAvg_ModePerYear= pd.read_csv("PRSA_DataAvg_ModePerYear.csv", sep=",", encoding="utf-8")
min_date=PRSA_DataAvg_ModePerMonth["month_year"].min()
max_date=PRSA_DataAvg_ModePerMonth["month_year"].max()
# st.write(min_date,max_date)

with st.sidebar:
    # st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.markdown(
        """
        <style>
        .rounded-image {
            border-radius: 15px;
            border: 2px solid #ccc;
            padding: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            max-width: 100%;
            height: auto; 
        }
        </style>
        <img src="https://raw.githubusercontent.com/AldiPrasetyoHari/Air-Quality-Analysys/main/Ilustrasipengukurankualitasudara.jpg"
        class="rounded-image">
        <style>
        .linkedin-logo {
            display: flex;
            align-items: center;
        }
        .linkedin-logo img {
            width: 24px; /* Ukuran logo */
            margin-right: 10px; /* Jarak antara logo dan teks */
        }
        .linkedin-logo a {
            text-decoration: none;
            color: #0077b5; /* Warna LinkedIn */
            font-size: 14px;
        }
        </style>
        <style>
        .doku-logo {
            display: flex;
            align-items: center;
        }
        .doku-logo img {
            width: 24px; /* Ukuran logo */
            margin-right: 10px; /* Jarak antara logo dan teks */
        }
        .doku-logo a {
            text-decoration: none;
            color: #0077b5; /* Warna LinkedIn */
            font-size: 14px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # st.image("https://raw.githubusercontent.com/AldiPrasetyoHari/Air-Quality-Analysys/main/Ilustrasipengukurankualitasudara.jpg")
    # Meminta input rentang waktu
    date_range = st.date_input(
        label="Pilih Rentang Waktu Data",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    try:
        if start_date or end_date: 
            pass
    except NameError:
        start_date=min_date
        end_date=max_date

    # Periksa apakah pengguna sudah selesai memilih kedua tanggal
    if len(date_range) < 2:
        # st.info("Silakan pilih rentang tanggal lengkap (Mulai dan Selesai).")
        st.info("Please select the complete date range (Start and End).")
        
    else:
        start_date, end_date = date_range
        if start_date > end_date:
            # st.error("Tanggal mulai tidak boleh lebih besar dari tanggal selesai.")
            st.error("The start date cannot be later than the end date.")
        else:
            # st.success(f"Rentang Tanggal: {start_date} hingga {end_date}")
            st.success(f"Date Range: {start_date} to {end_date}")
            # Tambahkan logika lain untuk memproses data berdasarkan rentang tanggal
    
    
    # Menampilkan informasi referensi saat tombol ditekan
    st.markdown(
        """
        <div style="display: flex; align-items: flex-end;">
            <img src="https://raw.githubusercontent.com/AldiPrasetyoHari/Air-Quality-Analysys/main/doku.png" alt="Dokumen Logo" style="width: 30px; margin-right: 10px; vertical-align: bottom;">
            <span style="font-size: 14px;">Referensi :</span>
        </div>
        <span style="font-size: 14px; font-style: italic;">
        Chen, S. (2017). Beijing Multi-Site Air Quality [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5RK5G.
        <a href="https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data" target="_blank">[Link]</a><br>
        Li, Y., Tang, Y., Fan, Z., Zhou, H., & Yang, Z. (2017). Assessment and comparison of three different air quality indices in China. Environmental Engineering Research, 23, 21-27.
        <a href="https://www.semanticscholar.org/paper/Assessment-and-comparison-of-three-different-air-in-Li-Tang/42ef17eef5a39ce971d5b76c976924c9162dcbbe?utm_source=direct_link" target="_blank">[Link]</a><br>
        Ren, L., Yang, W., & Bai, Z. (2017). Characteristics of Major Air Pollutants in China. Advances in experimental medicine and biology, 1017, 7-26.
        <a href="https://www.semanticscholar.org/paper/Characteristics-of-Major-Air-Pollutants-in-China.-Ren-Yang/31fdb8c32f635ba103183e269919ecffe2fdb4ee?utm_source=direct_link" target="_blank">[Link]</a><br>
        Zhang, S., Guo, B., Dong, A., He, J., Xu, Z., & Chen, S.X. (2017). Cautionary tales on air-quality improvement in Beijing. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 473. [Link](https://doi.org/10.5678/health.rev.2021.09876)
        <a href="https://www.semanticscholar.org/paper/Cautionary-tales-on-air-quality-improvement-in-Zhang-Guo/59c99a7bf19617b43be0aa9f492def8c80ffae19?utm_source=direct_link" target="_blank">[Link]</a><br>
        Air Pollutant Units and Conversion Factors.
        <a href="https://www2.environment.nsw.gov.au/topics/air/understanding-air-quality-data/units-and-conversion-factors" target="_blank">[Link]</a><br>
        Air Quality.
        <a href="https://www.epa.vic.gov.au/for-community/environmental-information/air-quality" target="_blank">[Link]</a><br>
        </span><br><br>
        <div class="linkedin-logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn Logo">
            <a href="https://www.linkedin.com/in/aldi-prasetyo-hari/" target="_blank">Aldi Prasetyo Hari</a>
        </div><br>
        <div style="display: flex; align-items: center; margin-right: 15px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub Logo" style="width: 30px; margin-right: 10px;">
            <a href="https://github.com/AldiPrasetyoHari/Air-Quality-Analysys" target="_blank" style="font-size: 14px;">GitHub Profile</a>
        </div><br>
        """,
        unsafe_allow_html=True,
    )
    

tab1, tab2= st.tabs(["Dashboard Time Series", "Dashboard Air Quality Parameter"])

with tab1:
    # st.markdown(f"<p style='font-size: 12px;text-align: justify;font-style: italic;'>Data yang ditampilkan merupakan data dalam rentang waktu : {start_date} hingga {end_date} , Jika ingin menyesuaikan silahkan pilih tanggal melalui Sidebar di samping kiri anda.</p>", unsafe_allow_html=True)
    # st.markdown(f"<p style='font-size: 14px;text-align: justify;'>Anda dapat mengamati bagaimana historical data dari setiap station untuk setiap parameter pollutant yang digunakan atau bahkan dibandingkan dengan parameter cuaca yang ada. \
                Namun perlu diperhatikan terdapat ketentuan dalam konfigurasi pilihan antara station, parameter pollutant dan parameter cuaca. Ketentuan tersebut akan memunculkan pesan otomatis sehingga anda dapat menyesuaikan kembali konfigurasi yang dipilih.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 12px;text-align: justify;font-style: italic;'>The data displayed is within the time range: {start_date} to {end_date}. If you wish to adjust it, please select the dates through the Sidebar on your left.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 14px;text-align: justify;'>You can observe the historical data from each station for every pollutant parameter used or even compare it with the available weather parameters. \
    However, please note that there are specific rules in the configuration choices between stations, pollutant parameters, and weather parameters. These rules will trigger an automatic message, allowing you to adjust the selected configuration accordingly.</p>", unsafe_allow_html=True)
    # st.write(f"Data yang ditampilkan merupakan data dalam rentang waktu : {start_date} hingga {end_date} , Jika ingin menyesuaikan silahkan pilih tanggal melalui Sidebar di samping kiri anda.")
    # Daftar station dan parameter polutan
    stations = PRSA_DataAvg_ModePerMonth["station"].unique()
    stations = sorted(stations)  # Sort stations alphabetically
    parameter_pollutant = ["CO", "NO2", "SO2", "O3", "PM2.5", "PM10"]

    # Streamlit UI untuk memilih station dan parameter
    stations_with_all = ["Select All"] + list(stations)

    # Filter untuk memilih station
    # selected_stations = st.multiselect("Pilih Station Pengamatan", options=stations_with_all, default=[stations_with_all[0]])
    selected_stations = st.multiselect("Select Observation Station", options=stations_with_all, default=[stations_with_all[0]])

    # Filter untuk memilih parameter polutan
    # selected_parameters_pollutant = st.multiselect("Pilih Parameter Pollutant", options=parameter_pollutant, default=["PM2.5"])
    selected_parameters_pollutant = st.multiselect("Select Pollutant Parameter", options=parameter_pollutant, default=["PM2.5"])

    # Checkbox untuk parameter cuaca
    # show_selectbox = st.checkbox('Bandingkan dengan parameter cuaca')
    show_selectbox = st.checkbox('Compare with Weather Parameters')

    # Pengecekan jika parameter cuaca aktif
    if show_selectbox:
        if "Select All" in selected_stations or not selected_stations:
            # st.warning("Anda hanya boleh memilih salah satu station saat parameter cuaca diaktifkan.")
            st.warning("You can only select one station when the weather parameter is enabled.")
            selected_stations = ["Aotizhongxin"]  # Kosongkan pilihan jika 'Pilih Semua' dipilih

        # Pastikan hanya satu parameter cuaca yang dipilih
        selected_parameter_cuaca = st.selectbox('Pilih Parameter Cuaca', ['PRES', 'TEMP', 'DEWP', 'RAIN'], key="cuaca")

        if len(selected_parameters_pollutant) > 1:
            st.warning("Hanya satu parameter polutan yang bisa dipilih jika parameter cuaca diaktifkan. Parameter polutan pertama yang dipilih akan digunakan.")
            selected_parameters_pollutant = selected_parameters_pollutant[:1]  # Ambil parameter pertama yang dipilih

        # Batasi hanya satu station yang dapat dipilih saat parameter cuaca diaktifkan
        if len(selected_stations) > 1:
            st.warning("Hanya satu station yang dapat dipilih saat parameter cuaca diaktifkan.")
            selected_stations = selected_stations[:1]  # Ambil station pertama yang dipilih

    else:
        selected_parameter_cuaca = None

    # Filter data berdasarkan pilihan station
    if not selected_stations or selected_stations[0] == "Pilih Semua":
        stations = stations
    else:
        stations = selected_stations

    if not selected_parameters_pollutant:
        selected_parameters_pollutant=["PM2.5"]

    # Membuat plot dengan dua sumbu Y jika parameter cuaca dipilih
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Membuat daftar warna solid untuk station (polutan)
    # solid_colors_pollutant = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

    # Membuat daftar warna solid untuk parameter cuaca
    solid_colors_weather = ['tab:cyan', 'tab:lime', 'tab:orange', 'tab:purple']

    # Pengecekan jika lebih dari dua parameter polutan dipilih
    if len(selected_parameters_pollutant) > 2:
        print("Warning: Hanya dua parameter polutan yang dapat dipilih. Parameter lebih dari dua tidak akan ditampilkan.")
        selected_parameters_pollutant = selected_parameters_pollutant[:2]  # Ambil hanya dua parameter pertama

    # Warna untuk setiap station (pastikan memiliki cukup warna)
    solid_colors_pollutant = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#17becf', '#e377c2']

    # Membuat color map untuk kombinasi station dan parameter polutan
    color_map = {}

    # Kombinasikan index station dan polutan untuk mendapatkan warna yang unik
    for i, station in enumerate(stations):
        for j, param in enumerate(selected_parameters_pollutant):
            # Kombinasi warna untuk station dan parameter polutan
            color_map[(station, param)] = solid_colors_pollutant[(i * len(selected_parameters_pollutant) + j) % len(solid_colors_pollutant)]

    # Menyiapkan figure dan axes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Jika dua parameter dipilih, sumbu Y kedua digunakan
    if len(selected_parameters_pollutant) == 2:
        ax2 = ax1.twinx()  # Membuat sumbu Y kedua
        
    

    PRSA_DataAvg_ModePerMonth=PRSA_DataAvg_ModePerMonth[(PRSA_DataAvg_ModePerMonth['month_year']>=str(start_date)) & (PRSA_DataAvg_ModePerMonth['month_year']<=str(end_date))]

    # Plot untuk parameter polutan (sumbu Y pertama)
    for station in stations:
        station_data = PRSA_DataAvg_ModePerMonth[PRSA_DataAvg_ModePerMonth['station'] == station]
        
        # Plot parameter polutan pertama di sumbu Y pertama
        param = selected_parameters_pollutant[0]
        color = color_map[(station, param)]
        ax1.plot(
            station_data['month_year'],
            station_data[param],  # Gunakan parameter polutan yang dipilih
            label=f"{station} - {param}",
            marker='o',
            color=color,  # Warna berdasarkan kombinasi station dan parameter
            linestyle='-',  # Garis solid
        )

        # Jika ada dua parameter, plot parameter kedua di sumbu Y kedua
        if len(selected_parameters_pollutant) == 2:
            param = selected_parameters_pollutant[1]
            color = color_map[(station, param)]
            ax2.plot(
                station_data['month_year'],
                station_data[param],  # Gunakan parameter polutan yang dipilih
                label=f"{station} - {param}",
                marker='x',
                color=color,  # Warna berdasarkan kombinasi station dan parameter
                linestyle='--',  # Garis putus-putus untuk membedakan
            )

    # Label untuk sumbu Y pertama (polutan)
    ax1.set_xlabel('Bulan-Tahun')
    ax1.set_ylabel(f'Rata-rata {selected_parameters_pollutant[0]} ug/m^3', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Label untuk sumbu Y kedua (jika ada dua parameter)
    if len(selected_parameters_pollutant) == 2:
        ax2.set_ylabel(f'Rata-rata {selected_parameters_pollutant[1]} ug/m^3', color='tab:red')
        ax2.tick_params(axis='y', labelcolor='tab:red')

    # Menambahkan legend untuk sumbu Y pertama dan kedua
    ax1.legend(title='Station - Pollutant (1st)', fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    if len(selected_parameters_pollutant) == 2:
        ax2.legend(title='Station - Pollutant (2nd)', fontsize=10, bbox_to_anchor=(1.05, 0.05), loc='upper left')

    # Mengatur jumlah tick pada sumbu X
    from matplotlib.ticker import MaxNLocator
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True, prune='lower', nbins=12))  # Mengatur jumlah tick pada sumbu X


    # Jika parameter cuaca dipilih, buat sumbu Y kedua
    if selected_parameter_cuaca:
        ax2 = ax1.twinx()  # Membuat sumbu Y kedua
        for i, station in enumerate(stations):
            station_data = PRSA_DataAvg_ModePerMonth[PRSA_DataAvg_ModePerMonth['station'] == station]
            ax2.plot(
                station_data['month_year'],
                station_data[selected_parameter_cuaca],
                label=f"{station} - {selected_parameter_cuaca}",
                marker='x', linestyle='--',
                color=solid_colors_weather[i % len(solid_colors_weather)]  # Gunakan warna solid untuk cuaca
            )

        # Label untuk sumbu Y kedua (cuaca)
        ax2.set_ylabel(f'Rata-rata {selected_parameter_cuaca}', color='tab:red')
        ax2.tick_params(axis='y', labelcolor='tab:red')

        # Menambahkan legend untuk sumbu Y kedua
        ax2.legend(title='Station - Cuaca', fontsize=10, bbox_to_anchor=(1.05, 0), loc='upper left')

    # Menambahkan rotasi pada tanggal dan memastikan tampilan label sumbu X cukup lebar
    fig.autofmt_xdate(rotation=45)

    # Menyusun layout agar tidak ada yang tumpang tindih
    plt.tight_layout()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)
with tab2:
    st.markdown(f"<p style='font-size: 12px;text-align: justify;font-style: italic;'>Data yang ditampilkan merupakan data dalam rentang waktu : {start_date} hingga {end_date} , Jika ingin menyesuaikan silahkan pilih tanggal melalui Sidebar di samping kiri anda.</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 14px;text-align: justify;'>Anda dapat mengamati station mana saja yang memiliki proporsi kategori tertinggi dan terendah berdasarka level kategori yang telah ditentukan. Kategori ini merupakan klasifikasi yang dibuat berdasarkan literatur jurnal termasuk dalam formulasi limit level kategorinya.\
                Level kategori memiliki hierarki terendah ke tertinggi yakni Extremly Poor, Very Poor, Poor, Fair, dan Good. Sebagai contoh untuk rentang tanggal 2013/03/01 - 2017/02/01 untuk parameter PM2.5 Lowest diperoleh station Dongsi pada urutan pertama. Meskipun secara proporsi ia hanya bernilai 6.25% namun secara hierarki Extremely Poor memiliki priority nomor 1\
                sehingga insight yang dapat diperoleh yakni pada station Dongsi harus dilakukan penanganan terlebih dahulu karena memiliki parameter kualitas PM2.5 yang Extremly poor, disusul oleh station berikutnya.<br>\
                <br>Adapun untuk Highest berarti ia memiliki kualitas paling baik yang didasarkan pada hierarki level Good, Fair, Poor, Very Poor, dan Extremely Poor. Dimana dapat diartiak selama rentang data 2013/03/01 - 2017/02/01 di station Dingling secara proporsi 25% memperoleh kualitas PM2.5 yang Good disusul oleh station dengan proporsi kualitas PM2.5 terbaik kedua selama rentang data tersebut.</p>", unsafe_allow_html=True)
    PRSA_DataAvg_ModePerMonth=PRSA_DataAvg_ModePerMonth[(PRSA_DataAvg_ModePerMonth['month_year']>=str(start_date)) & (PRSA_DataAvg_ModePerMonth['month_year']<=str(end_date))]
    # Pilih kolom yang diperlukan
    df = PRSA_DataAvg_ModePerMonth[["station", "CO_Category", "NO2_Category", "SO2_Category", "O3_Category", "PM2.5_Category", "PM10_Category"]]

    # Membuat fungsi untuk menghitung proporsi kategori per parameter dan station
    def calculate_category_proportions(df, category_column, parameter):
        # Menghitung jumlah kategori per station dan kategori
        category_counts = df.groupby(['station', category_column])[category_column].count().reset_index(name='count')
        
        # Menghitung total per station untuk menghitung proporsi
        total_counts = category_counts.groupby('station')['count'].transform('sum')
        
        # Menambahkan kolom proporsi
        category_counts['proporsi'] = (category_counts['count'] / total_counts) * 100
        
        # Menambahkan kolom parameter untuk setiap kategori
        category_counts['parameter'] = parameter
        
        return category_counts[['station', 'parameter', category_column, 'proporsi']].rename(columns={category_column: 'kategori'})

    # Menghitung proporsi untuk setiap parameter
    co_proportions = calculate_category_proportions(df, 'CO_Category', 'CO')
    pm25_proportions = calculate_category_proportions(df, 'PM2.5_Category', 'PM2.5')
    pm10_proportions = calculate_category_proportions(df, 'PM10_Category', 'PM10')
    no2_proportions = calculate_category_proportions(df, 'NO2_Category', 'NO2')
    so2_proportions = calculate_category_proportions(df, 'SO2_Category', 'SO2')
    o3_proportions = calculate_category_proportions(df, 'O3_Category', 'O3')

    # Menggabungkan semua proporsi menjadi satu DataFrame
    all_proportions = pd.concat([co_proportions, pm25_proportions, pm10_proportions, no2_proportions, so2_proportions, o3_proportions])
    # st.write(PRSA_DataAvg_ModePerMonth)

    def tampilan_param(dfSource,parameter,opsi):
        # Menyaring berdasarkan parameter yang dipilih
        dfTabel = dfSource[dfSource["parameter"] == parameter]

        # Menambahkan kolom persentase
        dfTabel["proportion (%)"] = dfTabel["proporsi"].apply(lambda x: f"{x:.2f}%")

        # Menyusun urutan kategori untuk Top 5 (Good -> Fair -> Poor -> Very Poor -> Extremely Poor)
        category_orderTop = ["Good", "Fair", "Poor", "Very Poor", "Extremely Poor"]

        # Mengubah kolom kategori menjadi kategori dengan urutan yang sudah ditentukan untuk Top 5
        dfTabel['kategori'] = pd.Categorical(dfTabel['kategori'], categories=category_orderTop, ordered=True)

        # Sorting untuk Top 5 (kategori lebih baik terlebih dahulu, lalu proporsi tertinggi)
        df_sortedTop = dfTabel.sort_values(by=["kategori", "proporsi"], ascending=[True, False]).reset_index(drop=True)

        # Mengambil Top 5 dari data yang sudah diurutkan
        top_5 = df_sortedTop.head(5).reset_index(drop=True)

        # Menyusun urutan kategori untuk Bottom 5 (Extremely Poor -> Very Poor -> Poor -> Fair -> Good)
        category_orderBottom = ["Extremely Poor", "Very Poor", "Poor", "Fair", "Good"]

        # Mengubah kategori di dfTabel menjadi urutan untuk Bottom 5
        dfTabel['kategori'] = pd.Categorical(dfTabel['kategori'], categories=category_orderBottom, ordered=True)

        # Sorting untuk Bottom 5 (kategori lebih buruk terlebih dahulu, lalu proporsi terendah dalam kategori tersebut)
        df_sortedBottom = dfTabel.sort_values(by=["kategori", "proporsi"], ascending=[False, True]).reset_index(drop=True)

        # Mengambil Bottom 5 dari data yang sudah diurutkan
        bottom_5 = df_sortedBottom.tail(5).reset_index(drop=True)

        # Filter bottom_5 untuk menghilangkan data yang sudah ada di top_5 (untuk menghindari duplikasi)
        filtered_bottom_5 = bottom_5[~bottom_5['station'].isin(top_5['station'])].sort_values(by=["kategori","proporsi"],ascending=[True,False]).reset_index(drop=True)
        
        # Gabungkan filtered_bottom_5 dengan top_5 dan pastikan hasilnya sudah sesuai dengan urutan kategori yang diinginkan
        final_result = pd.concat([top_5, filtered_bottom_5], ignore_index=True) \
            .sort_values(by=["kategori", "proporsi"], ascending=[False, False]) \
            .reset_index(drop=True)

        df=dfSource[dfSource["parameter"]==parameter]
        # Menambahkan kolom persentase
        df["proportion (%)"] = df["proporsi"].apply(lambda x: f"{x:.2f}%")

        # # Sorting untuk mendapatkan top 5 dan bottom 5
        # df_sorted = df.sort_values(by="proporsi", ascending=False)
        # top_5 = df_sorted.head(5).reset_index(drop=True)
        # bottom_5 = df_sorted.tail(5).reset_index(drop=True).sort_values(by="proporsi",ascending=True)
        if(opsi=="col1"):
            st.markdown(f"<h3 style='font-size: 16px;text-align: center;'>Lowest Proportion of Quality Category {parameter}</h3>", unsafe_allow_html=True)
            st.table(filtered_bottom_5[["station", "kategori","proportion (%)"]])
            
        elif(opsi=="col2"):
            st.markdown(f"<h3 style='font-size: 16px;text-align: center;'>Highest Proportion of Quality Category {parameter}</h3>", unsafe_allow_html=True)
            st.table(top_5[["station", "kategori","proportion (%)"]])
            # st.write("Bottom 5 Data", bottom_5)
        elif(opsi=="col3"):

            # Menghitung jumlah kategori berdasarkan parameter yang sama
            category_counts = df.groupby(["parameter", "kategori"]).size().reset_index(name="count")

            # Menghitung total jumlah kategori berdasarkan parameter
            total_counts = df.groupby("parameter")["kategori"].count().reset_index(name="total")

            # Menggabungkan kedua hasil di atas untuk mendapatkan persentase
            category_counts = category_counts.merge(total_counts, on="parameter")
            category_counts["percentage"] = (category_counts["count"] / category_counts["total"]) * 100


            # # Pilih parameter untuk ditampilkan
            # parameter = st.selectbox("Pilih Parameter untuk Pie Chart", df['parameter'].unique())

            # Filter data berdasarkan parameter yang dipilih
            filtered_data = category_counts[category_counts['parameter'] == parameter]
            st.markdown(f"<h3 style='font-size: 16px;text-align: center;'>Proportion of Quality Parameter {parameter}</h3>", unsafe_allow_html=True)
            # st.subheader("Proportion of Quality Parameter Category")
        
            # Filter data berdasarkan parameter yang dipilih
            filtered_data = category_counts[category_counts['parameter'] == parameter]
            # Membuat Pie Chart
            fig, ax = plt.subplots()
            ax.pie(
                filtered_data['percentage'],
                labels=filtered_data['kategori'],
                autopct='%1.1f%%',
                startangle=90,
                colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#ff3399']  # Warna untuk kategori
            )
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Menampilkan Pie Chart
            st.pyplot(fig)
    
    def scorecard_param(df, col_param):
        # Mengelompokkan data berdasarkan kategori dan menghitung rata-rata
        df_filtered = df.groupby(f"{col_param}_Category")[f"{col_param}"].mean().reset_index()
        df_filtered.columns = ["Kategori", "Rata-rata"]

        # Membuat dictionary untuk menyimpan nilai rata-rata berdasarkan kategori
        categories = ["Good", "Fair", "Poor", "Very Poor", "Extremely Poor"]
        colors = {
            "Good": "#007BFF",       # Biru
            "Fair": "#28a745",       # Hijau
            "Poor": "#ffc107",       # Kuning
            "Very Poor": "#fd7e14",  # Oranye
            "Extremely Poor": "#dc3545"   # Merah
        }
        score_dict = {category: "-" for category in categories}

        # Mengisi dictionary dengan nilai rata-rata dari kategori yang tersedia
        for _, row in df_filtered.iterrows():
            if row["Kategori"] in score_dict:
                if not pd.isna(row["Rata-rata"]):  # Periksa jika nilai bukan NaN
                    score_dict[row["Kategori"]] = f"{row['Rata-rata']:.2f}"

        # Menampilkan hasil ke dalam 5 kolom di baris yang sama
        cols = st.columns(len(categories))  # Membuat 5 kolom
        for i, category in enumerate(categories):
            with cols[i]:
                # st.metric(label=category, value=score_dict[category])
                # Membuat card kustom dengan HTML dan CSS
                st.markdown(
                f"""
                <div style="
                    border: 1px solid #ddd; 
                    border-radius: 10px; 
                    padding: 5px; 
                    text-align: center; 
                    background-color: #f9f9f9; 
                    position: relative; 
                    height: 70px;  /* Tinggi lebih kecil */
                    display: flex; 
                    flex-direction: column; 
                    justify-content: flex-end;  /* Dekatkan angka ke bawah */
                    align-items: center;">
                    <div style="font-size: 14px; font-weight: bold; color: #333; margin-bottom: auto;">{category}</div>
                    <div style="font-size: 20px; font-weight: bold; color: {colors[category]};">{score_dict[category]}</div>
                    <div style="font-size: 10px; color: grey; position: absolute; bottom: 3px; right: 5px;">In PPM Units</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    with st.container():
        parampa="PM2.5"
        st.markdown(f"<h2 style='font-size: 36px;text-align: center;'>Air Quality Parameters {parampa}</h2>", unsafe_allow_html=True)
        # st.write(all_proportions[all_proportions["parameter"]=="PM2.5"])
        with st.container():
            scorecard_param(PRSA_DataAvg_ModePerMonth, "PM2.5")
            col1, col2, col3, col4, col5 = st.columns(5)
            
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                tampilan_param(all_proportions, parampa, "col1")
                
            # Tabel Top 5
            with col2:
                tampilan_param(all_proportions, parampa, "col2") 
            
            with col3:
                tampilan_param(all_proportions, parampa, "col3")
    
    
    with st.container():
        parampa="PM10"
        st.markdown(f"<h2 style='font-size: 36px;text-align: center;'>Air Quality Parameters {parampa}</h2>", unsafe_allow_html=True)
        # st.write(all_proportions[all_proportions["parameter"]=="PM2.5"])
        with st.container():
            scorecard_param(PRSA_DataAvg_ModePerMonth, parampa)
            col1, col2, col3, col4, col5 = st.columns(5)
            # with col1:
            #     st.write("a")
            # with col2:
            #     st.write("b")
            # with col3:
            #     st.write("b")
            # with col4:
            #     st.write("d")
            # with col5:
            #     st.write("e")
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                tampilan_param(all_proportions, parampa, "col1")
                
            # Tabel Top 5
            with col2:
                tampilan_param(all_proportions, parampa, "col2") 
            
            with col3:
                tampilan_param(all_proportions, parampa, "col3")

    with st.container():
        parampa="CO"
        st.markdown(f"<h2 style='font-size: 36px;text-align: center;'>Air Quality Parameters {parampa}</h2>", unsafe_allow_html=True)
        with st.container():
            scorecard_param(PRSA_DataAvg_ModePerMonth, parampa)
            col1, col2, col3, col4, col5 = st.columns(5)
            # with col1:
            #     st.write("a")
            # with col2:
            #     st.write("b")
            # with col3:
            #     st.write("b")
            # with col4:
            #     st.write("d")
            # with col5:
            #     st.write("e")
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                tampilan_param(all_proportions, parampa, "col1")
                
            # Tabel Top 5
            with col2:
                tampilan_param(all_proportions, parampa, "col2") 
            
            with col3:
                tampilan_param(all_proportions, parampa, "col3")
            
    with st.container():
        parampa="NO2"
        st.markdown(f"<h2 style='font-size: 36px;text-align: center;'>Air Quality Parameters {parampa}</h2>", unsafe_allow_html=True)
        with st.container():
            scorecard_param(PRSA_DataAvg_ModePerMonth, parampa)
            col1, col2, col3, col4, col5 = st.columns(5)
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                tampilan_param(all_proportions,parampa , "col1")
            with col2:
                tampilan_param(all_proportions, parampa, "col2")
            with col3:
                tampilan_param(all_proportions, parampa, "col3")
    
    with st.container():
        parampa="SO2"
        st.markdown(f"<h2 style='font-size: 36px;text-align: center;'>Air Quality Parameters {parampa}</h2>", unsafe_allow_html=True)
        with st.container():
            scorecard_param(PRSA_DataAvg_ModePerMonth, parampa)
            col1, col2, col3, col4, col5 = st.columns(5)
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                tampilan_param(all_proportions,parampa , "col1")
            with col2:
                tampilan_param(all_proportions, parampa, "col2")
            with col3:
                tampilan_param(all_proportions, parampa, "col3")
    
    with st.container():
        parampa="O3"
        st.markdown(f"<h2 style='font-size: 36px;text-align: center;'>Air Quality Parameters {parampa}</h2>", unsafe_allow_html=True)
        # st.write(all_proportions[all_proportions["parameter"]==parampa])
        with st.container():
            scorecard_param(PRSA_DataAvg_ModePerMonth, parampa)
            col1, col2, col3, col4, col5 = st.columns(5)
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                tampilan_param(all_proportions,parampa , "col1")
            with col2:
                tampilan_param(all_proportions, parampa, "col2")
            with col3:
                tampilan_param(all_proportions, parampa, "col3")

st.markdown(
    """
    <style>
    .center-caption {
        text-align: center; /* Teks di tengah */
        font-size: 0.8rem; /* Ukuran font yang sesuai untuk caption */
        color: gray; /* Warna teks */
        margin-top: 20px; /* Memberi jarak dari elemen atas */
    }
    </style>
    <div class="center-caption">Copyright APH24 &copy; 2025</div>
    """,
    unsafe_allow_html=True,
)

# st.caption('Copyright APH24 (c) 2025')
