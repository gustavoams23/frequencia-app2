import streamlit as st

# Título personalizado
st.title("Cálculo de porcentagem de frequência do Prof. Gustavo Abreu (EJA)")

# Dicionário com total de aulas por disciplina
total_aulas = {
    "Português": 120,
    "Matemática": 120,
    "História": 60,
    "Geografia": 60,
    "Ciências": 60,
    "Artes": 40,
    "Inglês": 40,
    "Ed. Física": 40
}

# Escolha da disciplina
disciplina = st.selectbox("Selecione a disciplina:", list(total_aulas.keys()))

# Entrada do número de faltas
faltas = st.number_input("Digite o número de faltas do aluno:", min_value=0)

# Calcular frequência
if st.button("Calcular frequência"):
    aulas = total_aulas[disciplina]
    presencas = aulas - faltas
    frequencia = (presencas / aulas) * 100
    frequencia_arredondada = round(frequencia)  # Arredonda para inteiro
    st.success(f"Frequência em {disciplina}: {frequencia_arredondada}%")