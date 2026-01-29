def extract_action_items(text):
    keywords = ["need to", "should", "will", "action", "follow up", "decide"]
    actions = []

    for line in text.split("."):
        for key in keywords:
            if key in line.lower():
                actions.append(line.strip())
                break

    if not actions:
        return ["No clear action items identified."]

    return actions
