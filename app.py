"""
ASISTENTE TÉCNICO SATGARDEN V-DIAGNOSTICO-FINAL
Esta es una versión de diagnóstico para forzar la actualización en Streamlit Cloud.
"""

import os
import streamlit as st
import pandas as pd
from openai import OpenAI
from supabase import create_client, Client
import PyPDF2
from datetime import datetime
from dotenv import load_dotenv
import re
import json
from io import BytesIO

# --- Dependencias Opcionales para PDF ---
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

# --- Configuración Inicial ---
load_dotenv()
st.set_page_config(page_title="Asistente Satgarden V-DIAGNOSTICO-FINAL", page_icon="🚨", layout="wide")

st.success("✅ ¡Si ves este mensaje, la actualización a la versión de diagnóstico ha funcionado correctamente!")

# --- Estilos CSS Personalizados ---
def load_css():
    st.markdown("""
    <style>
        /* Base and Background */
        .stApp {
            background-color: #0c111e; /* Dark blue-grey background */
        }

        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            color: #e0e0e0; /* Off-white for titles */
        }
        .stMarkdown, .stTextInput, .stTextArea, .stSelectbox {
            color: #c0c0c0; /* Lighter grey for body text */
        }

        /* --- Hub Page Specific Styles --- */
        .stButton > button {
            all: unset; /* Reset Streamlit's default button styles */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            width: 100%;
            height: 140px; /* Reduced height */
            padding: 15px;
            font-size: 0.9em;  /* Final text size */
            font-weight: 400; /* Normal weight */
            color: #e0e0e0;
            background-color: #1c2a4a;
            border-radius: 12px;
            border: 1px solid #3a4a6a;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            white-space: pre-wrap; /* Ensures the newline character is respected */
        }
        .stButton > button:hover {
            background-color: #2a3a5a;
            border-color: #537895;
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }
        .stButton > button:active {
            transform: translateY(0px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        /* Style the first line (emoji icon) of the button text */
        .stButton > button p:first-of-type {
            font-size: 3.0em; /* Larger icon size */
            margin-bottom: 10px; /* Adjusted spacing */
            line-height: 1;
        }

        /* --- Kanban Board (CMMS) Styles --- */
        [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] > [data-testid="stVerticalBlock"] {
            background-color: rgba(42, 58, 90, 0.3);
            border-radius: 10px;
            padding: 15px;
        }

        .kanban-header h3 {
            text-align: center;
            background-color: rgba(0, 0, 0, 0.2);
            padding: 8px;
            border-radius: 8px;
            margin-bottom: 15px;
            font-size: 1.3em;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #537895; /* Accent color for headers */
        }

        /* Kanban Card Style */
        .st-emotion-cache-12w0qpk {
            background-color: #1c2a4a;
            border: 1px solid #3a4a6a;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            transition: background-color 0.2s;
        }
        .st-emotion-cache-12w0qpk:hover {
             background-color: #2a3a5a;
        }

        /* --- Sidebar Styles --- */
        .st-emotion-cache-16txtl3 {
            background-color: rgba(12, 17, 30, 0.8);
            backdrop-filter: blur(5px);
        }
    </style>
    """, unsafe_allow_html=True)

# --- Conexiones (Cacheado para Rendimiento) ---
@st.cache_resource
def init_connections():
    if not all([os.getenv("OPENAI_API_KEY"), os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")]):
        st.error("Faltan variables de entorno. Revisa tu archivo .env o los secrets en Streamlit Cloud.")
        st.stop()
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    supabase_client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    return openai_client, supabase_client

openai_client, supabase = init_connections()
EMBEDDING_MODEL = "text-embedding-3-small"


# --- Funciones de Ingesta y Procesamiento de Documentos (Placeholder para diagnóstico) ---
def ingest_pdf_files(files):
    st.info("Función de ingesta en modo diagnóstico.")

# --- Funciones de IA y Lógica de Negocio (Placeholder para diagnóstico) ---
def generate_embedding(text): return None
def generate_technical_response(query, context_docs, tipo): return "Respuesta de diagnóstico."
def generate_maintenance_plan(modelo, horas): return "Plan de mantenimiento de diagnóstico."
def generate_budget_estimate(trabajo, modelo, desc): return {}

# --- Funciones de Base de Datos (Placeholder para diagnóstico) ---
@st.cache_data(ttl=600)
def get_dashboard_data(): return pd.DataFrame()
@st.cache_data(ttl=300)
def get_work_orders(): return []
def create_work_order(title, description, machine_model, work_type, assigned_to, priority, related_consultation_id=None): pass
def update_work_order_status(order_id, new_status): pass
def update_work_order_with_report(order_id, report_text): pass
def search_verified_knowledge(query_text, top_k=1, threshold=0.8): return None
def search_document_knowledge(query_text, top_k=5): return []
def get_document_list(): return pd.DataFrame(columns=['source', 'chunks'])
def delete_document_by_source(source_name): pass
def log_and_get_id(tecnico, modelo, tipo, desc, diag): return None
def update_feedback(log_id, feedback_value): pass
def save_verified_knowledge(query, response, verifier): pass

# --- Funciones de UI y Pestañas (Simplificadas para diagnóstico) ---
def generate_pdf_report(title, data_dict, content_text): return None
def generate_work_order_pdf(case_data): return None
def consult_tab(): st.header("Pestaña de Consulta (Diagnóstico)")
def maintenance_tab(): st.header("Pestaña de Mantenimiento (Diagnóstico)")
def calculator_tab(): st.header("Pestaña de Calculadora (Diagnóstico)")
def dashboard_tab(): st.header("Pestaña de Dashboard (Diagnóstico)")
def history_tab(): st.header("Pestaña de Historial (Diagnóstico)")
def knowledge_management_tab(): st.header("Pestaña de Conocimiento (Diagnóstico)")
def cmms_tab(): st.header("Pestaña de CMMS (Diagnóstico)")


# --- Navegación Principal y Renderizado de Páginas ---

def render_hub_page():
    st.title("🛠️ Asistente Técnico Satgarden V-DIAGNOSTICO-FINAL")
    st.markdown("Esta es la página principal de la versión de diagnóstico.")
    st.divider()

    # --- ROW 1 ---
    row1_cols = st.columns(3)
    with row1_cols[0]:
        if st.button("💬\nConsulta Técnica", use_container_width=True, key="hub_consulta"):
            st.session_state.page = "Consulta"
            st.rerun()
    with row1_cols[1]:
        if st.button("📋\nGestión de Casos", use_container_width=True, key="hub_cmms"):
            st.session_state.page = "CMMS"
            st.rerun()
    with row1_cols[2]:
        if st.button("🧮\nCalculadora", use_container_width=True, key="hub_calculadora"):
            st.session_state.page = "Calculadora"
            st.rerun()

def render_full_app():
    if st.button("⬅️ Volver al Menú Principal"):
        st.session_state.page = "Hub"
        st.rerun()

    page_map = {
        "Consulta": consult_tab, "CMMS": cmms_tab, "Mantenimiento": maintenance_tab,
        "Calculadora": calculator_tab, "Dashboard": dashboard_tab, "Historial": history_tab,
        "Conocimiento": knowledge_management_tab,
    }
    
    page_function = page_map.get(st.session_state.page)
    if page_function:
        page_function()
    else:
        st.session_state.page = "Hub"
        st.rerun()

def main():
    load_css()
    if 'page' not in st.session_state:
        st.session_state.page = "Hub"
    if st.session_state.page == "Hub":
        render_hub_page()
    else:
        render_full_app()

if __name__ == "__main__":
    main()
