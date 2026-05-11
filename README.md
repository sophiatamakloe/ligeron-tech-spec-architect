# Ligeron Tech Spec Architect

## Overview

Ligeron Tech Spec Architect is a focused GenAI workflow prototype that converts natural-language wearable hardware design intent into structured technical specification recommendations.

The tool is designed for early-stage R&D hardware teams, product strategists, and engineering teams exploring rapid component screening and technical planning workflows.

This prototype demonstrates how generative AI can assist with:

- Hardware component recommendation
- Constraint analysis
- Technical reasoning
- Risk identification
- Human review escalation

---

## Example Use Case

Input:

> “I need a 660nm LED array that draws less than 20mA for a portable light-therapy patch.”

Generated Output Includes:

- Recommended component types
- Constraint matching
- Technical reasoning
- Engineering tradeoffs
- Risk flags
- Human review warnings

---

## Workflow Architecture

User Intent → Prompt Structuring → Gemini API → Structured Technical Recommendation Output

The application uses:

- Streamlit (UI)
- Google Gemini API
- Python
- Prompt engineering workflow design
The system also includes a fallback demonstration mode when Gemini API quota or availability limitations occur, allowing uninterrupted workflow evaluation.

---

## Key Features

- Natural-language hardware design input
- AI-generated structured technical specs
- Constraint-aware reasoning
- Engineering risk flag generation
- Human review requirement layer
- Lightweight interactive UI

---

## Evaluation Approach

The workflow was tested using realistic wearable hardware design prompts involving:

- LED wavelength constraints
- Battery limitations
- Form-factor restrictions
- Thermal considerations
- Low-power wearable systems

The system performed well for:

- Early-stage architecture recommendations
- Structured planning outputs
- Technical brainstorming support

The system is NOT intended for:

- Final engineering validation
- Procurement decisions
- Regulatory certification
- Medical-device approval

Human review is required before implementation.

---

## Baseline Comparison

Baseline approach:
- Manual internet research
- Spreadsheet-based component tracking
- Unstructured brainstorming

AI-assisted workflow advantages:
- Faster structured outputs
- Immediate technical organization
- Integrated risk considerations
- More consistent documentation format

---

## Limitations

- Outputs may contain inaccuracies or hallucinations
- Recommendations should not replace certified engineering review
- AI cannot guarantee regulatory compliance
- Technical validation is still required

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sophiatamakloe/ligeron-tech-spec-architect.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run app.py
```

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API

---

## Author

Sophia Tamakloe
Johns Hopkins University — MSAI
---

## Installation Instructions

### Clone Repository
```bash
git clone https://github.com/sophiatamakloe/ligeron-tech-spec-architect.git
## Demo Screenshots

### Live Gemini-Generated Technical Recommendation

![Live Gemini Output](screenshots/live_gemini_output.png)

---

### Reliability Fallback Mode

When Gemini API quota or availability issues occur, the system automatically switches to a structured fallback demo mode for uninterrupted evaluation.

![Fallback Mode](screenshots/fallback_mode.png)
