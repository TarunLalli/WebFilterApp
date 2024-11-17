from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from models.openai_model import edit_html_with_openai  # Import the function from models folder

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key is missing. Please add it to the .env file.")

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_html():
    """
    Handle POST requests to process HTML content.
    """
    data = request.json
    html = data.get('html')

    if not html:
        return jsonify({"error": "No HTML content provided."}), 400

    # Define the instructions for the edit
    instructions = "Modify the HTML to include a color filter."

    # Use the OpenAI API to modify the HTML
    modified_html = edit_html_with_openai(html, instructions)
    if modified_html:
        return jsonify({"modifiedHtml": modified_html})
    else:
        return jsonify({"error": "Failed to process HTML."}), 500

if __name__ == '__main__':
    app.run(port=5000)