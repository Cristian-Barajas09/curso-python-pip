import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact',response_class=HTMLResponse)
def get_list():
    return """
        <h1>this is a contact</h1>
    """

@app.get('/this')
def get_list():
    return {"this":"esta es otra ruta"}

def run():
    store.get_categories()


if __name__ == "__main__":
    run()

# uvicorn main:app --reload
"""
--reload: recargar el servidor
"""