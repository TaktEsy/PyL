from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def main() -> dict:
    return {"message": "Главная страницA!"}
@app.get("/user/admin/")
async def main() -> dict:
    return {"message": "Вы вошли как администратоR"}
@app.get("/user/{id}")
async def main(id: int) -> dict:
    return {"message": f"Ваш №: {id}"}

@app.get("/user")
async def main(username: str, age: int) -> dict:
    return {"message": f"Драсьте, {username}; Ваш возраст {age}"}



