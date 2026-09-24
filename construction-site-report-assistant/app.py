import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_site_report(project_data):
    prompt = f"""
You are an AI construction project reporting assistant.

Convert the following daily site information into a professional
construction site report.

Project information:
{project_data}

The report should contain:
1. Project name
2. Date
3. Weather
4. Work activities
5. Materials
6. Manpower
7. Equipment
8. Issues or delays
9. Recommended actions

Keep the report concise, professional, and suitable for submission
to a project manager.
"""
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


def main():
    print("=" * 50)
    print("AI CONSTRUCTION SITE REPORT ASSISTANT")
    print("=" * 50)

    project_data = input(
        "\nEnter today's site information:\n"
    )

    print("\nGenerating report...\n")

    report = generate_site_report(project_data)

    print("=" * 50)
    print("GENERATED SITE REPORT")
    print("=" * 50)
    print(report)


if __name__ == "__main__":
    main()
