import streamlit as st
import pandas as pd
import numpy as np
from utils import struct_input
import pickle

sb_period = ["Almoço", "Jantar"]
sb_day = ["Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
sb_sex = ["Masculino", "Feminino"]

st.title("Predição de gorjetas")

input_bill = st.number_input('Conta a pagar', min_value=0.0)
input_group = st.number_input('Número de pessoas', min_value=1)
input_time = st.selectbox("Período", sb_period)
input_day = st.selectbox("Dia da semana", sb_day)
input_sex = st.selectbox('Gênero', sb_sex)
input_smoker = st.checkbox("Mesa para fumante", value=False)
predict_button = st.button("Predizer gorjeta")

model = pickle.load(open("model.pickle.dat", "rb"))

if predict_button:
    data = struct_input(input_bill, input_sex, input_smoker, input_day, input_time, input_group)
    
    predict = model.predict(data)

    tip_pred = "Gorjeta estimada: " + str(np.round(predict[0], 2))
    st.write(tip_pred)
