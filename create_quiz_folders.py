import os
import re

def create_quiz_folders():
    questions = [
        "HTMX Attributes - hx-swap",
        "HTMX Attributes - hx-trigger",
        "HTMX Attributes - Other Important Attributes",
        "Events in HTMX - HTMX-generated events",
        "Events in HTMX - Server-generated events",
        "Events in HTMX - Using htmx:configRequest",
        "Events in HTMX - Canceling requests with htmx:abort",
        "HTTP Requests & Responses - Custom headers in HTMX",
        "HTTP Requests & Responses - HTTP response codes and HTMX behavior",
        "Updating Other Content - Expanding selection",
        "Updating Other Content - Out of Band swaps",
        "Updating Other Content - Event-driven updates",
        "Debugging HTMX - Using htmx.logAll()",
        "Debugging HTMX - Monitoring events in Chrome",
        "Security Considerations - Content Security Policies",
        "Security Considerations - Using hx-disable",
        "Configuring HTMX - Setting config options via meta tags",
        "Advanced HTMX Techniques - Synchronizing requests with hx-sync",
        "Advanced HTMX Techniques - Using event filters",
        "Advanced HTMX Techniques - Working with synthetic events",
        "HTMX Attributes - hx-swap modifiers",
        "HTMX Attributes - hx-trigger modifiers",
        "HTTP Requests & Responses - HX-Trigger response header",
        "Updating Other Content - Expanding target selection",
        "Debugging HTMX - Using Chrome's monitorEvents()",
        "Security Considerations - Escaping user-generated content",
        "Configuring HTMX - Default swap style",
        "Advanced HTMX Techniques - Using hx-push-url",
        "Advanced HTMX Techniques - Preserving elements with hx-preserve",
        "Advanced HTMX Techniques - Disabling HTMX with hx-disable"
    ]

    for i, question in enumerate(questions, 1):
        # Create a shorter folder name
        main_topic = question.split(' - ')[0].lower().replace(' ', '_')
        folder_name = f"{i:02d}_{main_topic}"
        os.makedirs(folder_name, exist_ok=True)

        # Create README.md file with full question as H1
        with open(os.path.join(folder_name, "README.md"), "w") as f:
            f.write(f"# {question}\n\n")
            f.write("This folder contains a quiz question about the following HTMX topic:\n\n")
            f.write(f"{question}\n\n")
            f.write("Please refer to the HTMX documentation for more information on this topic.")

    print(f"Created {len(questions)} quiz question folders with README files.")

create_quiz_folders()