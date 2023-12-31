# Use the official Anaconda base image
FROM continuumio/anaconda3:latest

# Set the working directory in the container
WORKDIR /specialist_recommender

# Copy the contents of the specialist recommender folder to the container
COPY app.py trained_model.joblib requirements.txt symptoms.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app will run on
EXPOSE 5000

# Set the command to run your app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--threads", "8", "--timeout", "0", "app:app"]

