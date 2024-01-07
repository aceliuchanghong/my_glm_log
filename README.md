# my_glm_log

the log of doing ChatGLM model

### purpose

build a saas in server then give api,so i can use

* 语音转文字==>faster-whisper git@github.com:SYSTRAN/faster-whisper.git
* 文字转语音==>TTS没想好看谁的
* 声音克隆
* llm==>ChatGLM git@github.com:THUDM/ChatGLM3.git LLaMA-7B
* sd的lora也可以试试==>之后再说

### install

#pip freeze > requirements.txt

git clone git@github.com:aceliuchanghong/my_glm_log.git

conda create -n myGLM python=3.10

conda activate myGLM

pip install -r requirements.txt --proxy=127.0.0.1:10809

python cli_demo.py

python web_demo_gradio.py

#conda deactivate
#conda remove -n myGLM --all
## 查看cuda版本和占用情况

nvidia-smi