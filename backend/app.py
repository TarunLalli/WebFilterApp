from flask import Flask, request, jsonify
from llama_cpp import Llama

app = Flask(__name__)

# Load your Llama model
llm = Llama(model_path="path_to_llama_model")

@app.route('/process', methods=['POST'])
def process_html():
    data = request.json
    html = data.get('html')

    # Generate new source code with a color filter applied
    prompt = f"Modify the following HTML to include a color filter: {html}"
    modified_html = llm(prompt)

    return jsonify({"modifiedHtml": modified_html["choices"][0]["text"]})

if __name__ == '__main__':
    app.run(port=5000)
