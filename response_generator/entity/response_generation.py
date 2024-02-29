from enum import Enum

class ResponseGeneration(Enum):
    ACCOUNT_REGISTER = 1
    ACCOUNT_LOGIN = 2



    BATTLE_WAIT_QUEUE_FOR_MATCH = 11
    BATTLE_READY = 12
    CANCEL_MATCH = 13
    CHECK_BATTLE_PREPARE = 14
    WHAT_IS_THE_ROOM_NUMBER = 15
    BATTLE_DECK_LIST = 16
    BATTLE_START_SHUFFLED_GAME_DECK_CARD_LIST = 17
    CHANGE_FIRST_HAND = 18

    ACCOUNT_CARD_LIST = 31
    ACCOUNT_DECK_REGISTER = 41

    SHOP_DATA = 71
    SHOP_GACHA = 72
    FREE_GACHA = 73
    EVENT_DISTRIBUTE_CARDS = 90

    ATTACH_FIELD_ENERGY_TO_UNIT = 1003
    DEPLOY_UNIT_USAGE = 1004
    DRAW_CARD = 1013

    GAME_NEXT_TURN = 3333

    GAME_SURRENDER = 4443

    PROGRAM_EXIT = 4444

    FAKE_BATTLE_ROOM_CREATION = 8001

