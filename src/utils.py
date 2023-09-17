class WorkToUser:
    """Взаимодействие с пользователем"""

    def __init__(self):
        self.site = None
        self.request = None
        self.quantity = None

    def __str__(self):
        return f"Ваш запрос:" \
               f"\nСайт - {self.site}" \
               f"\nЗапрос - {self.request}" \
               f"\nКоличество вакансий - {self.quantity}"

    def choice_site(self):
        """Выбирает платформу для поиска вакансий"""

        site_list = ['hh.ru', 'superjob.ru']
        while True:
            try:
                choice_user = int(
                    input(f'1 - {site_list[0]}\n2 - {site_list[1]}\nЧто ты хочешь посмотреть?: '))
                if choice_user in [1, 2]:
                    self.site = site_list[choice_user - 1]
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Или 1 или 2!")

    def get_request(self):
        """Получает запрос пользователя"""

        self.request = input("\nНапиши ключевое слово: ")

    def quantity_vacancies(self):
        """Получает количество искомых вакансий от пользователя"""

        if self.site == 'superjob.ru':
            self.quantity = 20
            print(f'Количество вакансий будет - {self.quantity}')
        else:
            while True:
                try:
                    choice_user = int(input("\nДиапазон от 1 до 100\nВведи количество вакансий для вывода в топ: "))
                    if 0 < choice_user < 101:
                        self.quantity = choice_user
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Попробуй еще раз")
