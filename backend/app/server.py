from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from pirate_speak.chain import chain as pirate_speak_chain
from openai_functions_agent import agent_executor as openai_functions_agent_chain

app = FastAPI()

add_routes(app, pirate_speak_chain, path="/pirate-speak")
add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent")


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
