# Use a base image with Ubuntu
FROM ubuntu:20.04

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    docker.io \
    maven \
    git \
    wget \
    unzip

# Install Trivy
RUN wget [1](https://github.com/aquasecurity/trivy/releases/download/v0.20.0/trivy_0.20.0_Linux-64bit.deb) && \
    dpkg -i trivy_0.20.0_Linux-64bit.deb && \
    rm trivy_0.20.0_Linux-64bit.deb

# Install OWASP Dependency-Check
RUN wget [2](https://github.com/jeremylong/DependencyCheck/releases/download/v6.4.2/dependency-check-6.4.2-release.zip) && \
    unzip dependency-check-6.4.2-release.zip && \
    rm dependency-check-6.4.2-release.zip

# Set environment variables
ENV PATH="/dependency-check/bin:${PATH}"

# Set working directory
WORKDIR /app

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
