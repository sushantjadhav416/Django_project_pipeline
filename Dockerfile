FROM ubuntu:latest

# Install Maven
RUN apt-get update && \
    apt-get install -y maven

# Install Docker
RUN apt-get update && \
    apt-get install -y docker.io

# Install Trivy
RUN apt-get update && \
    apt-get install -y wget apt-transport-https gnupg lsb-release && \
    wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | apt-key add - && \
    echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | tee -a /etc/apt/sources.list.d/trivy.list && \
    apt-get update && \
    apt-get install -y trivy

# Install OWASP Dependency-Check
RUN apt-get update && \
    apt-get install -y zaproxy


ENV PATH="/dependency-check/bin:${PATH}"

CMD ["bash"]

# Copy your application code (if needed)
# COPY . .

# Example: Run Trivy scan on a sample image
# CMD ["trivy", "image", "--exit-code", "1", "alpine:3.14"]

# Example: Run Maven build
# CMD ["mvn", "clean", "install"]

# Example: Run your pipeline agent tasks
# CMD ["echo", "Pipeline agent tasks go here"]

# You can customize the Dockerfile further based on your specific requirements.
# Make sure to replace the example commands with your actual pipeline tasks.

# Build the Docker image:
# docker build -t my-pipeline-agent .

# Run the Docker container:
# docker run -it my-pipeline-agent

# Note: You may need to adjust permissions, add users, or configure other settings as needed.

# Define the entry point (optional)
#CMD ["bash"]
