# 起始测试
from transformers import AutoTokenizer, AutoModel

MODEL_PATH = r'C:\Users\lawrence\Documents\chatglm3-6b'
TOKENIZER_PATH = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=MODEL_PATH, trust_remote_code=True)

model = AutoModel.from_pretrained(pretrained_model_name_or_path=MODEL_PATH, trust_remote_code=True,
                                  device_map="auto")
model = model.eval()


response, history = model.chat(TOKENIZER_PATH, "你好", history=[])
print(response)

response, history = model.chat(TOKENIZER_PATH, "晚上睡不着应该怎么办", history=history)

print(response)
