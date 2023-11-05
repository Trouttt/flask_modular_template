
from ....database.connection import Category

class saveCategoryRepository:
    def __init__(self, name) -> None:
        self.name = name

    async def execute(name):
        from ....main import session
        try:
            new_category = Category(name=name)
            session.add(new_category)
            session.commit()
            category_data = {
                'id': new_category.id,
                'name': new_category.name,
            # Adicione outros campos da categoria conforme necessário
            }
            return category_data
        except ValueError as e:
            print(e, 'ERRO ERRO ERRO')