import pytest
from lesson_08.pages.auth_api import AuthApi
from lesson_08.config import COMPANY_ID

# удаляет накопившиеся апи-ключи
def test_cleanup_tokens():
    auth_api = AuthApi()
    # 1. получить список всех ключей
    keys_resp = auth_api.get_api_keys()
    if keys_resp.status_code != 200:
        pytest.fail(f"Ошибка при получении ключей: {keys_resp.text}")

    keys_data = keys_resp.json()
    
    # 2. фильтрация по ID компании
    company_keys = []
    for key_info in keys_data:
        if key_info.get("companyId") == COMPANY_ID:
            company_keys.append(key_info)

    # 3. сколько ключей оставить
    KEYS_TO_KEEP = 2

    if len(company_keys) <= KEYS_TO_KEEP:
        return

    # 4. определить какие ключи удалять
    keys_to_delete = company_keys[:-KEYS_TO_KEEP]  # все кроме последних KEYS_TO_KEEP
    
    # 6. удалить старые ключи
    deleted_count = 0
    failed_count = 0
    
    for key_info in keys_to_delete:
        key_value = key_info.get("key", "")
        try:
            delete_resp = auth_api.delete_api_key(key_value)
            if delete_resp.status_code == 200:
                deleted_count += 1
            else:
                failed_count += 1
        except Exception as e:
            failed_count += 1
    
    # проверка что удаление успешно
    assert failed_count == 0, f"Не удалось удалить {failed_count} ключей"
    
    # проверка, что осталось нужное количество ключей
    # получаем обновленный список
    updated_keys_resp = auth_api.get_api_keys()
    if updated_keys_resp.status_code == 200:
        updated_keys = updated_keys_resp.json()
        updated_company_keys = [k for k in updated_keys if k.get("companyId") == COMPANY_ID]
        
        # проверяем, что количество ключей уменьшилось
        assert len(updated_company_keys) <= len(company_keys) - deleted_count, \
            f"Ключей осталось больше, чем ожидалось: {len(updated_company_keys)}"


if __name__ == "__main__":
    test_cleanup_tokens()
