import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Total electricity dashboard',
    page_icon=':globe_with_meridians:', 
    layout='centered'
)

@st.cache_data
def load_data():
    data = pd.read_csv('final_electricity.csv')
    return data

df = load_data()

with st.sidebar:
    st.title('Total Electricity of countries around the world :globe_with_meridians:')
    st.write('An interactive dashboard showing the Gross demand, Gross production and final consumption of electricity in kilowatt-hours, to the million!')

    country_list = list(df['Country'].unique())[::+1]

    selected_country = st.selectbox('Choose a country', country_list)
    df_selected_country = df.loc[df['Country'] == selected_country]
    df_selected_country_sorted = df_selected_country.sort_values(by='Country')


st.markdown(
    '''
    An interactive dashboard showing the Gross demand, Gross production and final consumption of electricity
    in kilowatt-hours, to the million!
    The data was sourced from the United Nations datamart. 
    Not all countries from the dataset will be included since some of them did not have accurate data, rather estimates.
    '''
    )

filtered_country_df = df.loc[df['Country'] == selected_country]

st.header(f'Dataframe for {selected_country}', divider='gray')
if st.checkbox(f'Show data for {selected_country}'):

    st.dataframe(filtered_country_df, width=1000)

st.header(f'Gross demand for {selected_country}', divider='gray')
fig_demand = px.line(filtered_country_df, x='Year', y='Gross demand')
st.plotly_chart(fig_demand)

st.header(f'Gross Production for {selected_country}', divider='gray')
fig_production = px.line(filtered_country_df, x='Year', y='Gross production')
st.plotly_chart(fig_production)

st.header(f'Final Consumption for {selected_country}', divider='gray')
fig_consumption = px.line(filtered_country_df, x='Year', y='Final consumption')
st.plotly_chart(fig_consumption)
