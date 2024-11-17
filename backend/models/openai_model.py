import openai

def edit_html_with_openai(html_content, instructions="Modify the HTML to include a greyscale filter."):
    """
    Use OpenAI's API to edit the given HTML content.
    """
    prompt = f"""You are an AI assistant helping to modify HTML code.
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
