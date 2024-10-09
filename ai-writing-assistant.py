import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import gradio as gr

# Load pre-trained model and tokenizer
model_name = "gpt2-medium"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Define genres and their corresponding prompts
genres = {
    "Sci-Fi": "In a distant galaxy,",
    "Fantasy": "In a realm of magic and wonder,",
    "Historical Fiction": "In the year 1876,",
    "Mystery": "The detective examined the crime scene,",
    "Romance": "Their eyes met across the crowded room,",
}

def generate_text(prompt, genre, max_length=100):
    # Prepend the genre-specific prompt
    full_prompt = f"{genres[genre]} {prompt}"
    
    # Encode the input and generate text
    input_ids = tokenizer.encode(full_prompt, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length + len(input_ids[0]),
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
    )
    
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

def writing_assistant(prompt, genre, max_length):
    generated_text = generate_text(prompt, genre, max_length)
    return generated_text

# Create the Gradio interface
iface = gr.Interface(
    fn=writing_assistant,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter your writing prompt here..."),
        gr.Dropdown(choices=list(genres.keys()), label="Select Genre"),
        gr.Slider(minimum=50, maximum=200, step=10, label="Max Length", value=100),
    ],
    outputs="text",
    title="AI-Powered Writing Assistant",
    description="Generate creative writing content based on your prompt and selected genre.",
)

# Launch the interface
iface.launch(True)