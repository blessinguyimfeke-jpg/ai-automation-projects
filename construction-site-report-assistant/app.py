import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
page_title="AI Construction Site Report Assistant",
page_icon="🏗️",
layout="centered"
)

st.title("🏗️ AI Construction Site Report Assistant")
st.write(
"Enter your daily construction site information below "
"and generate a professional site report."
)

project_name = st.text_input("Project Name")
date = st.date_input("Date")
weather = st.text_input("Weather")

work_activities = st.text_area(
"Work Activities",
placeholder="Example: Road excavation, sub-base placement, drainage construction..."
)

materials = st.text_area(
"Materials",
placeholder="Example: 120 tonnes of stone base received..."
)

manpower = st.text_area(
"Manpower",
placeholder="Example: 15 laborers, 2 engineers, 1 surveyor..."
)

equipment = st.text_area(
"Equipment",
placeholder="Example: Excavator, grader, roller, water tanker..."
)

issues = st.text_area(
"Issues or Delays",
placeholder="Describe any delays, site problems, or challenges..."
)

recommended_actions = st.text_area(
"Recommended Actions",
placeholder="Enter any recommended actions or leave blank for AI suggestions."
)

if st.button("Generate Site Report"):

if not api_key:
    st.error("OpenAI API key is not configured.")
elif not project_name or not work_activities:
    st.warning("Please enter at least the project name and work activities.")
else:
    client = OpenAI(api_key=api_key)

    project_data = f"""

Project Name: {project_name}
Date: {date}
Weather: {weather}
Work Activities: {work_activities}
Materials: {materials}
Manpower: {manpower}
Equipment: {equipment}
Issues or Delays: {issues}
Recommended Actions: {recommended_actions}
"""

    prompt = f"""

You are an AI construction project reporting assistant.

Convert the following daily site information into a professional
construction site report.

{project_data}

The report should contain:

1. Project Name
2. Date
3. Weather
4. Work Activities
5. Materials
6. Manpower
7. Equipment
8. Issues or Delays
9. Recommended Actions

Keep the report concise, professional, technically accurate,
and suitable for submission to a project manager.
"""

    with st.spinner("Generating professional site report..."):

        try:
            response = client.responses.create(
                model="gpt-5",
                input=prompt
            )

            report = response.output_text

            st.success("Site report generated successfully!")

            st.subheader("Generated Site Report")
            st.write(report)

        except Exception as e:
            st.error(f"An error occurred: {e}")
