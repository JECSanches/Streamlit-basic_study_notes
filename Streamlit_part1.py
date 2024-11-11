import streamlit as st
import pandas as pd
import numpy as np

st.write('## Testando comandos, funções e plots')

st.write('#### 1 - Noções sobre estado de sessão')
"st.sesseion_state object:", st.session_state

# Adicionando widgets (slider)
st.write('##### - Adicionando slider')
num = st.slider('Número', 1, 10, key='slider')
st.write(st.session_state)

# Adicionando botões
st.write('##### - Adicionando botões')
col1, buff, col2 = st.columns([1, 0.5, 3])
option_names = ['a', 'b', 'c']

# definindo um botão para a próxima opção
next = st.button('Next option')
if next:
    if st.session_state['radio_option'] == 'a':
        st.session_state.radio_option = 'b'
    elif st.session_state['radio_option'] == 'b':
        st.session_state.radio_option = 'c'
    else:
        st.session_state.radio_option = 'a'

option = col1.radio('Escolha uma opção', option_names, key='radio_option')
st.session_state

if option == 'a':
    col2.write('Você escolheu a opção "a" :smile:')
elif option == 'b':
    col2.write('Você escolheu a opção "b" :heart:')
else:
    col2.write('Você escolheu a opção "c" :rocket:')


# Conhecendo "on_change" e "on_click"
# on_change (input widgets) - st.slider ; st.number_input
# on_click (one-off widgets) - st.button; st.form_submit_button
st.write('#### 2 - "on_change" e "on_click"')
# Criando um widget para converter dois números
st.write('Convertendo massa ("lbs" - "kg")')

# Definindo as funções

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

col1, buff, col2 = st.columns([1,2,3])
with col1:
    kilogram = st.number_input('Kilograms:', key='kg',
                                on_change = kg_to_lbs)
    

with col2:
    pounds = st.number_input('Pounds:', key='lbs',
                            on_change = lbs_to_kg)
    






st.write('#### 3 - Gráfico de mapa para determinados pontos')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.write('DataFrame')
df
st.map(df)


st.write('#### 3.2 - Adicionando cores e tamanhos aos indicadores')
df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    }
)

'''DataFrame'''
df
"""Mapa"""
st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")


st.write('#### 4 - Carregando banco de dados por URL')
@st.cache_data # cria uma cópia dos dados em cada chamada de função
               # Lento somente na primeira execução, as demais são quase instantâneas.
# Carregando datasets
def load_data(url):
    df = pd.read_csv(url) # carrega o conjunto de dados
    return df 
#Aplicando a função 
url = 'https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv'
df = load_data(url)

st.write('Utilizando "@st.cache_data" - cria uma cópia dos dados em cada chamada da função.'
        ' Desta forma, é "lento" somente na primeira execução, as demais são quase instantâneas.')
st.write('URL:', url)
st.dataframe(df)
st.button('Rerun')


