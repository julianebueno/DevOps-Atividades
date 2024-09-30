from src.main import *
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
  result = await read_root()
  assert result == {"message": "Api de controle de itens"}

@pytest.mark.asyncio
async def test_read_items():
  result = await read_items()
  assert result == {"message": "teste read_items"}

@pytest.mark.asyncio
async def test_read_item():
  test_item_id = 1
  result = await read_item(test_item_id)
  assert result == {"message": "teste read_item"}

@pytest.mark.asyncio
async def test_create_item():
  test_item = Item(name="Teste", price=10, is_offer=True)
  result = await create_item(test_item)
  assert result == test_item

@pytest.mark.asyncio
async def test_update_item():
  test_item = Item(name="Teste", price=10, is_offer=True, item_id=1)
  result = await update_item(test_item)
  assert result == test_item

@pytest.mark.asyncio
async def test_delete_item():
  test_item_id = 1
  result = await delete_item(test_item_id)
  assert result == {"message": "Item deletado"}