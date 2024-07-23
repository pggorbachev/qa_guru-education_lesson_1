import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from users_data.users import users_data

app = FastAPI()


@app.get("/api/user/{user_id}")
async def get_user(user_id: int):
    user = users_data.get(user_id)
    if user:
        return JSONResponse(content={"data": user, "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }})
    else:
        return JSONResponse(status_code=404, content={"error": "User not found"})


if __name__ == "__main__":
    uvicorn.run(app)
