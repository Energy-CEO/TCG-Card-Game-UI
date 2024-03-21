from battle_field_fixed_card.fixed_field_card import FixedFieldCard
from card_info_from_csv.repository.card_info_from_csv_repository_impl import CardInfoFromCsvRepositoryImpl
from common.card_grade import CardGrade
from common.card_type import CardType
from opengl_battle_field_pickable_card.pickable_card import PickableCard


class MyCardPage:

    __card_info_repository = CardInfoFromCsvRepositoryImpl.getInstance()

    page_number = 0

    total_width = 0
    total_height = 0

    # 430 / 1920, 252 / 1043
    # 1490 / 1920, 252 / 1043
    # 6개 구성 (x_right_base_ratio - x_left_base_ratio) / 6
    x_left_base_ratio = 0.024
    x_right_base_ratio = 0.568
    y_bottom_base_ratio = 0.2416
    y_top_base_ratio = 0.593

    def __init__(self):
        self.my_card_page_card_list = []
        self.my_card_page_card_object_list = []

    def set_total_window_size(self, width, height):
        self.total_width = width
        self.total_height = height

    def set_page_number(self, page_number):
        self.page_number = page_number

    def add_my_card_to_page(self, my_card_list):
        if isinstance(my_card_list, list):
            self.my_card_page_card_list.extend(my_card_list)

    def update_my_card_to_page(self, my_card_list):
        if isinstance(my_card_list, list):
            self.my_card_page_card_list = []
            self.my_card_page_card_list.extend(my_card_list)

    def get_my_card_page_card_list(self):
        return self.my_card_page_card_list

    def get_my_card_page_card_object_list(self):
        return self.my_card_page_card_object_list

    def get_next_card_position(self, index):
        print(f"my_card_page -> get_next_card_position() - self.total_width: {self.total_width}")
        # TODO: 배치 간격 고려
        card_width_ratio = 300 / self.total_width
        place_index = index % 4

        current_y = self.total_height * self.y_bottom_base_ratio
        base_x = self.total_width * self.x_left_base_ratio

        x_increment = (self.x_right_base_ratio - self.x_left_base_ratio + card_width_ratio) / 4.0
        next_x = base_x + self.total_width * (x_increment * place_index)
        return (next_x, current_y)

    def create_my_card_list(self):
        my_card_page_card_list = self.get_my_card_page_card_list()
        print(f"my_card_page_card_list: {my_card_page_card_list}")

        for index, card_id in enumerate(my_card_page_card_list):
            print(f"index: {index}, card_number: {card_id}")
            my_card = PickableCard(local_translation=self.get_next_card_position(index))
            # new_card = FixedFieldCard(local_translation=self.get_next_card_position(index))
            print("Success to make PickableCard")
            my_card.init_card_in_my_card_frame(card_id, self.total_width, self.total_height)
            # my_card.init_card(card_id)
            print("Success to create card frame")
            my_card.set_index(index)
            self.my_card_page_card_object_list.append(my_card)