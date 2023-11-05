
from flask import jsonify, request
from .services.createCategory_service import *


class CategoryController:
    def __init__(self, app) -> None:
        self.app = app

    async def create():
        try:
            request_data = request.get_json()

            name = request_data['name']

            created_category = await CreateCategoryService.execute(name)


            return jsonify({'message': 'Categoria criada com sucesso', 'data': created_category}), 201
            
        except ValueError as e:
            return jsonify({'error': e}), 400