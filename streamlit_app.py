import streamlit as st

st.title("QILAKKKKK")
st.write(
    "sman 20"
)
st.image("IMG_5598.jpeg",width=200)



st.tittle("Aplikasi Sederhana")
st.header ("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:",value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
