# Specialist Recommender

This project is a specialist recommender system based on symptom inputs. It predicts the potential medical specialist based on the symptoms provided.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Specialist Recommender is a web-based application that utilizes a machine learning model to predict the appropriate medical specialist based on the symptoms entered by the user. It helps in triaging patients and providing initial recommendations for medical care.

The application is built using Python, Flask framework, and scikit-learn library. It employs a pre-trained machine learning model that takes symptom inputs and predicts the potential specialist.

## Installation

To install and run the Specialist Recommender locally, follow these steps:

1. Clone the repository:

git clone https://github.com/your-username/specialist-recommender.git

2. Change into the project directory:
   cd specialist-recommender
3. Install the required dependencies:
   pip install -r requirements.txt
4. Load the pre-trained machine learning model:

- Place the `trained_model.joblib` file in the project directory.

5. Run the Flask application:
   python app.py

The application will start running on http://localhost:5000.

## Usage

To use the Specialist Recommender, follow these steps:

1. Ensure that the application is running by visiting http://localhost:5000 in your web browser.

2. Use the API endpoints or interact with the web interface to predict the specialist based on the symptoms provided.

## API Endpoints

The Specialist Recommender provides the following API endpoints:

- `GET /` - Retrieves a list of available symptoms.
- `POST /predict` - Makes a prediction based on the provided symptoms.


## Contributing

Contributions to the Specialist Recommender project are welcome and encouraged! If you find any bugs, issues, or want to contribute enhancements, please open a new issue or submit a pull request.

When contributing to this repository, please first discuss the change you wish to make via an issue.

## License

This project is licensed under the [MIT License](LICENSE).

