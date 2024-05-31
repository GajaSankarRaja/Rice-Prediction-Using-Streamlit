# Use an official Python 3.10 image as the base image
FROM python:3.8-slim

# Set the default shell to Bash
SHELL ["/bin/bash", "-c"]

# Set the working directory to /app
WORKDIR /Streamlit

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

#copy pk_file
COPY pickle.sav .

#create env
RUN python -m venv env

#activating env
ENV pycode env Scripts activate

#pip timer
ENV PIP_DOWNLOAD_TIMEOUT=300

#upgrade pip
RUN pip install --upgrade pip

# Install the required packages using pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 5000 for the application
EXPOSE 8501

# Set the command to run the application
CMD ["streamlit", "run", "Streamlite.py"]
