
import pandas as pd
import numpy as np
import streamlit as st
import wash_data
import get_data

def main():

    x=st.sidebar.slider('The size of data:',0.0,1.0,1.0,0.01)
    df=wash_data.wash_data()
    df_selected=get_data.select_data(size=x)
    st.dataframe(df_selected)
    return None
    # radio('Pick one:', ['nose ','ear'])
    # st.selectbox('Select', [ 1, 2,3])
    # st.multiselect('Multiselect', [ 1, 2,3])
    # st.slider('Slide me', min_value=0, max_value=10)
    # st.select_slider('Slide to select', options=[ 1,'2'])
    # st.text_input('Enter some text')
    # st.number_input('Enter a number')
    # st.text_area('Area for textual entry')
    # st.date_input('Date input')
    # st.time_input('Time entry')
    # st.file_uploader('File uploader')
    #
    # st.camera_input("一二三,茄子!")
    # st.color_picker('Pick a color')

main()






