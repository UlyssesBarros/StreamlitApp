import streamlit as st
import pickle
import catboost as cat


option0 = st.selectbox(
    "Selecione a região da IES:",
    ("Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"),
    label_visibility="visible"    
)

option1 = st.selectbox(
    "Gênero do estudante:",
    ("Feminino", "Masculino"),
    label_visibility="visible"    
)

option2 = st.selectbox(
    "Cor/raça:",
    ('Amarela', 'Branca', 'Indígena', 'Não quero declarar', 'Parda', 'Preta'),
    label_visibility="visible"    
)

option3 = st.selectbox(
    "Estado civil:",
    ('Casado(a)', 'Outro', 'Separado(a) judicialmente/divorciado(a)', 'Solteiro(a)', 'Viúvo(a)'),
    label_visibility="visible"    
)

option4 = st.selectbox(
    "Renda familiar:",
    ('Acima de 30 salários mínimos (mais de R$ 28.620,00)', 'Até 1,5 salário mínimo (até R$ 1.431,00)', 'De 1,5 a 3 salários mínimos (R$ 1.431,01 a R$ 2.862,00)', 'De 10 a 30 salários mínimos (R$ 9.540,01 a R$ 28.620,00)', 'De 3 a 4,5 salários mínimos (R$ 2.862,01 a R$ 4.293,00)', 'De 4,5 a 6 salários mínimos (R$ 4.293,01 a R$ 5.724,00)', 'De 6 a 10 salários mínimos (R$ 5.724,01 a R$ 9.540,00)'),
    label_visibility="visible"    
)

option5 = st.selectbox(
    "Escolaridade Pai:",
    ('Ensino fundamental', 'Ensino médio', 'Ensino superior', 'Nenhuma'),
    label_visibility="visible"    
)

option6 = st.selectbox(
    "Escolaridade Mãe:",
    ('Ensino fundamental', 'Ensino médio', 'Ensino superior', 'Nenhuma'),
    label_visibility="visible"    
)

option7 = st.selectbox(
    "Companhia Residência:",
    ('Em alojamento universitário da própria instituição', 'Em casa ou apartamento, com cônjuge e/ou filhos', 'Em casa ou apartamento, com pais e/ou parentes', 'Em casa ou apartamento, sozinho', 'Em casa, apartamento ou em outros tipos de habitação coletiva, com outras pessoas'),
    label_visibility="visible"    
)

option8 = st.selectbox(
    "Tipo escola ensino médio:",
    ('Todo ou a maior parte em escola privada', 'Todo ou a maior parte em escola pública', 'Todo ou parte no exterior'),
    label_visibility="visible"    
)

option9 = st.selectbox(
    "Modalidade ensino médio:",
    ('Educação de Jovens e Adultos (EJA) e/ou Supletivo', 'Ensino médio tradicional', 'Outra modalidade', 'Profissionalizante magistério (Curso Normal)', 'Profissionalizante técnico (eletrônica, contabilidade, agrícola, outro)'),
    label_visibility="visible"    
)

option10 = st.selectbox(
    "Categoria administrativa da IES:",
    ('Estadual', 'Federal'),
    label_visibility="visible"    
)

option11 = st.selectbox(
    "Infraestrutura geral da IES:",
    ('Concordo', 'Discordo', 'Discordo/concordo parcialmente', 'Não se aplica', 'Não sei responder'),
    label_visibility="visible"    
)

option12 = st.selectbox(
    "Biblioteca Virtual da IES:",
    ('Concordo', 'Discordo', 'Discordo/concordo parcialmente', 'Não se aplica', 'Não sei responder'),
    label_visibility="visible"    
)

option13 = st.selectbox(
    "Biblioteca física da IES:",
    ('Concordo', 'Discordo', 'Discordo/concordo parcialmente', 'Não se aplica', 'Não sei responder'),
    label_visibility="visible"    
)

option14 = st.selectbox(
    "Turno graduação:",
    ('Integral', 'Matutino', 'Noturno', 'Vespertino'),
    label_visibility="visible"    
)

option15 = st.selectbox(
    "Ação afirmativa:",
    ('Não', 'Sim'),
    label_visibility="visible"    
)

option16 = st.selectbox(
    "Bolsa acadêmica:",
    ('Não', 'Sim'),
    label_visibility="visible"    
)

option17 = st.selectbox(
    "Auxílio permanência:",
    ('Não', 'Sim'),
    label_visibility="visible"    
)

option18 = st.selectbox(
    "Incentivo graduação:",
    ('Não', 'Sim'),
    label_visibility="visible"    
)

option19 = st.selectbox(
    "Graduação família:",
    ('Não', 'Sim'),
    label_visibility="visible"    
)

option20 = st.selectbox(
    "Oferta apoio geral:",
    ('Não', 'Sim'),
    label_visibility="visible"    
)

option21 = st.selectbox(
    "Situação trabalho:",
    ('Não', 'Sim'),
    label_visibility="visible"    
)

option22 = st.selectbox(
    "Situação financeira:",
    ('Não tenho renda e meus gastos são financiados pela família, por outras pessoas e/ou por programas governamentais', 'Tenho renda e contribuo para o sustento da família', 'Tenho renda e não preciso de ajuda para financiar meus gastos', 'Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos'),
    label_visibility="visible"    
)

option23 = st.selectbox(
    "Dedicação semanal:",
    ('De oito a doze', 'De quatro a sete', 'De uma a três', 'Mais de doze', 'Nenhuma, apenas assisto às aulas'),
    label_visibility="visible"    
)

option24 = st.selectbox(
    "Grau acadêmico curso:",
    ('Bacharelado', 'Licenciatura'),
    label_visibility="visible"    
)

option25 = st.selectbox(
    "Região escola ensino médio:",
    ('Centro-Oeste', 'Nordeste', 'Norte', 'Não se aplica', 'Sudeste', 'Sul'),
    label_visibility="visible"    
)

option26 = st.selectbox(
    "Grande área curso:",
    ('Agricultura, silvicultura, pesca e veterinária', 'Artes e humanidades', 'Ciências naturais, matemática e estatí\xadstica', 'Ciências sociais, jornalismo e informação', 'Computação e Tecnologias da Informação e Comunicação (TIC)', 'Educação', 'Engenharia, produção e construção', 'Negócios, administração e direito', 'Saúde e bem-estar', 'Serviços'),
    label_visibility="visible"    
)

option27 = st.selectbox(
    "Diferença inicio graduação fim ensino médio:",
    ('10 anos ou mais', '2 anos ou menos', 'Entre 3 e 5 anos', 'Entre 6 e 9 anos'),
    label_visibility="visible"    
)

option28 = st.selectbox(
    "Faixa etária:",
    ('60 anos ou mais', 'Entre 18 e 24 anos', 'Entre 25 e 39 anos', 'Entre 40 e 59 anos'),
    label_visibility="visible"    
)

if st.button('Avaliar perfil'):
    model = pickle.load(open('data.sav', 'rb'))
    y = model.predict([0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 1.0,
 0.0,
 1.0,
 0.0,
 0.0,
 1.0,
 0.0,
 1.0,
 0.0,
 1.0,
 1.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0])
    x = st.write('O perfil avaliado pertence ao grupo: ' + y)


