from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

def chat():
    # Initialize the chatbot using a pre-trained model (DialoGPT-medium)
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium", device=-1)  # Use CPU (-1) or GPU (0)

    # Load the tokenizer and model manually for better control
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

    # Set the pad token to the eos_token (end-of-sequence token)
    tokenizer.pad_token = tokenizer.eos_token

    print("Hello! I'm your AI chatbot. Type 'quit' to end the conversation.")
    
    conversation_history = ""
    
    while True:
        # Take user input
        user_input = input("You: ")
        
        # Break the loop if the user types 'quit'
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Add user input to the conversation history
        conversation_history += f"You: {user_input}\n"
        
        # Encode the conversation history with truncation to avoid overly long input sequences
        inputs = tokenizer(conversation_history, return_tensors='pt', padding=True, truncation=True, max_length=1024)

        # Generate a response (set do_sample=True to allow randomness)
        output = chatbot(conversation_history, 
                         max_length=1000, 
                         num_return_sequences=1, 
                         pad_token_id=tokenizer.eos_token_id, 
                         top_k=50,  # Control diversity with top-k
                         top_p=0.95,  # Cumulative probability cutoff
                         do_sample=True)  # Allow sampling for more diverse answers

        # Extract the generated response
        ai_response = output[0]['generated_text'].split("\n")[-1]  # Get only the AI's last response
        
        # Ensure that we don't duplicate the conversation history by trimming
        conversation_history += f"AI: {ai_response}\n"  # Add AI's response to the conversation history
        
        # Print AI's response
        print(f"AI: {ai_response}")

# Multiprocessing safety for Windows
if __name__ == "__main__":
    try:
        # Start chat
        chat()
    except Exception as e:
        print("Error occurred:", e)
