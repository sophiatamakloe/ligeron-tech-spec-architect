# Ligeron Tech-Spec Architect

## Overview
Ligeron Tech-Spec Architect is an AI-assisted workflow prototype designed to help wearable hardware teams rapidly translate natural-language engineering intent into structured technical specification recommendations.

The application demonstrates how generative AI workflows can support early-stage hardware planning, component screening, and product requirement drafting for wearable technology systems.

This prototype focuses on improving the speed and structure of early R&D specification workflows while maintaining a human-in-the-loop review process.

---

## Problem Statement
Early-stage wearable hardware specification drafting is often slow, fragmented, and highly manual. Engineers and product designers must review multiple component categories, technical constraints, and risk considerations before beginning prototyping.

This project explores how AI-assisted workflows can accelerate:
- Requirement interpretation
- Initial component recommendation
- Constraint analysis
- Risk awareness
- Technical planning structure

---

## Features
- Natural-language engineering input
- Structured wearable hardware component recommendations
- Constraint matching analysis
- Risk flag generation
- Interactive Streamlit interface
- Human-review safety messaging

---

## Example Workflow

### User Input
“I need a 660nm LED array that draws less than 20mA for a portable light-therapy patch.”

### Generated Output
- Recommended optical components
- Suggested power-control hardware
- Mechanical/electrical integration considerations
- Constraint match evaluation
- Risk review guidance

---

## Tech Stack
- Python
- Streamlit
- Pandas

---

## Project Architecture
1. User enters wearable hardware design intent
2. Application processes the request
3. Structured component recommendations are generated
4. Constraint analysis and risk considerations are displayed
5. Human review remains required before engineering implementation

---

## Installation Instructions

### Clone Repository
```bash
git clone https://github.com/sophiatamakloe/ligeron-tech-spec-architect.git
