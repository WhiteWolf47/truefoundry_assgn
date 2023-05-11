# Hugging Face Inference API

This repository contains a Python code that serves as an API for making inference requests to Hugging Face models using the V2 inference protocol. It provides a FastAPI web application that accepts input data, converts it to the appropriate protocol format, and sends a POST request to the deployed model endpoint.

## Prerequisites

Before running the code, ensure that you have the following:

- Python 3.7 or higher installed
- Required Python packages installed (can be installed using `pip install -r requirements.txt`)

## How to Run the Code

1. Clone the repository to your local machine:

```shell
git clone https://github.com/WhiteWolf47/truefoundry_assgn
cd truefoundry_assgn
```

2. Install the required libraries
```shell
pip install -r requirements.txt
```

3. Start the FastAPI server
```shell
python main.py --hf_pipeline <pipeline_name> --model_deployed_url <model_url>
```
Replace <pipeline_name> with the desired Hugging Face pipeline (e.g., zero-shot-classification, object-detection, etc.), and <model_url> with the deployed endpoint URL of the Hugging Face model.

4. The server should now be running on http://localhost:8000

5.Send a GET request to the API endpoint using tools like cURL or a web browser. The API will convert the input data to the V2 protocol, make a request to the model endpoint, and return the response.
Supported Pipelines
This code supports the following Hugging Face pipelines:

zero-shot-classification: Zero-shot text classification
object-detection: Object detection
text-generation: Text generation
token-classification: Token classification
biomedical-ner-all: Biomedical named entity recognition
Ensure that you provide the correct pipeline name and model URL when making the API request.

