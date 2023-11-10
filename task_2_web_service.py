import re
import streamlit as st
from transformers import pipeline

# Декоратор @st.cache говорит Streamlit, что модель нужно загрузить только один раз, чтобы избежать утечек памяти
@st.cache_data
def load_model():
    return pipeline('fill-mask', model='xlm-roberta-base')

# Загружаем предварительно обученную модель
model = load_model()

st.title('Подбор подходящих определений вместо шаблона')

answer = st.text_input("Пожалуйста, напишите предложение, указав вместо подбираемого слова шаблон <mask>:")
all_ok = re.search("<mask>", answer)

if all_ok:
    result = model(answer)
    for i, sting in enumerate(result):
        st.write("Вариант ", i, ": ", sting['sequence'])



