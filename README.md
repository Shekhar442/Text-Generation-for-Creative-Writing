# AI-Powered Writing Assistant

This project implements an AI-powered writing assistant using the GPT-2 language model. It generates creative writing content based on user prompts and selected genres.

## Features

- Generates text using the GPT-2 medium model
- Supports multiple genres: Sci-Fi, Fantasy, Historical Fiction, Mystery, and Romance
- Allows users to input custom prompts
- Adjustable maximum length for generated text
- User-friendly interface built with Gradio

## Requirements

- Python 3.6+
- PyTorch
- Transformers
- Gradio

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-writing-assistant.git
   cd ai-writing-assistant
   ```

2. Install the required packages:
   ```
   pip install torch transformers gradio
   ```

## Usage

1. Run the script:
   ```
   python writing_assistant.py
   ```

2. Open your web browser and go to the URL displayed in the console (usually `http://localhost:7860`).

3. In the web interface:
   - Enter your writing prompt in the text box
   - Select a genre from the dropdown menu
   - Adjust the maximum length using the slider
   - Click "Submit" to generate the text

## How it Works

1. The script loads a pre-trained GPT-2 medium model and tokenizer.
2. It defines genre-specific prompts to guide the text generation.
3. When a user inputs a prompt and selects a genre, the script combines the user's prompt with the genre-specific prompt.
4. The combined prompt is then fed into the GPT-2 model to generate creative text.
5. The generated text is displayed to the user through the Gradio interface.

## Customization

- To add or modify genres, update the `genres` dictionary in the script.
- Adjust the `temperature`, `top_k`, and `top_p` parameters in the `generate_text` function to control the creativity and randomness of the generated text.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- This project uses the GPT-2 model from the Transformers library by Hugging Face.
- The user interface is built using Gradio.

# Text-Generation-for-Creative-Writing