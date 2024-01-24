# get.py

import os
import requests
import json
from config import SAVE_PATH, FILE_EXPORT_JSON  # Импортируем переменные из config.py

def save_images(item):
    item_id = str(item["id"])
    folder_path = os.path.join(SAVE_PATH, item_id)

    # Создаем папку с именем id, если ее нет
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Сохраняем изображения в папке
    for i in range(1, 11):
        image_key = f"images{i}"
        if image_key in item:
            image_url = item[image_key]
            image_name = f"image_{i}.jpg"
            image_path = os.path.join(folder_path, image_name)

            # Проверяем, существует ли файл
            if not os.path.exists(image_path):
                # Загружаем изображение
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(image_path, "wb") as image_file:
                        image_file.write(response.content)
                        print(f"Изображение {image_name} сохранено по пути: {image_path}")
            else:
                print(f"Изображение {image_name} уже существует по пути: {image_path}")

if __name__ == "__main__":
    try:
        with open(FILE_EXPORT_JSON, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        items = json_data.get("catalog", {}).get("items", [])

        for item in items:
            save_images(item)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
