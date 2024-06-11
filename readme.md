# Microsoft Vision
This repo contains the dcoe base for the image analysis module from the microsoft SLM Module Phi3 Visison

## Hugging face link for the model 
Please do refer the link below for more details
https://huggingface.co/microsoft/Phi-3-vision-128k-instruct

## List of things to be done before using the model in local system

- When loading the model, ensure that trust_remote_code=True is passed as an argument of the from_pretrained() function.
- Update your local transformers to the development version: pip uninstall -y transformers && pip install git+https://github.com/huggingface/transformers. The previous command is an alternative to cloning and installing from the source.
    -   Note - In order to verify the local module please do use the following method for it `pip list | grep transformers`.


## Gathering required packages
Please do use the below command for the installing the packages.
`pip install -r requirements.txt`

## Suported GPU for the model 
- NVIDIA A100
- NVIDIA A6000
- NVIDIA H100





