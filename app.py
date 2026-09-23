import streamlit as st
from donor import add_donor

st.title("Food Donation Management System")
st.write("Help reduce food waste and support the community")

name = st.text_input("Donor name")
phone = st.text_input("Phone number")

if st.button("Add Donor"):
    add_donor()
    st.success("Donor Added")