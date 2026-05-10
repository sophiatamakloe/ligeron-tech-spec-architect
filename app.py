import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ligeron Tech-Spec Architect",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Ligeron Tech-Spec Architect")
st.subheader("Natural-language wearable intent → structured hardware recommendations")

st.markdown(
    """
    This prototype helps R&D hardware engineers and product designers translate a product idea
    into component recommendations with technical reasoning, constraint checks, and risk flags.
    """
)

with st.sidebar:
    st.header("Project Scope")
    st.write("User: R&D hardware/product designer")
    st.write("Workflow: design intent → candidate hardware components")
    st.write("Baseline: naive prompt-only component suggestion")

st.divider()

user_intent = st.text_area(
    "Enter product intent",
    value="I need a 660nm LED array that draws less than 20mA for a portable light-therapy patch.",
    height=120
)

if st.button("Generate Tech Spec"):
    st.success("Prototype output generated.")

    data = [
        {
            "Component": "660nm Red SMD LED",
            "Category": "Optics",
            "Key Specs": "660nm wavelength, <20mA current draw",
            "Fit": "Strong",
            "Reasoning": "Matches red-light therapy wavelength and low-current wearable constraint.",
            "Risk Flag": "Verify thermal limits before prototype use."
        },
        {
            "Component": "Low-power LED Driver",
            "Category": "Power Control",
            "Key Specs": "Constant current regulation",
            "Fit": "Moderate",
            "Reasoning": "Helps stabilize LED output under battery-powered conditions.",
            "Risk Flag": "Must match battery voltage range."
        },
        {
            "Component": "Flexible PCB Connector",
            "Category": "Mechanical/Electrical",
            "Key Specs": "Slim wearable-compatible package",
            "Fit": "Moderate",
            "Reasoning": "Supports compact patch-style physical design.",
            "Risk Flag": "Confirm footprint against enclosure size."
        }
    ]

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.warning(
        "Human review required: This tool supports early R&D screening only. "
        "It should not be used for final procurement or safety-critical engineering sign-off."
    )
