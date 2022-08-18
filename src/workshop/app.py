from fastapi import FastAPI
from .api import router

tags_metadata = [
    {
        'name': 'Авторизация',
        'description': 'Авторизация и регистрация'
    },
    {
        'name': 'Операции',
        'description': 'Работа с операциями'
    },
    {
        'name': 'Репорты',
        'description': 'Импорт и экспорт отчетов'
    },
]

app = FastAPI(
    title='FastAPI:Feed-market',
    description='Пробую перенести бекэнд на FastAPI',
    version='1.0.0',
    openapi_tags=tags_metadata,
)
app.include_router(router)

