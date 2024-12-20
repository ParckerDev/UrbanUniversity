from typing import Annotated
from fastapi import FastAPI, Path
import uvicorn

users = {'1': 'Имя: Example, возраст: 18'}
app = FastAPI()

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    current_id = int(max(users.keys(), key=int)) + 1
    users[current_id] = f'Имя: {username}, возраст: {age}'
    return f'User {current_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='34')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is update'

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='34')]):
    del users[user_id]
    return f'User {user_id} has been deleted'



if __name__ == "__main__":
    uvicorn.run("module_16_3:app", reload=True)