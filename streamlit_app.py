import streamlit as st

st.title("beruang kutub")
st.write(
    "beruang kutub gemes imut lucu."
)
st.image("ee5a551e64a7f75074e7e8d9f67c5a5f.jpg",width=200)
st.header("nilai genap ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1) 
if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap") 
else:
    st.write(f"{angka} adalah Bilangan Ganjil")

