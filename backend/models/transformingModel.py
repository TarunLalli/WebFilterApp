from dotenv import load_dotenv
import os
import openai

# Load environment variables from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def edit_html_with_openai(html_content, instructions):
    """
    Use OpenAI's API to edit the given HTML content based on the instructions.

    Parameters:
    - html_content: The raw HTML string to be processed.
    - instructions: Instructions for how the HTML should be modified.

    Returns:
    - The modified HTML content.
    """
    prompt = f"""You are an AI assisting with HTML modifications.
    Here is the HTML content:
    {html_content}
    
    Instructions: {instructions}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None
    
if __name__ == "__main__":
    # Load the HTML file (or string)
    with open("input.html", "r") as file:
        html_content = file.read()

    # Define instructions for the edit
    instructions = "Add a 'dark mode' toggle button at the top of the page."

    # Process the HTML using OpenAI API
    edited_html = edit_html_with_openai(html_content, instructions)

    # Save the edited HTML to an output file
    if edited_html:
        with open("output.html", "w") as file:
            file.write(edited_html)
        print("Edited HTML saved to output.html")
    else:
        print("Failed to edit HTML.")