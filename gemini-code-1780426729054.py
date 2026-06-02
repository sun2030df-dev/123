import streamlit as st

# --- Page Setup & Configurations ---
st.set_page_config(
    page_title="Poste de Buse", 
    page_icon="📐", 
    layout="centered"
)

# Custom injection for mobile responsiveness, background, typography, and button sizing
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Impact&family=Arial&display=swap');
    
    /* Viewport adjustment for mobile scaling */
    @viewport {
        width: device-width;
        zoom: 1.0;
    }

    /* Force main app background to white */
    .stApp {
        background-color: #FFFFFF !important;
        padding: 10px !important;
    }
    
    /* Title Banner optimized for smaller mobile screens */
    .header-banner {
        background-color: #000000;
        border-radius: 15px;
        padding: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    .header-text {
        font-family: 'Impact', sans-serif;
        font-style: italic;
        font-size: 26px;
        color: #FFFFFF;
        letter-spacing: 1px;
    }
    
    /* Form Label Settings optimized for phone reading */
    .form-label {
        font-family: 'Impact', sans-serif;
        font-style: italic;
        font-size: 18px;
        color: #000000;
        margin-top: 12px;
        margin-bottom: 2px;
    }
    
    /* Result Rows optimized for alignment on narrow layouts */
    .result-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 15px 0;
        border-bottom: 1px solid #EEEEEE;
        padding-bottom: 10px;
    }
    .result-title {
        font-family: 'Impact', sans-serif;
        font-style: italic;
        font-size: 32px;
        color: #000000;
    }
    .result-value {
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: #0066CC;
    }
    .result-error {
        font-family: 'Arial', sans-serif;
        font-size: 20px;
        color: #FF3333;
    }
    
    /* Text Inputs optimized for easy touch targeting on mobile */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #F5F5F5 !important;
        color: #000000 !important;
        border: 1px solid #CCCCCC !important;
        font-size: 18px !important; /* Prevents auto-zoom on mobile focus */
        height: 45px !important; /* Larger hit-box for fingers */
    }

    /* Make textareas slightly more compact on phone screens */
    .stTextArea>div>div>textarea {
        height: 100px !important;
    }

    /* Button adjustments for easier thumb-tapping */
    div.stButton > button {
        height: 50px !important;
        font-size: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Persistent Session States ---
if "notes_log" not in st.session_state:
    st.session_state.notes_log = ""
if "z1_display" not in st.session_state:
    st.session_state.z1_display = "—"
if "delta_display" not in st.session_state:
    st.session_state.delta_display = "—"
if "z1_is_error" not in st.session_state:
    st.session_state.z1_is_error = False
if "delta_is_error" not in st.session_state:
    st.session_state.delta_is_error = False

# Ensure mobile entry layout states exist cleanly
if "ref_in" not in st.session_state:
    st.session_state.ref_in = ""
if "arr_in" not in st.session_state:
    st.session_state.arr_in = ""
if "av_in" not in st.session_state:
    st.session_state.av_in = ""
if "proj_in" not in st.session_state:
    st.session_state.proj_in = ""

# --- Callback Function to Cleanly Clear Everything EXCEPT Logs ---
def clear_all_callback():
    # Reset output strings back to baseline values
    st.session_state.z1_display = "—"
    st.session_state.delta_display = "—"
    st.session_state.z1_is_error = False
    st.session_state.delta_is_error = False
    
    # Safe-clear inputs by editing session keys directly 
    st.session_state.ref_in = ""
    st.session_state.arr_in = ""
    st.session_state.av_in = ""
    st.session_state.proj_in = ""
    
    # Notice: st.session_state.notes_log is left out intentionally so it never gets deleted!

# --- Top Header Banner ---
st.markdown('<div class="header-banner"><span class="header-text">POSTE DE BUSE </span></div>', unsafe_allow_html=True)

# --- Form Inputs (Stacked Vertically for Android Screen Width) ---
st.markdown('<p class="form-label">COTE DE REFERENCE :</p>', unsafe_allow_html=True)
cote_ref_input = st.text_input("Ref", label_visibility="collapsed", key="ref_in")

st.markdown('<p class="form-label">LECTURE ARRIERE :</p>', unsafe_allow_html=True)
lec_arr_input = st.text_input("Arriere", label_visibility="collapsed", key="arr_in")

st.markdown('<p class="form-label">LECTURE AVANT :</p>', unsafe_allow_html=True)
lec_av_input = st.text_input("Avant", label_visibility="collapsed", key="av_in")

# --- Z / 1 Output Row ---
st.markdown('<div class="result-row">', unsafe_allow_html=True)
r_col1, r_col2 = st.columns([1, 1])
with r_col1:
    st.markdown('<span class="result-title">Z / 1 :</span>', unsafe_allow_html=True)
with r_col2:
    if st.session_state.z1_is_error:
        st.markdown(f'<div style="text-align: right;"><span class="result-error">{st.session_state.z1_display}</span></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="text-align: right;"><span class="result-value">{st.session_state.z1_display}</span></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Secondary Input Block ---
st.markdown('<p class="form-label">Z DE PROJET :</p>', unsafe_allow_html=True)
z_projet_input = st.text_input("Projet", label_visibility="collapsed", key="proj_in")

# --- Delta ZZ Output Row ---
st.markdown('<div class="result-row">', unsafe_allow_html=True)
r_col3, r_col4 = st.columns([1, 1])
with r_col3:
    st.markdown('<span class="result-title">DELTA ZZ :</span>', unsafe_allow_html=True)
with r_col4:
    if st.session_state.delta_is_error:
        st.markdown(f'<div style="text-align: right;"><span class="result-error">{st.session_state.delta_display}</span></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="text-align: right;"><span class="result-value">{st.session_state.delta_display}</span></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Notepad Log Box Area ---
st.markdown('<p class="form-label" style="font-size:16px;">NOTES / LOGS :</p>', unsafe_allow_html=True)
notepad_content = st.text_area("Logs", value=st.session_state.notes_log, label_visibility="collapsed")
st.session_state.notes_log = notepad_content

st.markdown('<div style="margin-top: 15px;"></div>', unsafe_allow_html=True)

# --- Mobile Navigation Buttons (Split Row layout) ---
btn_col1, btn_col2 = st.columns([2, 3])

with btn_col1:
    st.button("AC", use_container_width=True, type="secondary", on_click=clear_all_callback)

with btn_col2:
    if st.button("CALCULATE", use_container_width=True, type="primary"):
        z1_result = None
        
        # 1. Calculation Math Logic
        try:
            cote_ref = float(cote_ref_input.strip())
            lec_arr = float(lec_arr_input.strip())
            lec_av = float(lec_av_input.strip())

            z1_result = cote_ref + (lec_arr - lec_av)
            st.session_state.z1_display = f"{z1_result:.5f}"
            st.session_state.z1_is_error = False
        except ValueError:
            st.session_state.z1_display = "Error"
            st.session_state.z1_is_error = True

        try:
            z_projet = float(z_projet_input.strip())
            if z1_result is not None:
                delta_result = z1_result - z_projet
                st.session_state.delta_display = f"{delta_result:.5f}"
                st.session_state.delta_is_error = False
                
                # Append to history logs view window automatically
                st.session_state.notes_log += f"Z/1: {z1_result:.5f} | ΔZZ: {delta_result:.5f}\n"
            else:
                st.session_state.delta_display = "Invalid Z/1"
                st.session_state.delta_is_error = True
        except ValueError:
            st.session_state.delta_display = "Invalid Input"
            st.session_state.delta_is_error = True
            
        st.rerun()
