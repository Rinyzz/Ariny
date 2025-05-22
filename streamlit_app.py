import streamlit as st

st.title("Bagaimana cara berteman")
st.write(
    "Gimana ya :v"
)


st.image("9a24d48eafa6ba090c13cb91bcda5323-6462152e08a8b53812152342.jpg")
st.image("39568f388d8fb70c33681c332fc9060b.jpg")

st.title("Bingung sumpah")
st.Header("Ngitung apa y?")

angka = st.number_input("Ngitungngitung:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")

else :
    st.write(f"{angka} adalah Bilangan Ganjil")
