from fastapi import APIRouter

api = APIRouter()


@api.get('/example1')
async def example_1():
    return {'example': 1}
