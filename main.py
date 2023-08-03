import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import yfinance as yf

st.set_page_config(layout='wide')


st.image('dados/banner3.jpg')
st.markdown('')
st.header('Ações - Análise Descritiva de dados financeiros')
st.markdown('')
st.markdown('Ações são partes pequenas de uma empresa que podem ser compradas e vendidas na bolsa de valores. Quando você compra uma ação, você se torna um "acionista" da empresa, o que significa que você possui uma pequena parte dela.')
@st.cache(allow_output_mutation=True)

def get_data(path):
    data = pd.read_csv(path)
    return data

#############################
######## Download ###########
#############################

acoes = ['CPLE6.SA', 'SAPR4.SA', 'VIVT3.SA', 'GRND3.SA', 'BBDC4.SA', 'PRIO3.SA', 'WEGE3.SA', 'BOVA11.SA']
acoes_df = pd.DataFrame()
for acao in acoes:
  acoes_df[acao] = yf.download(acao, start='2015-01-01')['Close']


#############################
######### Limpeza ###########
#############################

acoes_df.dropna(inplace=True)

acoes_df = acoes_df.rename(columns={'CPLE6.SA': 'COPEL', 'SAPR4.SA' : 'SANEPAR', 'VIVT3.SA' : 'VIVO', 'GRND3.SA' : 'GRENDENE', 'BBDC4.SA' : 'BRADESCO', 'PRIO3.SA' : 'PRIO', 'WEGE3.SA': 'WEGE', 'BOVA11.SA' : 'BOVA'})
acoes_df.to_csv('dados/acoes.csv')
acoes_df2 = pd.read_csv('dados/acoes.csv')
acoes_df = acoes_df.reset_index()

acoes_df2['Date'] = pd.to_datetime(acoes_df2['Date'],errors='coerce').dt.strftime("%d/%m/%Y")


# ------------- Valores do fechamento das ações -----------
st.divider()
st.subheader('Preço de fechamento das ações')

st.markdown('O mercado de ações é um dos pilares fundamentais do sistema financeiro global, sendo um espaço onde investidores'
 ' compram e vendem ações de empresas de capital aberto. Um dos principais indicadores utilizados nesse mercado é o'
 ' preço de fechamento das ações, que reflete o valor pelo qual os títulos de uma empresa são negociados ao final do'
 ' pregão. Esse preço é extremamente relevante para investidores, analistas e tomadores de decisão, pois fornece'
 ' informações cruciais para avaliar a saúde financeira de uma empresa, identificar tendências de mercado e tomar'
 ' decisões estratégicas de investimento.')
st.markdown('')
st.markdown('Veja abaixo o dataframe com o preço de fechamento de algumas ações')
st.markdown('')

st.dataframe(acoes_df2)
st.text('*Ações escolhidas aleatoriamente, portanto não é uma recomendação de mercado')

st.subheader('Estatísticas Descritivas')

st.dataframe(acoes_df2.describe())
st.divider()

st.subheader("Vizualização dos Dados")



nome_acoes = st.selectbox('Escolha uma das ações', ['COPEL - CPLE6.SA', 'SANEPAR - SAPR4.SA', 'VIVO - VIVT3.SA', 'GRENDENE - GRND3.SA ', 'BRADESCO / BBDC4.SA ', 'PRIO - PRIO3.SA', 'WEGE - WEGE3.SA', 'BOVA - BOVA11.SA'])


#############################
######### COPEL #############
#############################

if nome_acoes == 'COPEL - CPLE6.SA':
    st.markdown('')
    st.markdown('A **Copel** – Companhia Paranaense de Energia - gera, transmite, distribui e comercializa energia, além de atuar no segmento de telecomunicações. A empresa é uma das maiores companhias elétricas do Brasil. A posição de prestígio da Copel no setor elétrico brasileiro é o resultado de 64 anos de experiência e competência técnica nas áreas de geração, transmissão, distribuição e comercialização de energia.')


    st.markdown('**Distribuição de Frequência dos Preços**')
    fig, ax1 = plt.subplots(1,  figsize=(8, 6))
    plot = sns.histplot(acoes_df["COPEL"], ax=ax1, kde = True)
    st.pyplot(fig)

    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação COPEL')
    if desc:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['COPEL'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação COPEL**')
            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x = acoes_df['COPEL'], ax=ax1)
            st.pyplot(fig)


        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação COPEL',  y='COPEL', x='Date', width=850, height=450,
                          color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)


#############################
######### SANEPAR ###########
#############################

elif nome_acoes == 'SANEPAR - SAPR4.SA':
    st.markdown('')
    st.markdown('A **Companhia de Saneamento do Paraná (Sanepar)**, sediada em Curitiba, no Paraná, é uma sociedade de economia mista e de capital aberto, controlada pelo Estado do Paraná. É responsável pela prestação de serviços de saneamento básico a 345 cidades paranaenses, além de 297 localidades de menor porte.')
    st.markdown('')
    st.markdown('**Distribuição de Frequência dos Preços**')
    fig, ax1 = plt.subplots(1,  figsize=(4, 2))
    plot = sns.histplot(acoes_df["SANEPAR"], ax=ax1, kde = True)
    st.pyplot(fig)

    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação SANEPAR')
    if desc:


        col1, col2 = st.columns(2)

        with col1:

            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['SANEPAR'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação SANEPAR**')
            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x=acoes_df['SANEPAR'], ax=ax1)
            st.pyplot(fig)

        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação SANEPAR', y='SANEPAR', x='Date', width=850, height=450,
                          color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)




#############################
#########  vivo   ###########
#############################

elif nome_acoes == 'VIVO - VIVT3.SA':
    st.markdown('')
    st.markdown('A **Telefônica Brasil S.A.** é a maior empresa de telecomunicações do país, com atuação em âmbito nacional e com um portfólio de produtos completo e convergente (voz fixa e móvel, banda larga fixa e móvel, ultra banda larga, dados e serviços digitais, TV por assinatura e TI).')
    st.markdown('')
    st.markdown('**Distribuição de Frequência dos Preços**')

    fig, ax1 = plt.subplots(1,  figsize=(4, 2))
    plot = sns.histplot(acoes_df["VIVO"], ax=ax1, kde = True)
    st.pyplot(fig)

    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação VIVO')
    if desc:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['VIVO'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação VIVO**')
            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x=acoes_df['VIVO'], ax=ax1)
            st.pyplot(fig)


        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação VIVO', y='VIVO', x='Date', width=850, height=450,
                      color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)



##############################
######### GRENDENE ###########
##############################


elif nome_acoes == 'GRENDENE - GRND3.SA':
    st.markdown('')
    st.markdown('A **Grendene** é uma empresa brasileira do setor calçadista com sede em Sobral, Ceará. A empresa possui 5 plantas industriais e marcas famosas, como Grendha, Melissa, Ipanema, Rider, Zaxy, Cartago, Pega Forte e Nuar.')
    st.markdown('')
    st.markdown('**Distribuição de Frequência dos Preços**')

    fig, ax1 = plt.subplots(1,  figsize=(4, 2))
    plot = sns.histplot(acoes_df["GRENDENE"], ax=ax1, kde = True)
    st.pyplot(fig)

    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação GRENDENE')
    if desc:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['GRENDENE'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação GRENDENE**')

            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x=acoes_df['GRENDENE'], ax=ax1)
            st.pyplot(fig)


        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação GRENDENE', y='GRENDENE', x='Date', width=850, height=450,
                      color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)



##############################
######### BRADESCO ###########
##############################

elif nome_acoes == 'BRADESCO / BBDC4.SA':
    st.markdown('')
    st.markdown('O **Bradesco** é um banco brasileiro, fundado em 1943 na cidade de Marília, interior de São Paulo, por Amador Aguiar. É uma instituição de capital aberto, com um portfólio de produtos e serviços diversificados, destinados a todos os tipos de clientes e, cada vez mais, voltada à implementação de inovações e tecnologias para atender pessoas físicas e jurídicas.')
    st.markdown('')
    st.markdown('**Distribuição de Frequência dos Preços**')


    fig, ax1 = plt.subplots(1,  figsize=(4, 2))
    plot = sns.histplot(acoes_df["BRADESCO"], ax=ax1, kde = True)
    st.pyplot(fig)

    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação BRADESCO')
    if desc:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['BRADESCO'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação BRADESCO**')
            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x=acoes_df['BRADESCO'], ax=ax1)
            st.pyplot(fig)


        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação BRADESCO', y='BRADESCO', x='Date', width=850, height=450,
                      color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)



#############################
########## PRIO #############
#############################

elif nome_acoes == 'PRIO - PRIO3.SA':
    st.markdown('')
    st.markdown('A PRIO (antiga PetroRio) é uma empresa brasileira de capital aberto com foco na produção de petróleo e gás, no investimento e na recuperação de ativos em produção, especializada na gestão eficiente de reservatórios e no desenvolvimento de campos maduros. A Companhia é dedicada também à produção, exploração, comercialização e transporte de petróleo e gás natural.')
    st.markdown('')
    st.markdown('**Distribuição de Frequência dos Preços**')
    fig, ax1 = plt.subplots(1,  figsize=(4, 2))
    plot = sns.histplot(acoes_df["PRIO"], ax=ax1, kde = True)
    st.pyplot(fig)


    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação PRIO')
    if desc:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['PRIO'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação PRIO**')

            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x=acoes_df['PRIO'], ax=ax1)
            st.pyplot(fig)


        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação PRIO', y='PRIO', x='Date', width=850, height=450,
                      color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)



#############################
######### WEGE ##############
#############################

elif nome_acoes == 'WEGE - WEGE3.SA':
    st.markdown('')
    st.markdown('**WEG S.A** é uma empresa multinacional brasileira, foi fundada em 1961, com sede na cidade de Jaraguá do Sul, no estado de Santa Catarina. '
                ''
                'A empresa é uma das maiores fabricantes de equipamentos elétricos do mundo, atuando nas áreas de comando e proteção, variação de velocidade, automação de processos industriais, geração e distribuição de energia e tintas e vernizes industriais, entre outros produtos.')
    st.markdown('')
    st.markdown('**Distribuição de Frequência dos Preços**')
    fig, ax1 = plt.subplots(1,  figsize=(4, 2))
    plot8 = sns.histplot(acoes_df["WEGE"], ax=ax1, kde = True)
    st.pyplot(fig)

    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação WEGE')
    if desc:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['WEGE'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação WEGE**')

            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x=acoes_df['WEGE'], ax=ax1)
            st.pyplot(fig)


        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação WEGE', y='WEGE', x='Date', width=850, height=450,
                      color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)



#############################
######### BOVA ##############
#############################

else:
    st.markdown('')
    st.markdown('O **BOVA** é um ETF (Exchange Traded Funds) – uma carteira de ativos que utiliza um índice como base de referência – neste caso, o Índice Bovespa (IBOV).')
    st.markdown('É um fundo de índice que apresenta uma performance em linha com o IBOV, sendo uma forma de investir no Ibovespa.')
    st.markdown('Assim, o capital disponível para o fundo, proveniente das aplicações dos investidores, é distribuído para a compra de ações nas mesmas proporções do Índice Ibovespa.')
    st.markdown('')
    st.markdown('**Distribuição de Frequência dos Preços**')
    fig, ax1 = plt.subplots(1,  figsize=(4, 2))
    plot = sns.histplot(acoes_df["BOVA"], ax=ax1, kde = True)
    st.pyplot(fig)

    desc = st.checkbox('Exibir Mais Detalhes da Análise da Ação BOVA')
    if desc:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('**Estatísticas Descritivas**')
            st.write(acoes_df['BOVA'].describe())

        with col2:
            st.markdown('**Visualização do Histórico de Distribuição dos Valores da Ação BOVA**')

            fig, ax1 = plt.subplots(1)
            plot = sns.boxplot(x=acoes_df['BOVA'], ax=ax1)
            st.pyplot(fig)

        fig = px.line(acoes_df, title= 'Histórico dos Valores da Ação BOVA', y='BOVA', x='Date', width=850, height=450,
                      color_discrete_sequence=px.colors.qualitative.G10)
        fig.update_xaxes(tickangle=0)
        st.plotly_chart(fig)

st.divider()




#############################################################
############## Normalizado as ações #########################
#############################################################

acoes_df_normalizado = acoes_df.copy()
for i in acoes_df_normalizado.columns[1:]:
  acoes_df_normalizado[i] = acoes_df_normalizado[i] / acoes_df_normalizado[i][0]




#############################################################
######### Historico de todas as ações normalizado ###########
#############################################################
st.subheader('Histórico do Preço de Todas das Ações')
st.markdown('')
st.markdown('O histórico de preços das ações é de fundamental importância para investidores e analistas financeiros, pois fornece informações valiosas sobre o desempenho passado de uma empresa no mercado de ações. Esse histórico registra os preços pelos quais as ações foram negociadas ao longo do tempo, permitindo que os investidores analisem padrões e tendências que podem ajudar a tomar decisões informadas sobre investimentos futuros.')
st.markdown('')
fig = px.line( width=950, height=600,)
for i in acoes_df.columns[1:]:
  fig.add_scatter(x = acoes_df['Date'], y = acoes_df[i], name = i)
st.plotly_chart(fig)

st.markdown('Em suma, o histórico de preços das ações é uma ferramenta poderosa para entender'
 ' o comportamento do mercado e tomar decisões inteligentes no mundo dos investimentos.'
 ' No entanto, é importante lembrar que o desempenho passado não garante resultados futuros,'
 ' e uma análise completa deve ser realizada para uma tomada de decisão adequada.')
st.divider()
#############################################################
######### Historico de todas as ações normalizado ###########
#############################################################

st.subheader('Historico de todas as Ações - Preços Normalizado')
st.markdown('')
st.markdown('O preço de ações normalizado é uma ferramenta valiosa para os investidores, pois permite'
 ' uma melhor comparação de desempenho entre diferentes ações ou ao longo do tempo. '
 'Também ajuda a analisar tendências e tomar decisões informadas sobre investimentos, '
 'levando em conta as variações reais dos preços das ações.')
st.markdown('')
st.markdown('')
fig = px.line( width=950, height=600,)
for i in acoes_df_normalizado.columns[1:]:
  fig.add_scatter(x = acoes_df_normalizado['Date'], y = acoes_df_normalizado[i], name = i)
st.plotly_chart(fig)

st.markdown('Preço de ações normalizado refere-se a uma forma de apresentar o valor das ações de uma empresa'
            ' de maneira mais compreensível para os investidores. Em vez de simplesmente mostrar o preço atual'
            ' das ações em seu valor absoluto (por exemplo, R\$ 100), o preço normalizado é expresso como'
            ' um percentual em relação a um período de referência.'
            ' O processo de normalização é útil porque ajuda a eliminar a influência de fatores externos,'
            ' como a inflação ou mudanças no valor da moeda, permitindo que os investidores avaliem o desempenho'
            ' real das ações.')
st.markdown('Para normalizar o preço das ações, geralmente utiliza-se a seguinte fórmula simples:')
st.markdown('Preço Normalizado = (Preço Atual da Ação / Preço da Ação no Período de Referência) x 100')
st.markdown('O período de referência pode ser qualquer período escolhido, como um ano específico ou'
            ' o preço das ações em uma data específica. Por exemplo, se o preço de uma ação é de R\$ 120 hoje'
            ' e era de R\$ 100 no mesmo dia do ano passado, o preço normalizado seria:')
st.markdown('Preço Normalizado = (R\$ 120 / R$ 100) x 100 = 120\% ')
st.markdown(
            'Dessa forma, o preço normalizado mostra que o valor da ação aumentou em 20\%'
            ' em relação ao ano anterior.')