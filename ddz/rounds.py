from typing import NamedTuple
import random

from ddz.models import GroupMember


class Card(NamedTuple):
    """
    单张牌
    """
    rank: str
    suit: str
    owner_index: -1 | 0 | 1 | 2 | 3 = 0  # 0 底牌，1 玩家1，2：玩家2，3：玩家3，-1：已出牌


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks] + [Card("Joker", "big"), Card("Joker", "little")]
        random.shuffle(self._cards)  # 洗牌
        self.odds: int = 1  # 赔率
        self.multiple: int = 1  # 倍数
        self.index: int = 0  # 第几局
        self.hole_cards = self._cards[0:3]  # 底牌
        for card in self._cards[3:20]:
            card.owner_index = 1
        for card in self._cards[20:37]:
            card.owner_index = 2
        for card in self._cards[37:54]:
            card.owner_index = 2
        self.land_owner_index: 1 | 2 | 3 = 1  # 地主成员编号
        self.player_index = 1  # 当前出牌编号


# class Innings(NamedTuple):
#     """
#     每一轮比赛的详细信息
#     """
#     land_owner_index: 0 | 1 | 2 = None  # 地主的成员编号
#     odds: 1 | 2 | 3 = 1  # 赔率
#     multiple: int = 1  # 倍数
#     index: int = 0  # 第几局
#
#
class Rounds(NamedTuple):
    """
    一共几局，当前第几局
    """
    No_0: GroupMember  # 成员1
    No_1: GroupMember  # 成员2
    No_2: GroupMember  # 成员3
    french_deck: FrenchDeck  # 当前局的详细信息
    num: int = 8  # 一轮一共多少局
