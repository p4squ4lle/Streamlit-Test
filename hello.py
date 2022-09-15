import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write('# Hello')
st.write('This is a streamlit web-app for testing purposes.')

x = np.linspace(-3, 3, 100)
y = np.exp(-x**2/2)
z = np.transpose([x, y])

df = pd.DataFrame(z, columns=["x", "y"])
df
st.line_chart(df, x='x', y='y')

#fig, ax = plt.subplots()
#st.pyplot(fig)
