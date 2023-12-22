from transformers import Conversation, pipeline, AutoTokenizer

# Crear un tokenizador para el modelo DialoGPT-medium
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

# Crear una tubería para la generación de texto conversacional
nlp = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Conversación inicial
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
]

# Crear un objeto de tipo Conversation
conversation = Conversation(conversation_history)

while True:
        
    # Agregar la nueva entrada del usuario a la conversación
    user_input = input(">> User: ")
    if user_input == "exit":
        break
    conversation.add_user_input(user_input)

    # Generar una respuesta del modelo
    response = nlp(conversation)

    # Mostrar la respuesta del modelo
    print(response[-1]["content"])
