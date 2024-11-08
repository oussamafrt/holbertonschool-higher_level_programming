import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            invitation = invitation.replace(f"{{{placeholder}}}", value if value is not None else "N/A")

        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(invitation)
            print(f"Generated: {filename}")
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")

