import os

def generate_invitations(template, attendees):
    # Tip yoxlaması
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # Boş giriş yoxlaması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal
    for i, attendee in enumerate(attendees, start=1):
        invitation = template
        
        # Placeholder siyahısı
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            value = attendee.get(key)
            # Əgər dəyər yoxdursa və ya None-dırsa "N/A" ilə əvəzlə
            replacement = value if value is not None else "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(replacement))
        
        # Fayla yazma
        filename = f"output_{i}.txt"
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. Overwriting...")
        
        try:
            with open(filename, 'w') as f:
                f.write(invitation)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")

