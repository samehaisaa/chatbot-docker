# Use the custom base image with PyTorch and transformers
FROM my-pytorch-base

# Set the working directory in the container
WORKDIR /app

# Copy the chatbot code and any necessary files into the container
COPY chatbot.py /app/

# Expose the port if your chatbot is intended to run as a web service
# EXPOSE 5000

# Define the default command to run your chatbot script
CMD ["python", "chatbot.py"]
