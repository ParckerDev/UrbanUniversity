from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

templates = Jinja2Templates('templates/')
users = []
app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id):
    user = list(filter(lambda user: user.id == user_id, users))[0]
    return templates.TemplateResponse('users.html', {'request': request, 'user': user})

@app.post('/user/{username}/{age}')
async def add_user(user: User):
    user.id = 1 if not users else users[-1].id + 1
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='34')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    try:
        updated_user = list(filter(lambda user: user.id == user_id, users))[0]
        updated_user.username = username
        updated_user.age = age
        return f'The user {user_id} is update'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='34')]):
    try:
        deleted_user = list(filter(lambda user: user.id == user_id, users))[0]
        users.remove(deleted_user)
        return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')



if __name__ == "__main__":
    uvicorn.run("module_16_5:app", reload=True)