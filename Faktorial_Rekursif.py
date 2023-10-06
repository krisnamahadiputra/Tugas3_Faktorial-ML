import streamlit as st

st.set_page_config(page_title="Faktorial Rekursif", page_icon="🧮")
st.title("Perhitungan Faktorial Secara Rekursif")

def faktorial(n):
    #base case
    if n == 0:
        return 1, "1"
    
    #recursive case
    else:
        subhasil, subpenjabaran = faktorial(n - 1) #fungsi faktorial() dipanggil kembali secara rekursif
        hasil = n * subhasil

        #kondisi khusus agar hasil penjabaran dari 1! tidak dituliskan (agar tidak menjadi ...* 2 * 1 * 1)
        if n == 1:
            penjabaran = f"{subpenjabaran}" 
        else:
            penjabaran = f"{n} * {subpenjabaran}"

        return hasil, penjabaran

with st.form(key='input angka'): #form dalam streamlit
    n = int(st.number_input("Masukkan Angka", step=1)) #input bilangan 
    submitted = st.form_submit_button("Hitung Faktorial") #tombol/button untuk men-submit form sebelumnya

if submitted: #tombol "Hitung Faktorial" telah diklik
    st.subheader(f"Hasil Perhitungan {n}!") #subheader

    #error handling ketika bilangan yang di-input bernilai negatif (< 0)
    if n < 0:
        st.error("Faktorial tidak tersedia untuk angka negatif.")

    #proses perhitungan dilakukan ketika bilangan yang di-input positif
    else:
        hasil, penjabaran = faktorial(n)
        st.write(f"{n}! = {penjabaran}")
        st.success(f"{n}! = {hasil}")
