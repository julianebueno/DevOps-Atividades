""" Testes """

import pytest
# import pytest_asyncio

from src.main import Item
from src.main import read_root, read_items
from src.main import create_item, read_item, update_item, delete_item

@pytest.mark.asyncio
async def test_root():
    """ Teste Raiz """
    result = await read_root()
    assert result == {"message": "Api de controle de itens"}

@pytest.mark.asyncio
async def test_read_items():
    """ Teste GET TODOS OS ITEM """
    result = await read_items()
    assert not result == {"message": "Nenhum item encontrado"}

@pytest.mark.asyncio
async def test_read_item():
    """ Teste GET ITEM POR ID """
    test_item_id = 1
    result = await read_item(test_item_id)
    assert not result == {"message": "Item não encontrado"}

@pytest.mark.asyncio
async def test_create_item():
    """ Teste POST ITEM """
    test_item = Item(name="Teste", price=10, is_offer=True)
    result = await create_item(test_item)
    assert result == test_item

@pytest.mark.asyncio
async def test_update_item():
    """ Teste PUT ITEM POR ID """
    test_item_id = 1
    test_item = Item(name="Teste", price=10, is_offer=True)
    result = await update_item(test_item_id, test_item)
    assert result == test_item

@pytest.mark.asyncio
async def test_delete_item():
    """ Teste DELETE ITEM POR ID """
    test_item_id = 1
    result = await delete_item(test_item_id)
    assert result == {"message": "Item deletado"}
    