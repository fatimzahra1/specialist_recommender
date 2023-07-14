# Use the official Anaconda base image
FROM continuumio/anaconda3:latest

# Set the working directory in the container
WORKDIR /specialist_recommender

# Copy the contents of the specialist recommender folder to the container
COPY app.py trained_model.joblib .

RUN pip install waitress

# Expose the port your app will run on
EXPOSE 5000

# Set the command to run your app
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]