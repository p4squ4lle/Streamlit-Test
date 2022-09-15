import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from serial.tools import list_ports
import serial
import time

st.write('# Hello')
st.write('This is a streamlit web-app for testing purposes.')

ports = list_ports.comports()
serPortsDescription = [p.description for p in ports]
serPortDescription = st.selectbox('Choose the com port:', serPortsDescription)

#ser = serial.Serial('COM3', 9600, timeout=1)
#ser.close()

connectButton = st.button('connect')
if connectButton:
    serPort = ports[serPortsDescription.index(serPortDescription)]
    ser = serial.Serial(serPort.device, 9600, timeout=1)

disconnectButton = st.button('disconnect')
i = 0;
while connectButton and i <10:
    i += 1
    if ser==None:
        continue
    if ser.is_open:
        st.write(ser.readline())
    time.sleep(0.5)

ser.close()




#x = np.linspace(-3, 3, 100)
#y = np.exp(-x**2/2)
#z = np.transpose([x, y])

#df = pd.DataFrame(z, columns=["x", "y"])
#df
#st.line_chart(df, x='x', y='y')

#fig, ax = plt.subplots()
#st.pyplot(fig)
