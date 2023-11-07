import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
    plt.style.use("ggplot")
    df_selected=data_selected()
    st.bar_chart(df_selected[['ApplicantIncome','LoanAmount']])
    return None

def page_plot_box():
    plt.style.use("ggplot")
    st.title('Boxplot')
    df_selected = data_selected().drop('Loan_ID',axis=1)
    df_x=df_selected[['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents']]
    df_y=df_selected.drop(['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents'],axis=1)
    choice_x=st.selectbox('x variable',df_x.columns.tolist())
    choice_y=st.selectbox('y variable',df_y.columns.tolist())
    s=sns.catplot(x=choice_x,y=choice_y,kind='box',data=df_selected)
    st.pyplot(s)
    return None

def page_plot_pie():
    plt.style.use("ggplot")
    df_selected = data_selected()
    df_x=df_selected[['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents']]
    choice_x=st.selectbox('Ways to classify',df_x.columns.tolist())
    df_selected_g=df_selected.groupby(choice_x)
    df=df_selected_g.count()
    fig,ax=plt.subplots()
    labels=[]
    if df.shape[0]==0:
        st.text('The dataset that you selected is empty, please give up some selectors.')
        return None
    # elif choice_x=='Dependents':
    #     labels=[f'{choice_x}:0',f'{choice_x}:1',f'{choice_x}:2',f'{choice_x}:3+']
    else:
        for i in range(0,df.shape[0]):
            labels.append(f'{choice_x}:{i}')
    ax.pie(df['Loan_ID'],labels=labels,autopct="%1.1f%%")
    st.pyplot(fig)
    return None

def page_plot_heatmap():
    plt.style.use("ggplot")
    fig,ax=plt.subplots()
    df_selected=data_selected()
    df=df_selected.drop(['Loan_ID'],axis=1)
    cols=df.corr().abs().nlargest(9, 'Loan_Status')['Loan_Status'].index
    cm=df_selected[cols].corr()
    variables=cols.tolist()
    labels=cols.tolist()
    cax=ax.matshow(cm,cmap='hot_r')
    fig.colorbar(cax)
    tick_spacing=1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_xticklabels(['']+variables)
    ax.set_yticklabels(['']+labels)    
    st.pyplot(fig)
    return None
    
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
