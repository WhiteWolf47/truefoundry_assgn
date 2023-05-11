import uvicorn
import argparse
from fastapi import FastAPI
import requests

app = FastAPI()

def convert_to_v2_protocol(pipeline_name, model_url, data):
    headers = {"Content-Type": "application/json"}
    url = f"{model_url}/{pipeline_name}/infer"

    if pipeline_name == "zero-shot-classification":
        # Convert input data to V2 protocol for zero-shot-classification
        payload = {
            "inputs": {
                "array_inputs": [data["inputs"]["key"]],
                "candidate_labels": ["label_1", "label_2"]  # Add the desired candidate labels
            }
        }
    elif pipeline_name == "object-detection":
        # Convert input data to V2 protocol for object-detection
        payload = {
            "inputs": {
                "inputs": data["inputs"]["key"]
            }
        }
    elif pipeline_name == "text-generation" or pipeline_name == "tiny-gpt2":
        # Convert input data to V2 protocol for text-generation or tiny-gpt2
        payload = {
            "inputs": {
                "array_inputs": [data["inputs"]["key"]]
            }
        }
    elif pipeline_name == "token-classification" or pipeline_name == "biomedical-ner-all":
        # Convert input data to V2 protocol for token-classification or biomedical-ner-all
        payload = {
            "inputs": {
                "args": [data["inputs"]["key"]]
            }
        }
    else:
        # Pipeline not supported
        raise ValueError("Unsupported pipeline")

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

@app.get("/")
async def convert_input(hf_pipeline: str, model_deployed_url: str):
    input_data = {
        "inputs": {
            "key": "value"
        }
    }

    try:
        result = convert_to_v2_protocol(hf_pipeline, model_deployed_url, input_data)
        return result
    except ValueError as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hf_pipeline", type=str, help="Hugging Face pipeline name")
    parser.add_argument("--model_deployed_url", type=str, help="Deployed endpoint URL of the Hugging Face model")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=8000)
