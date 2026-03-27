# task_00_intro.py

def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendee dicts.

    Files are written as: output_1.txt, output_2.txt, ...
    """

    # --- Type checks ---
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # --- Empty checks ---
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- Process each attendee ---
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        # Build a safe dict with "N/A" for missing or None values
        data = {}
        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            data[key] = value

        # Use str.format with our data dict
        try:
            filled = template.format(**data)
        except KeyError as e:
            # In case the template has unexpected placeholders;
            # you could handle differently, but we'll just skip.
            print(f"Missing placeholder in data for key: {e}")
            continue

        # Output file name: output_X.txt
        filename = f"output_{idx}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(filled)
