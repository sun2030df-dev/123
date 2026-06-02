import streamlit as st

# --- Page Setup & Configurations ---
st.set_page_config(
    page_title="Poste de Buse", 
    page_icon="📐", 
    layout="centered"
)

# Custom injection for styling text elements, headings, and input box shapes
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Impact&family=Arial&display=swap');
    
    /* Title Stylings */
    .header-banner {
        background-color: #000000;
        border-radius: 25px;
        padding: 15px;
        text-align: center;
        margin-bottom: 25px;
    }
    .header-text {
        font-family: 'Impact', sans-serif;
        font-style: italic;
        font-size: 34px;
        color: #FFFFFF;
        letter-spacing: 1px;
    }
    
    /* Form Label Settings */
    .form-label {
        font-family: 'Impact', sans-serif;
        font-style: italic;
        font-size: 22px;
        color: #000000;
        margin-top: 10px;
    }
    
    /* Result Display Rows */
    .result-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 20px 0;
    }
    .result-title {
        font-family: 'Impact', sans-serif;
        font-style: italic;
        font-size: 40px;
        color: #000000;
    }
    .result-value {
        font-family: 'Arial', sans-serif;
        font-size: 28px;
        font-weight: normal;
        color: #0066CC;
    }
    .result-error {
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        color: #FF3333;
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

# Field inputs session states (To allow AC to clear them)
if "ref_val" not in st.session_state:
    st.session_state.ref_val = ""
if "arr_val" not in st.session_state:
    st.session_state.arr_val = ""
if "av_val" not in st.session_state:
    st.session_state.av_val = ""
if "proj_val" not in st.session_state:
    st.session_state.proj_val = ""

# --- Top Header ---
st.markdown('<div class="header-banner"><span class="header-text">POSTE DE BUSE </span></div>', unsafe_allow_html=True)

# --- Form Fields Container ---
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('<p class="form-label">COTE DE REFERENCE :</p>', unsafe_allow_html=True)
with col2:
    cote_ref_input = st.text_input("Ref", value=st.session_state.ref_val, label_visibility="collapsed", key="ref_in")

col3, col4 = st.columns([3, 2])
with col3:
    st.markdown('<p class="form-label">LECTURE ARRIERE :</p>', unsafe_allow_html=True)
with col4:
    lec_arr_input = st.text_input("Arriere", value=st.session_state.arr_val, label_visibility="collapsed", key="arr_in")

col5, col6 = st.columns([3, 2])
with col5:
    st.markdown('<p class="form-label">LECTURE AVANT :</p>', unsafe_allow_html=True)
with col6:
    lec_av_input = st.text_input("Avant", value=st.session_state.av_val, label_visibility="collapsed", key="av_in")

# --- Z / 1 Row Display ---
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

# --- Secondary Input Row ---
col7, col8 = st.columns([3, 2])
with col7:
    st.markdown('<p class="form-label">Z DE PROJET :</p>', unsafe_allow_html=True)
with col8:
    z_projet_input = st.text_input("Projet", value=st.session_state.proj_val, label_visibility="collapsed", key="proj_in")

# --- Delta ZZ Row Display ---
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

# --- Notepad Area ---
st.markdown('<p class="form-label" style="font-size:18px;">NOTES / LOGS :</p>', unsafe_allow_html=True)
notepad_content = st.text_area("Logs", value=st.session_state.notes_log, height=120, label_visibility="collapsed")
st.session_state.notes_log = notepad_content

# --- Bottom Layout Control Buttons ---
btn_col1, btn_col2 = st.columns([1, 3])

with btn_col1:
    if st.button("AC", use_container_width=True, type="secondary"):
        # Reset output values
        st.session_state.z1_display = "—"
        st.session_state.delta_display = "—"
        st.session_state.z1_is_error = False
        st.session_state.delta_is_error = False
        
        # Reset text field states explicitly
        st.session_state.ref_val = ""
        st.session_state.arr_val = ""
        st.session_state.av_val = ""
        st.session_state.proj_val = ""
        st.rerun()

with btn_col2:
    if st.button("CALCULATE", use_container_width=True, type="primary"):
        # Save current input strings into session state so they persist over the rerun
        st.session_state.ref_val = cote_ref_input
        st.session_state.arr_val = lec_arr_input
        st.session_state.av_val = lec_av_input
        st.session_state.proj_val = z_projet_input
        
        z1_result = None
        
        # 1. Independent Z/1 Math Logic Block
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

        # 2. Sequential Delta ZZ Logic Block
        try:
            z_projet = float(z_projet_input.strip())
            if z1_result is not None:
                delta_result = z1_result - z_projet
                st.session_state.delta_display = f"{delta_result:.5f}"
                st.session_state.delta_is_error = False
                
                # Automatically append log history lines
                st.session_state.notes_log += f"Z/1: {z1_result:.5f} | ΔZZ: {delta_result:.5f}\n"
            else:
                st.session_state.delta_display = "Invalid Z/1"
                st.session_state.delta_is_error = True
        except ValueError:
            st.session_state.delta_display = "Invalid Input"
            st.session_state.delta_is_error = True
            
        st.rerun()
