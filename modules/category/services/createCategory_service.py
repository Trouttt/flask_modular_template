from ..repositories.saveCategory_repository import *

class CreateCategoryService:
    def __init__(self, name) -> None:
        self.name = name

    async def execute(name):
        try:
            createdCategory = await saveCategoryRepository.execute(name)

            return createdCategory
           
        except ValueError as e:
            print(e)