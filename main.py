"""
1. Goal - Цель.
    1.1. Повторяющаяся
    1.2. Дочерние
2. Action - Действие. Выполнение может вызывать влияния и принести результат в какую-то цель
    2.1. Качество/процент выполнения действия
    2.2. Влияния
    2.3. Результат
3. Condition - Кондиция. Общее состояние человека. Может влиять на продуктивность выполняемых действий
4. Influence - Влияние. Временное изменение кондиции человека. Совокупность влияний формирует кондицию
"""

from kivy import platform
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

if __name__ == '__main__':
    try:
        import time
        import traceback
        from common import abs_path_near_exe

        from gui import AchieveTheGoalApp

        AchieveTheGoalApp().run()

    except Exception as e:
        error_text = str(e) + '\n' + traceback.format_exc()
        try:
            path = abs_path_near_exe("startup_error.txt")
            with open(path, 'w') as file:
                file.write(error_text)
            print(f"Startup error saved in file: {path}")
            print(error_text)
        except Exception as e:
            print(f"File write error: {str(e)}")
            print(f"Startup error: {error_text}")
            time.sleep(10)
