from otree.api import *

doc = """PaymentInfo"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

class PaymentInfo(Page):

    def vars_for_template(self):
        payoff = self.participant.payoff
        payoff_plus_participation_fee = self.participant.payoff_plus_participation_fee()
        return dict(
            payoff=Currency(payoff),
            payoff_plus_participation_fee=int(payoff_plus_participation_fee),
        )


#
# class Redirect(Page):
#     pass


page_sequence = [PaymentInfo]