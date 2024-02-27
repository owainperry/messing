from fastapi import FastAPI

# That is the file where NeuralSearcher is stored
from neural_searcher import NeuralSearcher

app = FastAPI()

# Create an instance of the neural searcher
neural_searcher = NeuralSearcher(collection_name='demo_collection')

@app.get("/api/search")
def search_startup(q: str):
    return {
        "result": neural_searcher.search(text=q)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
