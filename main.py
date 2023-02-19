import os
import pywebio
import threading
from pywebio.output import *
import pywebio.input as inp

from modules.menu import TaskHandler
from modules.parser import check_coins_balance


@pywebio.config(theme="dark")
async def main():
    clear()
    threading.Thread(target=check_coins_balance()).start()
    task = TaskHandler()
    logo_path = os.path.join("data", "logo.jpg")
    put_image(open(logo_path, "rb").read())
    method = await inp.select(
        "Выберите нужный вариант",
        [
            "Добавить задание",
            "Список заданий"
        ]
    )
    if "Добавить задание" == method:
        await task.add_task_in_list()
    elif "Список заданий" == method:
        task.get_task_list()


if __name__ == "__main__":
    pywebio.start_server(main, host='127.0.0.1', port=4444)
