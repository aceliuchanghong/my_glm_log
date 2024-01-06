from transformers import AutoTokenizer, AutoModel

model_path = r'C:\Users\lawrence\Documents\chatglm3-6b'
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=model_path, trust_remote_code=True)
print('response1')
model = AutoModel.from_pretrained(pretrained_model_name_or_path=model_path, trust_remote_code=True, device='cuda')
print('response2')
model = model.eval()
print('response3')

response, history = model.chat(tokenizer, "你好", history=[])
print(response)

response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)

print(response)

