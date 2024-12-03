import matplotlib.pyplot as plt
import streamlit as st

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)


# Layout das etapas
tab0, tab1, tab2 = st.tabs(["Análise",
                            "Crise Financeira",
                            "Geopolítica"])
with tab0:


    '''
    ## Análise
    O mercado de petróleo tem se mostrado altamente volátil ao longo das últimas décadas. A análise da série temporal, que abrange desde os primeiros dados históricos até os dias atuais, revela padrões de flutuação significativos. São apresentados os valores médios, mínimos e máximos, tanto para a série completa quanto para os últimos 12 meses. O dashboard inclui, ainda, um histograma da distribuição dos preços do barril de petróleo, além de séries temporais sobre o consumo e a produção de petróleo, com destaque para eventos políticos que impactaram negativamente o mercado.

    Até o início da década de 2000, o preço do barril de petróleo jamais ultrapassou a marca de 30 dólares, com uma estabilidade relativa no mercado, salvo por um breve período no início dos anos 1990, marcado pela Guerra do Golfo, que afetou a região do Kuwait.

    Com o agravamento dos conflitos no Oriente Médio, particularmente com a crescente tensão entre grupos como a Al-Qaeda e países ocidentais, especialmente os Estados Unidos, o preço do barril começou a subir de forma acelerada a partir da década de 2000. Diversos fatores contribuíram para essa volatilidade, com destaque para a Guerra do Iraque e a instabilidade política na região. Em 2008, o mercado sofreu uma grande queda, com o preço do barril caindo quase 100 dólares, reflexo da recessão econômica global gerada pela crise financeira originada na bolha imobiliária dos EUA, que resultou na falência de bancos de renome mundial.

    A recuperação foi notável no final de 2008, com os preços voltando a subir, alcançando 110 dólares por barril em maio de 2011. Entre 2011 e 2014, o mercado experimentou um período de flutuações, com recorrentes altos e baixos, evidenciando o caráter cada vez mais volátil do mercado petrolífero no século XXI. No meio de 2014, uma nova queda nos preços foi observada, com a principal causa sendo a redução na demanda global e o aumento da produção nos Estados Unidos e no Canadá, que passaram a extrair grandes quantidades de petróleo de xisto.

    Após outro período de volatilidade entre 2016 e 2020, a pandemia da COVID-19 causou um impacto devastador tanto na produção quanto no consumo global de petróleo. O preço do barril chegou a cair para cerca de 17 dólares, um reflexo da drástica redução da atividade econômica mundial. Com a recuperação da demanda após o pico da pandemia, o mercado petrolífero se reergueu rapidamente, atingindo a marca de 120 dólares por barril. No entanto, a partir de 2022, o mercado entrou em uma nova fase de turbulência, impulsionada pela Guerra da Ucrânia e novos conflitos entre Israel e Palestina, que reconfiguraram as dinâmicas do comércio global de petróleo.
    '''

with tab1:
    '''
    ## Crises financeiras
    
    Nesta seção, serão analisadas as crises financeiras ao longo do tempo para investigar a possível correlação entre esses eventos e as variações no preço do barril de petróleo.

    Os dados sobre as crises financeiras foram obtidos a partir do site Investopedia (https://www.investopedia.com/articles/economics/08/past-recessions.asp).
    '''
    st.image(load_img('Gráficos/crise_financeira.png'))
    '''
    ### Análise
    A partir da análise do gráfico, observa-se que muitas das recessões econômicas mais significativas durante o período analisado coincidem com uma considerável variação no preço do barril de petróleo. Embora isso não implique que as recessões tenham causado diretamente as flutuações nos preços do petróleo, é possível perceber uma correlação entre esses dois fatores. As crises financeiras tendem a impactar a demanda global, o que, por sua vez, influencia os preços do petróleo. No entanto, outras variáveis, como a oferta e a geopolítica, também desempenham papéis cruciais na determinação desses preços.
    '''
with tab2:
    '''
    ## Conflitos Geopolíticos Relacionados ao Petróleo

    Esta seção visa analisar a relação entre grandes conflitos armados e a variação dos preços do barril de petróleo ao longo do período abrangido pelo dataset.

    O petróleo, sendo um recurso de grande valor estratégico e econômico, tem sido um fator de disputas geopolíticas ao longo da história. Conflitos envolvendo a sua extração, manipulação e comercialização podem impactar diretamente o comportamento da série temporal dos preços do barril de petróleo, influenciando a dinâmica global de oferta e demanda.

    Os dados sobre os conflitos geopolíticos foram obtidos da página da Wikipedia sobre as "Guerras do Petróleo" (https://en.wikipedia.org/wiki/Oil_war).
    '''
    st.image(load_img('Gráficos/guerras.png'))
    '''
    ### Análise
    Assim como observado na análise das crises financeiras, há uma forte correlação entre grandes guerras e a variação no preço do barril de petróleo. Durante os períodos de conflitos armados, especialmente aqueles envolvendo países do Oriente Médio, observamos flutuações significativas nos preços do petróleo. O petróleo, sendo a principal fonte de renda de muitos países produtores, exerce um papel crucial na economia global, além de ser uma fonte primária de energia e matéria-prima para a fabricação de produtos essenciais.

    Dado seu valor estratégico e a alta demanda global, é plausível afirmar que as variações nos preços do barril de petróleo estão, de fato, correlacionadas com conflitos armados. O controle sobre os recursos petrolíferos é frequentemente um ponto central em disputas geopolíticas, e as instabilidades políticas decorrentes de guerras podem gerar rupturas na oferta, afetando diretamente os preços do mercado.
    '''