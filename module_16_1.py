from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/')
async def get_main_page():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def get_admin_page():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def get_user_id(user_id):
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def get_user_info(username: str = 'Ilya', age: int = 26):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}




if __name__ == "__main__":
    uvicorn.run("module_16_1:app", reload=True)