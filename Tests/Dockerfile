# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Set the display environment variable
ENV DISPLAY=:0

# Install X11 server and window manager
RUN apt-get update && apt-get install -y x11-apps x11-utils x11vnc xvfb openbox

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run when the container starts
CMD ["python", "main.py"]
