from utils import WorkToUser
from work_file import ReadWriteToJSON


def get_user(player: WorkToUser, count: int):
    """Выполняет запрос пользователя"""

    player.choice_site()  # выбор ресурса
    player.get_request()  # запрос
    player.quantity_vacancies()  # Количество вакансий

    print(f'\n{player}')  # Показывает запрос

    player.work_api(count)


def repeat_get(player: WorkToUser):
    """Повторяет запрос пользователя"""

    while True:
        try:
            choice_user = int(input('\nХочешь повторить запрос?\n1 - Да\n2 - Нет\n'))
            if choice_user == 1:
                get_user(player, 1)
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Ай-яй-яй, внимательней кнопочки нажимать надо!")


def find_get(player: WorkToUser):
    """Ищет дополнительный запрос пользователя"""

    while True:
        try:
            choice_user = int(input('\nХочешь найти ключевое слово в вакансиях?\n1 - Да\n2 - Нет\n'))
            if choice_user == 1:
                data = input('Итак, твой запрос: ')
                print(player.find_word(data))
            elif choice_user == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("Что-то не то нажато))")


def main():
    while input('Нажми Enter, чтобы начать: ') != '':
        continue

    # Очищаем файл
    f = open('vacancies.json', 'w')
    f.close()

    print('\nПривет! Я робот Вертер и я найду тебе кучу вакансий.')

    player = WorkToUser()

    get_user(player, 0)
    repeat_get(player)
    WorkToUser.sort_all()
    find_get(player)

    if not ReadWriteToJSON.read_json():
        print('\nПардон,но по запросу ничего не найдено')
    else:
        print('\nСписок вакансий, отсортированных по зарплате, ты можешь посмотреть в файле - vacancies.json')
    print('\nХорошего дня!')


if __name__ == "__main__":
    main()
