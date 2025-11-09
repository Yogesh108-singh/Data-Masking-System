import streamlit as st
import pandas as pd
import hashlib
import io

\
st.set_page_config(
    page_title=" Data Masking System",
    page_icon="🛡️",
    layout="wide"
)


st.markdown("""
    <style>
    /* Global dark background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }

    /* Wider content area */
    .block-container {
        max-width: 1500px !important;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }

    /* Dataframe styling */
    div[data-testid="stDataFrame"] div[role="gridcell"] {
        color: #FFFFFF !important;
    }

    /* Buttons */
    .stButton button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 0.7em 1.4em;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #1E40AF;
        transform: scale(1.02);
    }

    /* Download button */
    .stDownloadButton button {
        background-color: #22C55E;
        color: white;
        border-radius: 8px;
        padding: 0.7em 1.4em;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }
    .stDownloadButton button:hover {
        background-color: #15803D;
        transform: scale(1.02);
    }

    /* Headings */
    h1, h2, h3 {
        color: #93C5FD;
    }

    /* Info boxes */
    .stAlert {
        border-radius: 10px !important;
    }

    </style>
""", unsafe_allow_html=True)


# MASKING LOGIC

PATTERNS = ["email", "phone", "contact", "card", "ssn", "pan", "aadhar"]

def mask_value(val, mode):
    """Apply masking based on selected mode"""
    if pd.isna(val) or str(val).strip() == "":
        return val
    val = str(val).strip()

    if mode == "Redact":
        return "⬛REDACTED⬛"
    elif mode == "Partial":
        return "*" * (len(val) - 4) + val[-4:]
    elif mode == "Hash":
        return "####" + hashlib.sha256(val.encode()).hexdigest()[:10] + "####"
    return val

def detect_sensitive_columns(columns):
    """Auto-detect sensitive columns"""
    return [col for col in columns if any(key in col.lower() for key in PATTERNS)]



# MAIN CONTENT

st.title("🛡️ Data Masking System")
st.markdown("""
Upload a **CSV file**, automatically detect sensitive columns,  
and apply **Redact**, **Partial**, or **Hash** masking to protect private data.  
All operations happen locally — no data is sent anywhere.
""")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding="latin-1", on_bad_lines="skip")
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        st.stop()

    st.success("✅ File uploaded successfully!")

    # Layout columns for broader UI
    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("⚙️ Options")
        mode = st.selectbox("🎭 Masking Mode", ["Redact", "Partial", "Hash"])
        sensitive_cols = detect_sensitive_columns(df.columns)

        if sensitive_cols:
            st.info(f"Detected: {', '.join(sensitive_cols)}")
        else:
            st.warning("⚠️ No sensitive columns detected automatically.")
            sensitive_cols = []

        selected_cols = st.multiselect(
            "✅ Select columns to mask",
            df.columns.tolist(),
            default=sensitive_cols
        )

        if st.button("🚀 Apply Masking"):
            if not selected_cols:
                st.warning("Please select at least one column to mask.")
            else:
                df_masked = df.copy()
                for col in selected_cols:
                    df_masked[col] = df_masked[col].apply(lambda x: mask_value(x, mode))

                buffer = io.StringIO()
                df_masked.to_csv(buffer, index=False, encoding="latin-1")
                masked_csv = buffer.getvalue()

                st.success(f"✅ Masking completed! {len(selected_cols)} column(s) masked.")

                st.download_button(
                    label="💾 Download Masked CSV File",
                    data=masked_csv,
                    file_name="masked_data.csv",
                    mime="text/csv",
                    use_container_width=True
                )

                with col2:
                    st.subheader("🔍 Masked Data Preview")
                    st.dataframe(df_masked.head(20), use_container_width=True)

    # Show original data below for reference
    st.subheader("📄 Original Data Preview")
    st.dataframe(df.head(20), use_container_width=True)

else:
    st.info("👆 Upload a CSV file to start masking sensitive data.")


