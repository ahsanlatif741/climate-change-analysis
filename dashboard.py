import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_loader import ClimateDataLoader

# Page configuration
st.set_page_config(
    page_title="Climate Change Analysis Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem;
    }
    .plot-container {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

class ClimateDashboard:
    def __init__(self):
        self.loader = ClimateDataLoader()
        self.temp_data, self.co2_data, self.extreme_data = self.loader.get_all_data()
    
    def run(self):
        # Header
        st.markdown('<h1 class="main-header">🌍 Climate Change Trend Analysis Dashboard</h1>', 
                   unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
        <h3>Final Year Project - University Presentation</h3>
        <p>Comprehensive analysis of global climate change trends using historical data</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Key Metrics Row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total Warming (since 1880)",
                value=f"{self.temp_data['Temperature_Anomaly'].iloc[-1]:.2f}°C",
                delta=f"{self.temp_data['Temperature_Anomaly'].iloc[-1] - self.temp_data['Temperature_Anomaly'].iloc[0]:.2f}°C"
            )
        
        with col2:
            st.metric(
                label="Current CO2 Level",
                value=f"{self.co2_data['CO2_ppm'].iloc[-1]:.1f} ppm",
                delta=f"+{self.co2_data['CO2_ppm'].iloc[-1] - self.co2_data['CO2_ppm'].iloc[0]:.1f} ppm since 1958"
            )
        
        with col3:
            recent_warming = self.temp_data[self.temp_data['Year'] >= 2000]['Temperature_Anomaly']
            warming_since_2000 = recent_warming.iloc[-1] - recent_warming.iloc[0]
            st.metric(
                label="Warming since 2000",
                value=f"{warming_since_2000:.2f}°C",
                delta="Accelerated"
            )
        
        with col4:
            st.metric(
                label="Extreme Events Trend",
                value="+8% per decade",
                delta="Increasing"
            )
        
        # Tabs for different analyses
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📈 Temperature Analysis", 
            "🌫️ CO2 Analysis", 
            "🔗 Correlations",
            "🌪️ Extreme Events",
            "📊 Project Info"
        ])
        
        with tab1:
            self.show_temperature_analysis()
        
        with tab2:
            self.show_co2_analysis()
        
        with tab3:
            self.show_correlation_analysis()
        
        with tab4:
            self.show_extreme_events()
        
        with tab5:
            self.show_project_info()
    