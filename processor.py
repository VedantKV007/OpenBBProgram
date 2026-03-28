import json

def process_tickets():
    # In a real scenario, this data would be passed to an LLM API
    with open('data/tickets.json', 'r') as f:
        tickets = json.load(f)

    print(f"Loading {len(tickets)} tickets for AI analysis...")
    # The AI reads the concatenated string of these tickets
    combined_text = " ".join([t['content'] for t in tickets])
    return combined_text

if __name__ == "__main__":
    content = process_tickets()
    print("AI is now processing the following content...")