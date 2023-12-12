from chain import get_chain
from prompt import prompt_template


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes


import os

# os.environ["OPENAI_API_KEY"] = "key"

bot =  get_chain(prompt_template)

origins = [
  'http://localhost:5173'
]

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

add_routes(
    app,
    bot,
    path="/",
)

if __name__ == "__main__":
    import uvicorn
    print(prompt_template.format(context="The president", question="Who is the president?"))
    uvicorn.run(app, host="localhost", port=8000)