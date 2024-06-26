from PIL import Image 
import requests 
from transformers import AutoModelForCausalLM 
from transformers import AutoProcessor 
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/get-image-insights/")
def read_item(image_url: str, question: str):
    model_id = "microsoft/Phi-3-vision-128k-instruct" 
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda", trust_remote_code=True, torch_dtype="auto", _attn_implementation='flash_attention_2') # use _attn_implementation='eager' to disable flash attention
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True) 
    messages = [ 
        {"role": "user", "content": "<|image_1|>\nWhat is shown in this image?"},
        {"role": "user", "content": question}   
    ] 
    url = "https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2024/04/BMDataViz_661fb89f3845e.png" 
    image = Image.open(requests.get(image_url, stream=True).raw) 
    prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(prompt, [image], return_tensors="pt").to("cuda:0") 
    generation_args = { 
        "max_new_tokens": 500, 
        "temperature": 0.0, 
        "do_sample": False, 
    } 
    generate_ids = model.generate(**inputs, eos_token_id=processor.tokenizer.eos_token_id, **generation_args) 

    # remove input tokens 
    generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
    response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] 

    return response


@app.get("/get-discussion-questions/")
def read_item(image_url: str, question: str, chart_definition: str, chart_action: str):
    model_id = "microsoft/Phi-3-vision-128k-instruct" 
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda", trust_remote_code=True, torch_dtype="auto", _attn_implementation='flash_attention_2') # use _attn_implementation='eager' to disable flash attention
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True) 
    messages = [ 
        {"role": "user", "content": "<|image_1|>\nWhat is shown in this image?"},
        {"role": "assistant", "content": chart_definition}, 
        {"role": "user", "content": chart_action} 
]  
    url = "https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2024/04/BMDataViz_661fb89f3845e.png" 
    image = Image.open(requests.get(image_url, stream=True).raw) 
    prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(prompt, [image], return_tensors="pt").to("cuda:0") 
    generation_args = { 
        "max_new_tokens": 500, 
        "temperature": 0.0, 
        "do_sample": False, 
    } 
    generate_ids = model.generate(**inputs, eos_token_id=processor.tokenizer.eos_token_id, **generation_args) 

    # remove input tokens 
    generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
    response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] 

    return response


