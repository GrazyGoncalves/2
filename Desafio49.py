import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CADASTRO_IES_2020.CSV', encoding='ISO-8859-1', sep=';', low_memory=False)



#Título 
st.title('Análise de Estudantes - Grupo 1')


#subtítulo
st.subheader('Bianca, Graziella, Evely, João, Milena')
st.dataframe(df)

#Bianca
st.subheader('Bianca')
state_counts_bianca = df['NO_UF_IES'].value_counts()
fig_bianca, ax_bianca = plt.subplots(figsize=(10, 6))
state_counts_bianca.plot(kind='line', title='Contagem de Alunos por Estado', ax=ax_bianca)
ax_bianca.set_xlabel('Estado')
ax_bianca.set_ylabel('Contagem de Alunos')

st.pyplot(fig_bianca)

st.write("Alguns dados interessantes da atualidade trazidos pelo Censo - 2020.No Brasil, 87,6% das instituições de educação superior são privadas. Há 304 IES públicas e 2.153 privadas Em relação às IES públicas, 42,4% estaduais; 38,8% federais e 18,8% municipais. A maioria das universidades é pública e entre as IES privadas, predominam as faculdades.")
# Evely
st.subheader('Evely')
state_counts_evely = df['NO_UF_IES'].value_counts()
fig_evely, ax_evely = plt.subplots(figsize=(10, 6))
state_counts_evely.plot(kind='bar', title='Contagem de Alunos por Estado', ax=ax_evely)
ax_evely.set_xlabel('Estado')
ax_evely.set_ylabel('Contagem de Alunos')

st.pyplot(fig_evely)

st.write("Quase três quintos das IES federais são universidades e 33,9% são Institutos Federais de Educação, Ciência e Tecnologia (IFs) e Centros Federais de Educação Tecnológica (Cefets).São 2.457 Instituições de educação superior no Brasil (atente-se que os dados são de 2020), das quais 77% são faculdades. As 203 universidades existentes no Brasil equivalem a 8,1% do total de IES.")

# Grazi
st.subheader('Graziella')
state_counts_graziella = df['NO_UF_IES'].value_counts()
fig_graziella, ax_graziella = plt.subplots(figsize=(10, 10))
state_counts_graziella.plot(kind='pie', title='Contagem de Alunos por Estado', ax=ax_graziella)
ax_graziella.set_facecolor('none')  # Define o fundo como transparente

st.pyplot(fig_graziella)

st.write("Por outro lado, 54,3% das matrículas de graduação estão concentradas nas universidades. Apesar do alto número de faculdades, nelas estão matriculados apenas 16,2% dos estudantes de graduação.")

#João
st.subheader('João')
state_counts_joao = df['NO_UF_IES'].value_counts()
fig_joao, ax_joao = plt.subplots(figsize=(10, 6))
state_counts_joao.plot(kind='line', marker='o', title='Contagem de Alunos por Estado', ax=ax_joao)
ax_joao.set_xlabel('Estado')
ax_joao.set_ylabel('Contagem de Alunos')
ax_joao.grid(True)
ax_joao.set_axisbelow(True)
for i, v in enumerate(state_counts_joao):
    ax_joao.text(i, v + 10, str(v), ha='center', va='bottom', fontsize=8, color='black')

st.pyplot(fig_joao)
st.write("Em 2020, 41.953 cursos de graduação e 25 cursos sequenciais são ofertados em 2.457 IES no Brasil. Em média, as IES oferecem 17,1 cursos de graduação Só 3,2% das Instituições de Educação Superior (IES) oferecem 100 ou mais cursos de graduação; um quarto delas ofertam até 2 cursos de graduação.")

#Milena
st.subheader('Milena')
qt_regiao = df.groupby('NO_REGIAO_IES')['QT_TEC_TOTAL'].sum()
fig_milena, ax_milena = plt.subplots(figsize=(10, 6)) 
qt_regiao.plot(kind='bar', color='purple', title='Relação de Estudantes por Região', ax=ax_milena)
ax_milena.set_xlabel('Regiões')
ax_milena.set_ylabel('Estudantes')

st.pyplot(fig_milena)

st.write("O grau acadêmico predominante dos cursos de graduação é o bacharelado e 85,3% dos cursos (de graduação) nas universidades são na modalidade presencial.")


#Link
st.markdown('[Leia mais](https://www.jacobsconsultoria.com.br/post/o-censo-da-educa%C3%A7%C3%A3o-superior-de-2020)')





