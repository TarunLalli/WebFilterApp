from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
from dotenv import load_dotenv
import os
from models.openai_model import edit_html_with_openai  # Assuming you are using a separate model file

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key is missing. Please add it to the .env file.")

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

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
