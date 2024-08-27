#!/usr/bin/env python

import sys
import requests

API_TOKEN = ""
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"


def query(payload):
    """
    Run the Hugging Face query with the given payload
    """

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=20)

        return response.json()

    except Exception as e:

        return False

def get_summary(text):
    """
    Get a summary of the text from Hugging Face using Bart
    """

    data = query(
            {
                "inputs": text,
                "parameters": {"do_sample": False},
            }
    )

    if data:

        return data[0]['summary_text']

    return "Unable to obtain summary"

def main():
    """
    Summarize text using Hugging Face
    """

    # Check if text provided as system arg
    if len(sys.argv) < 2:
        # If not, prompt the user for input
        text = input("Please enter text to summarize:")
    else:
        text = ' '.join(sys.argv[1:])

    summary = get_summary(text)
    print("\nSummary:\n")
    print(summary)


if __name__ == "__main__":
    main()
