import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dataset.csv')

def header():
    """
    Shows the header section of the Streamlit application, 
    including a description of the dataset and author information.
    """
    st.markdown("# Saúde do Sono e Estilo de Vida")
    st.markdown("O *dataset* [Sleep Health and Lifestyle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) contém informações relacionadas a hábitos de vida, saúde do sono e características demográficas, como idade, gênero, índice de massa corporal (IMC), qualidade do sono e atividades diárias. Ele é projetado para ajudar na análise e identificação de padrões relacionados ao impacto do estilo de vida e saúde geral sobre o sono, sendo útil para estudos em áreas como saúde pública, bem-estar e ciência comportamental. O conjunto de dados é composto por registros organizados, permitindo cruzamentos entre variáveis e insights valiosos sobre a relação entre sono, peso e fatores demográficos.")
    st.markdown("""
    - José Wilson Martins Filho
    - Augusto César Honorato do Santos
    - David Fontes Silva
    - Victor Gabriel Vieira Santos
    """)

def sleep_disorder_chart():
    """
    Creates a scatter plot displaying the correlation between sleep disorders, 
    sleep duration, and occupation.
    """
    st.header("Correlação: Distúrbios do Sono, Duração do Sono e Ocupação")
    if 'SleepDisorder' in data.columns:
        data['Sleep Disorder Numeric'] = data['SleepDisorder'].astype('category').cat.codes
    else:
        st.error("Column 'Sleep Disorder' not found in the dataset!")

    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        x=data['Occupation'], 
        y=data['SleepDuration'], 
        hue=data['SleepDisorder'], 
        palette='Set2',
        alpha=0.7
    )
    plt.title("Duração do Sono por Ocupação e Distúrbios do Sono")
    plt.xlabel("Ocupação")
    plt.ylabel("Duração do Sono (horas)")
    plt.legend(title="Distúrbios do Sono")
    plt.xticks(rotation=45, ha='right') 
    st.pyplot(plt)

def physical_activity_chart():
    """
    Creates a scatter plot displaying the relationship between gender, 
    age, and physical activity levels.
    """
    st.header("Relação: Gênero, Idade e Atividade Física")
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        x=data['Age'], 
        y=data['PhysicalActivity'], 
        hue=data['Gender'], 
        palette='coolwarm',
        alpha=0.7
    )
    plt.title("Atividade Física por Idade e Gênero")
    plt.xlabel("Idade")
    plt.ylabel("Nível de Atividade Física")
    plt.legend(title="Gênero")
    st.pyplot(plt)

def age_imc_gender_chart():
    """
    Creates a scatter plot analyzing the relationship between age, 
    BMI (Body Mass Index), and gender. Allows users to filter data by 
    age range and gender using Streamlit widgets.
    """
    st.title("Análise da Relação entre Idade, IMC e Gênero")
    min_age, max_age = int(data['Age'].min()), int(data['Age'].max())
    selected_age_range = st.slider(
        "Selecione a faixa etária:",
        min_value=min_age,
        max_value=max_age,
        value=(min_age, max_age)
    )
    available_genders = data['Gender'].unique()
    selected_gender = st.selectbox(
        "Selecione o gênero:",
        options=available_genders,
        index=0
    )

    filtered_data = data[
        (data['Age'] >= selected_age_range[0]) &
        (data['Age'] <= selected_age_range[1]) &
        (data['Gender'] == selected_gender)
    ]

    if filtered_data.empty:
        st.warning("No data available for the selected age range and gender combination.")
    else:
        fig, ax = plt.subplots()
        ax.scatter(filtered_data['Age'], filtered_data['BMI'], alpha=0.6, edgecolors="w", s=100)
        ax.set_title(f"Relação entre Idade e IMC ({selected_gender})", fontsize=16)
        ax.set_xlabel("Idade", fontsize=12)
        ax.set_ylabel("IMC", fontsize=12)
        ax.grid(True)

        st.pyplot(fig)

    if st.checkbox("Mostrar dados filtrados"):
        st.dataframe(filtered_data)

def general_data():
    """
    Shows the dataset in a tabular format using Streamlit.
    """
    st.markdown('## Dados')
    st.write(data)

if __name__ == '__main__':
    header()
    sleep_disorder_chart()
    physical_activity_chart()
    age_imc_gender_chart()
    general_data()
