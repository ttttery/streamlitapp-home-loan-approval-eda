# import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
import wash_data
import get_data

def page_home():
    df_selected=data_selected()
    st.dataframe(df_selected)
    return None

def page_plot_bar():
    df_selected=data_selected()
    st.bar_chart(df_selected[['ApplicantIncome','LoanAmount']])
    return None

def page_plot_box():
    df_selected = data_selected()
    # px.box(df_selected,x='Is_graduate',y='LoanAmount')
    st.title('Boxplot')
    return None

def data_selected():
    x = st.sidebar.slider('The size of data:', 0.0, 1.0, 1.0, 0.01)
    df = wash_data.wash_data()
    is_graduate = st.sidebar.selectbox('Graduate', [None, True, False])
    is_married = st.sidebar.selectbox('Married', [None, True, False])
    is_female = st.sidebar.selectbox('Female', [None, True, False])
    is_self_employed = st.sidebar.selectbox('Self_employed', [None, True, False])
    is_urban = st.sidebar.selectbox('Urban', [None, True, False])
    credit_history = st.sidebar.selectbox('Credit_History', [None, True, False])
    df_selected = get_data.select_data(x, is_graduate, is_married, is_female, is_self_employed, is_urban,
                                       credit_history)
    return df_selected


def main():

    session_state=st.session_state
    if 'page' not in session_state:
        session_state['page']='Home'
    page=st.sidebar.radio('Navigate',['Home','Plot_bar','Plot_box'])
    
    if page=='Home':
        page_home()
    elif page=='Plot_bar':
        page_plot_bar()
    elif page=='Plot_box':
        page_plot_box()                      
                                      
main()
