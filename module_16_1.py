from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def admin():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user(user_id):
    return {'message': f'Вы вошли как пользователь № {user_id}'}




if __name__ == "__main__":
    uvicorn.run("tmp:app", reload=True)