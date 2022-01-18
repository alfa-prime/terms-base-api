from models.categories import Category
from models.terms import Term

CATEGORIES_LIST = ['Python', 'Data Science']

TERMS_LIST = [
    {"name_eng": "list", "name_rus": "список", "category": {"id": 1, "name": "python"}},
    {"name_eng": "dict", "name_rus": "словарь", "category": {"id": 1, "name": "python"}},
    {"name_eng": "dict", "name_rus": "словарь", "category": {"id": 2, "name": "data science"}},
    {"name_eng": "list", "name_rus": "список", "category": {"id": 2, "name": "data science"}},
]


async def populate_db():
    """ Populate db by test data """
    categories = await Category.objects.all()
    if not categories:
        for category_name in CATEGORIES_LIST:
            await Category.objects.create(name=category_name.lower())
        for term in TERMS_LIST:
            await Term.objects.create(**term)
