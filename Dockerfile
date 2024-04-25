# Use a base image (e.g., Ubuntu, Alpine, etc.)
FROM ubuntu:latest

# Install required packages
RUN apt-get update && apt-get install -y \
    docker.io \
    maven\
    git \
    Trivy \
    OWASP 

# Add other tools here (e.g., Trivy, OWASP dependencies)

# Set up Git credentials (if needed)
RUN git config --global user.name "Your Name" && \
   git config --global user.email "your@email.com"

# Set the working directory
WORKDIR /app

# Define the entry point (optional)
CMD ["bash"]
