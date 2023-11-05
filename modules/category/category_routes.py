from .category_controller import *
from flask import Blueprint, jsonify

category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods=['POST'])
async def createCategoryRoute():
    pass

    return await CategoryController.create()

    

 