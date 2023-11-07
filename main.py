
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
import wash_data
import get_data

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


def page_home():
    df_selected=data_selected()
    st.dataframe(df_selected)
    return None

def page_plot_bar():
    df_selected=data_selected()
    st.bar_chart(df_selected[['ApplicantIncome','LoanAmount']])
    return None

def page_plot_box():
    st.title('Boxplot')
    df_selected = data_selected()
    fig,ax=plt.subplots()
    st.pyplot(fig)
    return None

def page_plot_pie():
    df_selected = data_selected()
    df_selected_g=df_selected.groupby('Loan_Status')
    df=df_selected_g.count()
    fig,ax=plt.subplots()
    ax.pie(df['Loan_ID'],autopct="%1.1f%%")
    st.pyplot(fig)
    return None

def page_plot_heatmap():
    fig,ax=plt.subplots()
    df_selected=data_selected()
    variables=df_selected.columns.tolist()
    labels=df_selected.columns.tolist()
    cax=ax.matshow(df_selected,cmap='hot_r')
    fig.colorbar(cax)
    tick_spacing=1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_xticklabels(['']+list(df_selected.columns))
    ax.set_yticklabels(['']+list(df_selected.columns))    
    st.pyplot(fig)

def main():

    session_state=st.session_state
    if 'page' not in session_state:
        session_state['page']='Home'
    page=st.sidebar.radio('Navigate',['Home','Plot_bar','Plot_box','Plot_pie','Plot_heatmap'])
    
    if page=='Home':
        page_home()
    elif page=='Plot_bar':
        page_plot_bar()
    elif page=='Plot_box':
        page_plot_box()
    elif page=='Plot_pie':
        page_plot_pie()
    elif page=='Plot_heatmap':
        page_plot_heatmap()
                                      
main()
