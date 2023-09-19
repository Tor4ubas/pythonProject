from utils import WorkToUser
from work_file import ReadWriteToJSON

def get_user(player: WorkToUser, count: int):
    """Выполняет запрос пользователя"""

    player.choice_site()  # выбор ресурса
    player.get_request()  # запрос
    player.quantity_vacancies()  # Количество вакансий

    print(f'\n{player}')  # Показывает запрос

    player.work_api(count)