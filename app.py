import chainlit as cl
from embedchain import App
import os

os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"

@cl.on_chat_start
async def on_chat_start():
    app = App.from_config(config_path="config.yaml")

    # import your data here
    app.add('sample_data.csv')
    app.collect_metrics = False
    cl.user_session.set("app", app)

@cl.on_message
async def on_message(message: cl.Message):
    app = cl.user_session.get("app")
    msg = cl.Message(content="")
    for chunk in await cl.make_async(app.chat)(message.content):
        await msg.stream_token(chunk)
    
    await msg.send()