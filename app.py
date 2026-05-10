import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ligeron Tech-Spec Architect",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Ligeron Tech-Spec Architect")
st.subheader("Natural-language wearable hardware intent → structured component recommendations")

st.markdown(
    "A focused GenAI workflow prototype for R&D hardware engineers and product designers."
)

user_input = st.text_area(
    "Enter wearable hardware design intent:",
    value="I need a 660nm LED array that draws less than 20mA for a portable light-therapy patch.",
    height=120
)

if st.button("Generate Tech Spec"):
    st.success("Structured tech-spec generated.")

    data = [
        {
            "Component Type": "660nm Red SMD LED",
            "Category": "Optics",
            "Constraint Match": "Strong",
            "Reasoning": "Matches red-light wavelength target and low-current wearable use case.",
            "Risk Flag": "Verify thermal limits and supplier datasheet before prototype."
        },
        {
            "Component Type": "Low-Power LED Driver",
            "Category": "Power Control",
            "Constraint Match": "Moderate",
            "Reasoning": "Supports stable current delivery for battery-powered light therapy.",
            "Risk Flag": "Confirm compatibility with battery voltage and LED current range."
        },
        {
            "Component Type": "Flexible PCB Connector",
            "Category": "Mechanical/Electrical",
            "Constraint Match": "Moderate",
            "Reasoning": "Supports slim, patch-style wearable form factor.",
            "Risk Flag": "Validate footprint against enclosure constraints."
        }
    ]

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.warning(
        "Human review required: This tool supports early R&D screening only. "
        "It is not a substitute for final engineering, safety, or procurement review."
    )
