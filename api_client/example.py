from .client import NewsAPIClient
import json


def main():
    
    client = NewsAPIClient("http://127.0.0.1:8000")

    print("=== РЕГИСТРАЦИЯ ===")
    result = client.register("testuser", "test@example.com", "testpass123")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    print("\n=== ЛОГИН ===")
    result = client.login("testuser", "testpass123")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    print("\n=== СПИСОК ПОЛЬЗОВАТЕЛЕЙ ===")
    result = client.get_users()
    print(json.dumps(result, indent=2, ensure_ascii=False))

    print("\n=== СОЗДАНИЕ НОВОСТИ ===")
    result = client.create_news(
        title="Тестовая новость",
        content="Это очень длинный текст новости, который должен содержать минимум 50 символов для прохождения валидации.",
        summary="Краткое описание новости"
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if 'id' in result:
        news_id = result['id']
        print(f"\n=== ПОЛУЧЕНИЕ НОВОСТИ #{news_id} ===")
        result = client.get_news(news_id)
        print(json.dumps(result, indent=2, ensure_ascii=False))

        print(f"\n=== ОБНОВЛЕНИЕ НОВОСТИ #{news_id} ===")
        result = client.update_news(
            news_id,
            title="Обновлённый заголовок",
            summary="Обновлённое краткое описание"
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))

        print(f"\n=== УДАЛЕНИЕ НОВОСТИ #{news_id} ===")
        status = client.delete_news(news_id)
        print(f"Статус удаления: {status}")


if __name__ == "__main__":
    main()