import streamlit as st
import pickle
import catboost as cat
import os
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(
    page_title="Ulysses Tcc App",    
    )

dir_path = os.path.dirname(os.path.realpath(__file__))

tab1, tab2, tab3 = st.tabs(["Avaliar Perfil", "Dashboard", "Pandas Report"])


with tab1:

    st.text("")
    st.text("")

    with st.expander("Dados Relacionados à IES"):
        aux0 = ("Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul")
        option0 = st.selectbox(
            "Região da IES:",
            range(len(aux0)),
            format_func=lambda x: aux0[x]    
        )

        aux10 = ('Estadual', 'Federal')
        option10 = st.selectbox(
            "Categoria administrativa da IES:",    
            range(len(aux10)),
            format_func=lambda x: aux10[x]   
        )

        aux11 = ('Concordo', 'Discordo', 'Discordo/concordo parcialmente', 'Não se aplica', 'Não sei responder')
        option11 = st.selectbox(
            "Infraestrutura geral da IES:",    
            range(len(aux11)),
            format_func=lambda x: aux11[x]    
        )

        aux12 = ('Concordo', 'Discordo', 'Discordo/concordo parcialmente', 'Não se aplica', 'Não sei responder')
        option12 = st.selectbox(
            "Biblioteca Virtual da IES:",    
            range(len(aux12)),
            format_func=lambda x: aux12[x]   
        )

        aux13 = ('Concordo', 'Discordo', 'Discordo/concordo parcialmente', 'Não se aplica', 'Não sei responder')
        option13 = st.selectbox(
            "Biblioteca física da IES:",    
            range(len(aux13)),
            format_func=lambda x: aux13[x]    
        )

        aux14 = ('Integral', 'Matutino', 'Noturno', 'Vespertino')
        option14 = st.selectbox(
            "Turno graduação:",    
            range(len(aux14)),
            format_func=lambda x: aux14[x]    
        )

        aux23 = ('De oito a doze', 'De quatro a sete', 'De uma a três', 'Mais de doze', 'Nenhuma, apenas assisto às aulas')
        option23 = st.selectbox(
            "Dedicação semanal:",
            range(len(aux23)),
            format_func=lambda x: aux23[x]   
        )

        aux24 = ('Bacharelado', 'Licenciatura')
        option24 = st.selectbox(
            "Grau acadêmico curso:",
            range(len(aux24)),
            format_func=lambda x: aux24[x]    
        )

        aux26 = ('Agricultura, silvicultura, pesca e veterinária', 'Artes e humanidades', 'Ciências naturais, matemática e estatí\xadstica', 'Ciências sociais, jornalismo e informação', 'Computação e Tecnologias da Informação e Comunicação (TIC)', 'Educação', 'Engenharia, produção e construção', 'Negócios, administração e direito', 'Saúde e bem-estar', 'Serviços')
        option26 = st.selectbox(
            "Grande área curso:",
            range(len(aux26)),
            format_func=lambda x: aux26[x]   
        )


    with st.expander("Dados do Aluno(a)"):
        
        aux1 = ("Feminino", "Masculino")
        option1 = st.selectbox(
            "Gênero do estudante:",    
            range(len(aux1)),
            format_func=lambda x: aux1[x]   
        )

        aux2 = ('Amarela', 'Branca', 'Indígena', 'Não quero declarar', 'Parda', 'Preta')
        option2 = st.selectbox(
            "Cor/raça:",    
            range(len(aux2)),
            format_func=lambda x: aux2[x]   
        )

        aux3 = ('Casado(a)', 'Outro', 'Separado(a) judicialmente/divorciado(a)', 'Solteiro(a)', 'Viúvo(a)')
        option3 = st.selectbox(
            "Estado civil:",    
            range(len(aux3)),
            format_func=lambda x: aux3[x]   
        )

        aux4 = ('Acima de 30 salários mínimos (mais de R$ 28.620,00)', 'Até 1,5 salário mínimo (até R$ 1.431,00)', 'De 1,5 a 3 salários mínimos (R$ 1.431,01 a R$ 2.862,00)', 'De 10 a 30 salários mínimos (R$ 9.540,01 a R$ 28.620,00)', 'De 3 a 4,5 salários mínimos (R$ 2.862,01 a R$ 4.293,00)', 'De 4,5 a 6 salários mínimos (R$ 4.293,01 a R$ 5.724,00)', 'De 6 a 10 salários mínimos (R$ 5.724,01 a R$ 9.540,00)')
        option4 = st.selectbox(
            "Renda familiar:",    
            range(len(aux4)),
            format_func=lambda x: aux4[x]    
        )

        aux5 = ('Ensino fundamental', 'Ensino médio', 'Ensino superior', 'Nenhuma')
        option5 = st.selectbox(
            "Escolaridade Pai:",    
            range(len(aux5)),
            format_func=lambda x: aux5[x]    
        )

        aux6 = ('Ensino fundamental', 'Ensino médio', 'Ensino superior', 'Nenhuma')
        option6 = st.selectbox(
            "Escolaridade Mãe:",    
            range(len(aux6)),
            format_func=lambda x: aux6[x]    
        )

        aux7 = ('Em alojamento universitário da própria instituição', 'Em casa ou apartamento, com cônjuge e/ou filhos', 'Em casa ou apartamento, com pais e/ou parentes', 'Em casa ou apartamento, sozinho', 'Em casa, apartamento ou em outros tipos de habitação coletiva, com outras pessoas')
        option7 = st.selectbox(
            "Companhia Residência:",    
            range(len(aux7)),
            format_func=lambda x: aux7[x]    
        )

        aux19 = ('Não', 'Sim')
        option19 = st.selectbox(
            "Graduação família:",    
            range(len(aux19)),
            format_func=lambda x: aux19[x]    
        )

        aux21 = ('Não', 'Sim')
        option21 = st.selectbox(
            "Situação trabalho:",    
            range(len(aux21)),
            format_func=lambda x: aux21[x]    
        )

        aux22 = ('Não tenho renda e meus gastos são financiados pela família, por outras pessoas e/ou por programas governamentais', 'Tenho renda e contribuo para o sustento da família', 'Tenho renda e não preciso de ajuda para financiar meus gastos', 'Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos')
        option22 = st.selectbox(
            "Situação financeira:",    
            range(len(aux22)),
            format_func=lambda x: aux22[x]    
        )

        aux28 = ('60 anos ou mais', 'Entre 18 e 24 anos', 'Entre 25 e 39 anos', 'Entre 40 e 59 anos')
        option28 = st.selectbox(
            "Faixa etária:",
            range(len(aux28)),
            format_func=lambda x: aux28[x]
        )

    with st.expander("Histórico Escolar"):

        aux8 = ('Todo ou a maior parte em escola privada', 'Todo ou a maior parte em escola pública', 'Todo ou parte no exterior')
        option8 = st.selectbox(
            "Tipo escola ensino médio:",    
            range(len(aux8)),
            format_func=lambda x: aux8[x]    
        )

        aux9 = ('Educação de Jovens e Adultos (EJA) e/ou Supletivo', 'Ensino médio tradicional', 'Outra modalidade', 'Profissionalizante magistério (Curso Normal)', 'Profissionalizante técnico (eletrônica, contabilidade, agrícola, outro)')
        option9 = st.selectbox(
            "Modalidade ensino médio:",    
            range(len(aux9)),
            format_func=lambda x: aux9[x]    
        )

        aux25 = ('Centro-Oeste', 'Nordeste', 'Norte', 'Não se aplica', 'Sudeste', 'Sul')
        option25 = st.selectbox(
            "Região escola ensino médio:",
            range(len(aux25)),
            format_func=lambda x: aux25[x]    
        )

        aux27 = ('10 anos ou mais', '2 anos ou menos', 'Entre 3 e 5 anos', 'Entre 6 e 9 anos')
        option27 = st.selectbox(
            "Diferença entre inicio da graduação e fim do ensino médio:",
            range(len(aux27)),
            format_func=lambda x: aux27[x]    
        )

    with st.expander("Ações Afirmativas"):

        aux15 = ('Não', 'Sim')
        option15 = st.selectbox(
            "Ação afirmativa:",    
            range(len(aux15)),
            format_func=lambda x: aux15[x]    
        )

        aux16 = ('Não', 'Sim')
        option16 = st.selectbox(
            "Bolsa acadêmica:",    
            range(len(aux16)),
            format_func=lambda x: aux16[x]   
        )

        aux17 = ('Não', 'Sim')
        option17 = st.selectbox(
            "Auxílio permanência:",    
            range(len(aux17)),
            format_func=lambda x: aux17[x]   
        )

        aux18 = ('Não', 'Sim')
        option18 = st.selectbox(
            "Incentivo graduação:",    
            range(len(aux18)),
            format_func=lambda x: aux18[x]    
        )

        aux20 = ('Não', 'Sim')
        option20 = st.selectbox(
            "Oferta apoio geral:",    
            range(len(aux20)),
            format_func=lambda x: aux20[x]    
        )

    st.text("")
    st.text("")

    if st.button('Avaliar'):
        predList = []
        for i in range(29):        
            auxList = [0] * len(globals()['aux' + str(i)])
            position = globals()['option' + str(i)]
            auxList[position] = 1
            predList.extend(auxList)
        model = pickle.load(open( dir_path + "/data-15.sav", "rb"))
        y = model.predict(predList)
        x = st.write('O perfil avaliado pertence ao grupo: ' + ('Entre 2 e 4 anos'
                     if(y == 'TEMPO_GRADUACAO: Entre 2 e 4 anos')
                         
                     else
                         '5 anos ou mais'
                    ))

with tab2:

    st.text("")
    st.text("")

    with st.expander("Análise de variáveis"):
        image1 = dir_path + "/importance.png"
        st.image(image1, caption="Feature importance considerando as vinte primeiras variáveis.")
        image2 = dir_path + "/correlacao.png"
        st.image(image2, caption="Matriz de correlação.")
    

    df =  pd.read_parquet( dir_path + "/df.parquet.gzip", engine='auto')

    regioes = ["Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"]
    faixa_etaria = ['Entre 18 e 24 anos', 'Entre 25 e 39 anos', 'Entre 40 e 59 anos', '60 anos ou mais']
    tempo_grad = ['Entre 2 e 4 anos', '5 anos ou mais']

    
    with st.expander("Filtros"):
        sort_values = st.multiselect('Regiões', options= regioes, default= regioes)
        sort_values2 = st.multiselect('Faixa Etária', options= faixa_etaria, default= faixa_etaria[0])
        sort_values3 = st.multiselect('Tempo de Graduação', options= tempo_grad, default= tempo_grad[0])


    df = df.query("REGIAO_IES in (@sort_values) & FAIXA_ETARIA in (@sort_values2) & TEMPO_GRADUACAO_1 in (@sort_values3)")

    st.header('Alunos por Faixa Etária')
    faixa_etaria = df['FAIXA_ETARIA'].replace(regex=['FAIXA_ETARIA: '],value= '').value_counts()
    #st.bar_chart(faixa_etaria)
    import plotly.express as px     
    fig=px.bar(faixa_etaria, y = 'count', x = faixa_etaria.index, labels={'FAIXA_ETARIA':'QTD de Alunos', 'index': 'Faixa etária'}, orientation='v')
    st.write(fig)

    st.header('Alunos por Região')
    faixa_etariaR = df.groupby(["FAIXA_ETARIA","REGIAO_IES"], as_index=False)["SEXO"].count().replace(regex=['FAIXA_ETARIA: ', 'REGIAO_IES: '],value= '')
    #st.bar_chart(faixa_etaria)
    import plotly.express as px     
    fig=px.bar(faixa_etariaR, x = 'SEXO', y = 'FAIXA_ETARIA', color='REGIAO_IES', color_discrete_sequence = ['#3366cc']*3, text="REGIAO_IES",labels={'SEXO':'QTD de Alunos', 'FAIXA_ETARIA': 'Faixa etária', 'REGIAO_IES': 'REGIÃO IES'}, barmode = 'group')
    fig.update_traces(textfont_size=24, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(showlegend=False)
    fig = fig.update_layout(
    xaxis_range=[0, 0.5e5])
    st.write(fig)

    st.header('Tempo de Graduação x Faixa Etária')
    faixa_etariaR = df.groupby(["FAIXA_ETARIA","TEMPO_GRADUACAO_1"], as_index=False)["SEXO"].count().replace(regex=['FAIXA_ETARIA: ', 'TEMPO_GRADUACAO: '],value= '')
    #st.bar_chart(faixa_etaria)
    import plotly.express as px     
    fig=px.bar(faixa_etariaR, x = 'SEXO', y = 'FAIXA_ETARIA', color='TEMPO_GRADUACAO_1', labels={'SEXO':'QTD Alunos', 'FAIXA_ETARIA': 'Faixa etária', "TEMPO_GRADUACAO_1": 'TEMPO GRADUAÇÃO'}, barmode = 'group')
    st.write(fig)


with tab3:

    import streamlit.components.v1 as components

    st.text("")
    st.text("")

    report_file = open(dir_path + '/report_tcc.html', 'r', encoding='utf-8')
    source_code = report_file.read() 
    components.html(source_code, height=600, scrolling=True)

    


