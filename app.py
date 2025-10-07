"""
ASISTENTE TÉCNICO SATGARDEN V-LISTA-FINAL
Implementación final con layout de lista para forzar la actualización.
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
st.set_page_config(page_title="Asistente Satgarden V-LISTA-FINAL", page_icon="🛠️", layout="wide")

# --- Estilos CSS Personalizados ---
def load_css():
    st.markdown("""
    <style>
        /* Base and Background */
        .stApp {
            background-color: #0c111e;
        }

        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            color: #e0e0e0;
        }
        .stMarkdown, .stTextInput, .stTextArea, .stSelectbox {
            color: #c0c0c0;
        }

        /* --- Hub Page (List Layout) Styles --- */
        .stButton > button {
            all: unset;
            display: flex;
            align-items: center;
            width: 100%;
            padding: 15px 25px;
            margin-bottom: 10px;
            font-size: 1.2em;
            font-weight: 500;
            color: #e0e0e0;
            background-color: #1c2a4a;
            border-radius: 10px;
            border: 1px solid #3a4a6a;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #2a3a5a;
            border-color: #537895;
        }
        .stButton > button::before {
            content: attr(data-icon);
            font-size: 2em;
            margin-right: 20px;
        }

        /* --- Sidebar Styles --- */
        .st-emotion-cache-16txtl3 {
            background-color: rgba(12, 17, 30, 0.8);
            backdrop-filter: blur(5px);
        }
    </style>
    """, unsafe_allow_html=True)

# --- Conexiones ---
@st.cache_resource
def init_connections():
    if not all([os.getenv("OPENAI_API_KEY"), os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")]):
        st.error("Faltan variables de entorno.")
        st.stop()
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    supabase_client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    return openai_client, supabase_client

openai_client, supabase = init_connections()
EMBEDDING_MODEL = "text-embedding-3-small"

# --- Placeholder para las funciones completas ---
def placeholder_tab(title):
    st.header(title)
    st.info("Esta funcionalidad está activa en la versión completa del código.")

# --- Navegación Principal y Renderizado de Páginas ---
def render_hub_page():
    st.title("🛠️ Asistente Técnico Satgarden V-LISTA-FINAL")
    st.markdown("Bienvenido al centro de operaciones técnicas. Selecciona una herramienta para empezar:")
    st.divider()

    # Usamos markdown para crear el botón y poder pasar el data-icon
    if st.button("Consulta Técnica", key="hub_consulta", use_container_width=True):
        st.session_state.page = "Consulta"
        st.rerun()
    if st.button("Gestión de Casos", key="hub_cmms", use_container_width=True):
        st.session_state.page = "CMMS"
        st.rerun()
    if st.button("Calculadora", key="hub_calculadora", use_container_width=True):
        st.session_state.page = "Calculadora"
        st.rerun()
    if st.button("Dashboard", key="hub_dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()
    if st.button("Mantenimiento Preventivo", key="hub_mantenimiento", use_container_width=True):
        st.session_state.page = "Mantenimiento"
        st.rerun()
    if st.button("Base de Conocimiento", key="hub_conocimiento", use_container_width=True):
        st.session_state.page = "Conocimiento"
        st.rerun()
    if st.button("Ver Historial y Verificar", key="hub_historial", use_container_width=True):
        st.session_state.page = "Historial"
        st.rerun()
    
    # Este script de JS añade los iconos a los botones
    st.markdown("""
    <script>
        const buttons = window.parent.document.querySelectorAll('.stButton > button');
        const icons = {
            'Consulta Técnica': '💬',
            'Gestión de Casos': '📋',
            'Calculadora': '🧮',
            'Dashboard': '📊',
            'Mantenimiento Preventivo': '⚙️',
            'Base de Conocimiento': '📚',
            'Ver Historial y Verificar': '📜'
        };
        buttons.forEach(button => {
            const label = button.textContent;
            if (icons[label]) {
                button.setAttribute('data-icon', icons[label]);
            }
        });
    </script>
    """, unsafe_allow_html=True)


def render_full_app():
    if st.button("⬅️ Volver al Menú Principal"):
        st.session_state.page = "Hub"
        st.rerun()

    page_map = {
        "Consulta": lambda: placeholder_tab("Consulta Técnica"),
        "CMMS": lambda: placeholder_tab("Gestión de Casos (CMMS)"),
        "Mantenimiento": lambda: placeholder_tab("Mantenimiento Preventivo"),
        "Calculadora": lambda: placeholder_tab("Calculadora de Estimaciones"),
        "Dashboard": lambda: placeholder_tab("Dashboard"),
        "Historial": lambda: placeholder_tab("Historial y Verificación"),
        "Conocimiento": lambda: placeholder_tab("Base de Conocimiento"),
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
