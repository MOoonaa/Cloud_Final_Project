
# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the local directory's contents into the container at /app
COPY . /app

# Install Python dependencies listed in requirements.txt using pip
RUN pip install -r requirements.txt

# Specify the command to run when the container starts
CMD python ./app.py


