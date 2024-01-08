from os import listdir as os_list_dir
from pygame import image, transform


def loading_sprites(storage: dict) -> dict:
    """ Загрузка спрайтов для объекта """
    sprites = {}
    # Путь к директориям с изображениями;
    path = storage["path"]
    # Получаем объекты изображений;
    for name, size in storage["sprites"].items():
        sprites[name] = [transform.scale(
            image.load(f"{path}/{name}/{img+1}.png"), (size)
        ) for img in range(len(os_list_dir(path=f"{path}/{name}")))]
    sprites["size"] = storage["sprites"]
    return sprites
