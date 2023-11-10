#import io
import re
import streamlit as st
#from PIL import Image
#import numpy as np
#from tensorflow.keras.applications import EfficientNetB0
#from tensorflow.keras.preprocessing import image
#from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def load_model(text_to_fill):
    unmasker = pipeline('fill-mask', model='xlm-roberta-base')
    return unmasker(text_to_fill)

st.title('Подбор подходящих определений вместо шаблона')
st.echo(code_location=None)

#with st.echo("below"):
#with st.spinner(text="Думаем..."):
answer = st.text_input("Пожалуйста, напишите предложение, указав вместо подбираемого слова шаблон <mask>:")
match = re.search("<mask>", answer)
if match:
    result = load_model(text_to_fill = answer)
    st.write(result)


