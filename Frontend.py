import numpy as np
import streamlit as st
import pickle

loaded_model = pickle.load(open('model.pkl', 'rb'))

st.image("logo.jpg")

st.title('Agricultural Production Optimization Engine')

N = float(st.number_input("Ratio of Nitrogen in Soil"))
P = float(st.number_input("Ratio of Phosphorous in Soil"))
K = float(st.number_input("Ratio of Potassium in Soil"))
temperature = float(st.number_input("Temperature in celsius"))
Humidity = float(st.number_input("Humidity"))
Ph = float(st.number_input("Ph Level in soil"))
Rainfall = float(st.number_input("Rainfall in mm"))

if st.button("Predict Crop"):
    st.write("The Suggested crop for such climate is :")
    pred_result = loaded_model.predict(np.array([N, P, K, temperature, Humidity, Ph, Rainfall]).reshape(1, -1))

    print(np.argmax(pred_result))

    st.subheader(pred_result)

    if pred_result == "rice":
        st.image("rice-cultivation.jpg")
    elif pred_result == "maize":
        st.image("maize.jpg")
    elif pred_result == "cotton":
        st.image("cotton.jpg")
    elif pred_result == "apple":
        st.image("apple.jpg")
    elif pred_result == "grapes":
        st.image("grapes.jpg")
    elif pred_result == "watermelon":
        st.image("watermelon.jpg")
    elif pred_result == "mango":
        st.image("mango.jpg")
    elif pred_result == "muskmelon":
        st.image("muskmelon.jpg")
    elif pred_result == "banana":
        st.image("banana.jpg")
    elif pred_result == "coffee":
        st.image("coffee.jpg")
    elif pred_result == "jute":
        st.image("jute.jpg")
    elif pred_result == "lenti":
        st.image("lentil.jpg")
    elif pred_result == "coconut":
        st.image("coconut.jpg")
    elif pred_result == "chickpea":
        st.image("chickpea.jpg")
    elif pred_result == "orange":
        st.image("orange.jpg")
    elif pred_result == "pomegranate":
        st.image("pomegranate.jpg")
    elif pred_result == "papaya":
        st.image("papaya.jpg")
    elif pred_result == "kidney beans":
        st.image("kidney beans.jpg")
    elif pred_result == "pigeonpeas":
        st.image("pigeon peas.jpg")
    elif pred_result == "mothbeans":
        st.image("moth beans.jpg")
    elif pred_result == "mungbean":
        st.image("mung bean.jpg")
    else:
        st.image("black gram.jpg")

