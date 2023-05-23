""" Файл содержит выполнение код для выполнения задачи """
from random import randint


class TravelAgency:
    """
    Класс представляющий туристическое агенство
    """

    __count_tips = 0
    __map_places = ["Istanbul", "Ankara", "Sochi", "Gelendzhik", "Denpasar", "Paris"]
    __degrees_of_comfort = [1, 2, 3, 4, 5]

    def set_tips_count(self, count: int) -> None:
        """Устанавливает количество мест, которые предложит тур агенство"""

        self.__count_tips = count

    def get_tip(self) -> list:
        """Выдает одну случайную подсказку куда поехать"""

        place = self.__map_places[randint(0, len(self.__map_places) - 1)]
        degree_of_comfort = self.__degrees_of_comfort[
            randint(0, len(self.__degrees_of_comfort) - 1)
        ]

        return [place, degree_of_comfort]

    def get_tips(self) -> list:
        """Выдает столько сколько установленно ранее в конструкторе или методу подсказок куда поехать"""

        all_tips = []
        for n in range(self.__count_tips):
            all_tips.append(self.get_tip())

        return all_tips


class Tourist:
    """
    Класс представляющий туриста
    """

    __tips = []

    def set_tips(self, tips: list):
        """Устанавливает какие подсказки надо проверить туристу"""

        self.__tips = tips

    def get_choice(self) -> list:
        """Производит опредление лучшего по комфорту варианта для отдыха"""

        best_tip = self.__tips[0]
        for tip in self.__tips:
            if best_tip[1] < tip[1]:
                best_tip = tip

        return best_tip


def main():
    travel_agency = TravelAgency()
    tourist = Tourist()

    travel_agency.set_tips_count(10)
    travel_agency_tips = travel_agency.get_tips()

    tourist.set_tips(travel_agency_tips)

    print(tourist.get_choice())
    help(Tourist)


if __name__ == "__main__":
    main()
