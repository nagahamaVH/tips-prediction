import streamlit as st
import pandas as pd
import numpy as np
import pickle
from utils import struct_input
from texts import *

sb_period = ["Almoço", "Jantar"]
sb_day = ["Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
sb_sex = ["Masculino", "Feminino"]

model = pickle.load(open("src/model.pickle.dat", "rb"))

st.title("Qual será a minha gorjeta?")
st.markdown(subtitle)

input_bill = st.number_input('Conta a pagar', min_value=0.0)
input_group = st.number_input('Número de pessoas', min_value=1)
input_time = st.selectbox("Período", sb_period)
input_day = st.selectbox("Dia da semana", sb_day)
input_sex = st.selectbox('Gênero', sb_sex)
input_smoker = st.checkbox("Mesa para fumante", value=False)
predict_button = st.button("Predizer gorjeta")

if predict_button:
    data = struct_input(input_bill, input_sex, input_smoker, input_day, input_time, input_group)
    predict = model.predict(data)
    tip_pred = "Gorjeta estimada: " + str(np.round(predict[0], 2)) + " USD"

    st.subheader(tip_pred)

st.markdown("***")
st.markdown(about_app)
st.markdown(about_author)