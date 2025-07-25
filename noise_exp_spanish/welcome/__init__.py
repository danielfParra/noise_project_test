from otree.api import *
import random
import math


class Constants(BaseConstants):
    name_in_url = 'welcome'
    players_per_group = None
    num_rounds = 1
    SHOW_UP_FEE = 12000
    POINTS_TO_CURRENCY = 320.00


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    computer_number = models.IntegerField(
        label='Introduce el número del computador en el que estás sentado '
              '(es el mismo número que te dimos en la llave para guardar tu celular)',
        min=1,
        max=60,
    )

class ComputerPage(Page):
    form_model = 'player'
    form_fields = ['computer_number']

    def before_next_page(player: Player, timeout_happened):
        # Sobrescribimos participant.label con el número de PC
        player.participant.label = str(player.computer_number)

    def is_displayed(player: Player):

        return player.round_number == 1

class Welcome(Page):

    def is_displayed(player: Player):

        return player.round_number == 1



page_sequence = [ComputerPage, Welcome]
