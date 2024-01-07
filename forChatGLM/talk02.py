# 测试langchain
import os

from langchain import hub

from langchain_demo.ChatGLM3 import ChatGLM3


llm = ChatGLM3()
MODEL_PATH = os.environ.get('MODEL_PATH', 'THUDM/chatglm3-6b')
llm.load_model(MODEL_PATH)
prompt = hub.pull("hwchase17/structured-chat-agent")
