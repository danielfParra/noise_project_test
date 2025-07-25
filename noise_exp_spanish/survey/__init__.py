from otree.api import *
import random

def miso_field(label):
    return models.IntegerField(
        choices=list(range(1, 11)),
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    # Opciones 0…10 para la escala de misofonía
    MISO_CHOICES = [[i, str(i)] for i in range(0, 11)]


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Demographics
    age = models.IntegerField(label='Edad', min=13, max=100)

    gender = models.IntegerField(
        label='Género',
        choices=[[0, 'Masculino'], [1, 'Femenino'], [2, 'Prefiero no decir'], [3, 'Otro']]
    )
    gender_add = models.StringField(blank=True, label='')
    education = models.IntegerField(
        choices=[[0, 'Menos que secundaria'],
                 [1, 'Secundaria'],
                 [2, 'Algo de universidad'],
                 [3, 'Título de asociado'],
                 [4, 'Título universitario'],
                 [5, 'Título avanzado o profesional']
                 ],
        label='¿Cuál es tu nivel más alto de educación?'
    )
    student = models.IntegerField(
        label='¿Estás actualmente inscrito en la universidad?',
        choices=[[0, 'No'], [1, 'Sí']]
    )
    experiments = models.IntegerField(
        label='Por favor, da una estimación aproximada del número de experimentos en los que has participado antes',
        blank=True
    )

    # Pregunta sobre el ambiente
    room_environment_rating = models.LongStringField(
        label='Por favor describe qué tan agradable fue el ambiente en la sala:',
        blank=True
    )

    # Sugerencias para mejorar el ambiente
    room_environment_suggestion = models.LongStringField(
        label='Por favor describe cómo crees que podría mejorarse el ambiente en la sala:',
        blank=True
    )

    mood_image = models.StringField(
        choices=[
            ['happy', 'Feliz'],
            ['satisfied', 'Satisfecho'],
            ['neutral', 'Neutral'],
            ['unsatisfied', 'Insatisfecho'],
            ['sad', 'Triste']
        ],
        label='¿Cuál imagen describe mejor tu estado de ánimo durante el experimento?',
        widget=widgets.RadioSelect
    )

    followup_interest = models.IntegerField(
        label='¿Qué tanto te gustaría participar en un experimento posterior similar al que realizaste hoy?',
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    # Misophonia Scale (0 to 10 sliders)

    miso_q1 = miso_field("1. No me reúno con amigos tan seguido como me gustaría por los ruidos que hacen.")
    miso_q2 = miso_field(
        "2. Si no puedo alejarme de ciertos ruidos, temo que podría entrar en pánico o sentir que voy a explotar.")
    miso_q3 = miso_field("3. Si no puedo evitar ciertos sonidos, me siento impotente.")
    miso_q4 = miso_field("4. Si las personas hacen ciertos sonidos que no soporto, me vuelvo verbalmente agresivo/a.")
    miso_q5 = miso_field("5. Me respeto menos por mis respuestas a ciertos sonidos.")
    miso_q6 = miso_field(
        "6. Las personas deberían hacer todo lo posible para evitar hacer ruidos que puedan molestar a otros.")
    miso_q7 = miso_field("7. Me siento ansioso/a si no puedo evitar escuchar ciertos sonidos.")
    miso_q8 = miso_field(
        "8. La forma en que reacciono a ciertos ruidos me hace sentir que debo ser una persona poco agradable en el fondo.")
    miso_q9 = miso_field(
        "9. La forma en que siento/reacciono a ciertos sonidos eventualmente me aislará y me impedirá hacer cosas cotidianas.")
    miso_q10 = miso_field("10. Puedo experimentar angustia como resultado de algunos ruidos.")
    miso_q11 = miso_field("11. Me siento atrapado/a si no puedo alejarme de ciertos ruidos.")
    miso_q12 = miso_field(
        "12. Siento que debo ser una persona muy enojada por dentro debido a cómo reacciono a ciertos sonidos.")
    miso_q13 = miso_field(
        "13. Las personas no deberían hacer ciertos sonidos, incluso si no saben sobre las sensibilidades de otros.")
    miso_q14 = miso_field(
        "14. Hay lugares a los que me gustaría ir, pero no lo hago porque me preocupa demasiado cómo me afectarán los ruidos.")
    miso_q15 = miso_field(
        "15. Puedo imaginar un futuro donde no pueda hacer cosas cotidianas por mis reacciones a los ruidos.")
    miso_q16 = miso_field(
        "16. Reacciono fuertemente a ciertos sonidos porque no soporto lo egoístas, desconsideradas o maleducadas que pueden ser las personas.")
    miso_q17 = miso_field(
        "17. Puedo enojarme tanto por ciertos ruidos que me vuelvo físicamente agresivo/a con las personas para que se detengan.")
    miso_q18 = miso_field(
        "18. La forma en que reacciono a ciertos sonidos me hace preguntarme si en el fondo soy una mala persona.")
    miso_q19 = miso_field("19. No me gusto a mí mismo/a en los momentos en que reacciono a los sonidos.")
    miso_q20 = miso_field("20. Mis oportunidades laborales están limitadas por mi reacción a ciertos ruidos.")
    miso_q21 = miso_field(
        "21. Ciertos sonidos son simplemente mala educación, y no es extraño sentir una intensa ira por ello.")
    miso_q22 = miso_field(
        "22. A veces me angustio tanto por los ruidos que uso la violencia para intentar que se detengan.")
    miso_q23 = miso_field("23. Algunos sonidos son tan insoportables que grito a las personas para que se detengan.")
    miso_q24 = miso_field(
        "24. Me da miedo hacer algo agresivo o violento porque no soporto el ruido que alguien está haciendo.")
    miso_q25 = miso_field("25. Me enojo con otras personas por lo irrespetuosas que son con los ruidos que hacen.")

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'student', 'experiments',
                   'mood_image', 'room_environment_rating', 'room_environment_suggestion',
                   'followup_interest'
                   ]

    def vars_for_template(player):
        mood_choices = [
            ('happy', 'Feliz'),
            ('satisfied', 'Satisfecho'),
            ('neutral', 'Neutral'),
            ('unsatisfied', 'Insatisfecho'),
            ('sad', 'Triste'),
        ]
        return dict(mood_choices=mood_choices)

class Misophonia(Page):
    form_model = 'player'
    form_fields = [ 'miso_q1', 'miso_q2', 'miso_q3', 'miso_q4', 'miso_q5',
                    'miso_q6', 'miso_q7', 'miso_q8', 'miso_q9', 'miso_q10',
                    'miso_q11', 'miso_q12', 'miso_q13', 'miso_q14', 'miso_q15',
                    'miso_q16', 'miso_q17', 'miso_q18', 'miso_q19', 'miso_q20',
                    'miso_q21', 'miso_q22', 'miso_q23', 'miso_q24', 'miso_q25']

    def vars_for_template(player):
        items = [
            "1. No me reúno con amigos tan seguido como me gustaría por los ruidos que hacen.",
            "2. Si no puedo alejarme de ciertos ruidos, temo que podría entrar en pánico o sentir que voy a explotar.",
            "3. Si no puedo evitar ciertos sonidos, me siento impotente.",
            "4. Si las personas hacen ciertos sonidos que no soporto, me vuelvo verbalmente agresivo/a.",
            "5. Me respeto menos por mis respuestas a ciertos sonidos.",
            "6. Las personas deberían hacer todo lo posible para evitar hacer ruidos que puedan molestar a otros.",
            "7. Me siento ansioso/a si no puedo evitar escuchar ciertos sonidos.",
            "8. La forma en que reacciono a ciertos ruidos me hace sentir que debo ser una persona poco agradable en el fondo.",
            "9. La forma en que siento/reacciono a ciertos sonidos eventualmente me aislará y me impedirá hacer cosas cotidianas.",
            "10. Puedo experimentar angustia como resultado de algunos ruidos.",
            "11. Me siento atrapado/a si no puedo alejarme de ciertos ruidos.",
            "12. Siento que debo ser una persona muy enojada por dentro debido a cómo reacciono a ciertos sonidos.",
            "13. Las personas no deberían hacer ciertos sonidos, incluso si no saben sobre las sensibilidades de otros.",
            "14. Hay lugares a los que me gustaría ir, pero no lo hago porque me preocupa demasiado cómo me afectarán los ruidos.",
            "15. Puedo imaginar un futuro donde no pueda hacer cosas cotidianas por mis reacciones a los ruidos.",
            "16. Reacciono fuertemente a ciertos sonidos porque no soporto lo egoístas, desconsideradas o maleducadas que pueden ser las personas.",
            "17. Puedo enojarme tanto por ciertos ruidos que me vuelvo físicamente agresivo/a con las personas para que se detengan.",
            "18. La forma en que reacciono a ciertos sonidos me hace preguntarme si en el fondo soy una mala persona.",
            "19. No me gusto a mí mismo/a en los momentos en que reacciono a los sonidos.",
            "20. Mis oportunidades laborales están limitadas por mi reacción a ciertos ruidos.",
            "21. Ciertos sonidos son simplemente mala educación, y no es extraño sentir una intensa ira por ello.",
            "22. A veces me angustio tanto por los ruidos que uso la violencia para intentar que se detengan.",
            "23. Algunos sonidos son tan insoportables que grito a las personas para que se detengan.",
            "24. Me da miedo hacer algo agresivo o violento porque no soporto el ruido que alguien está haciendo.",
            "25. Me enojo con otras personas por lo irrespetuosas que son con los ruidos que hacen.",
        ]
        return dict(items=zip(range(1, 26), items))


page_sequence = [Demographics,
                 Misophonia]