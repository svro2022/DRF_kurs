from rest_framework.serializers import ValidationError


class NiceHabitValidator:
    '''Cвязанная привычка, приятная привычка и награда.'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_is_nice = dict(value).get('is_nice_habit')  # приятная привычка
        habit_is_linked = dict(value).get('link_nice_habit')  # связанная привычка
        habit_reward = dict(value).get('reward')  # награда

        if habit_is_nice and habit_reward is not None:
            raise ValidationError('У приятной привычки нет награды!')

        if habit_is_nice and habit_is_linked is not None:
            raise ValidationError('Нельзя выбрать приятную и связанную привычки одновременно!')


class IsNiceHabitValidator:
    '''Связанная привычка - привычка с признаком приятной привычки.'''

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        nice_habit = dict(value).get(self.fields)
        if nice_habit:
            if not nice_habit.is_nice_habit:
                raise ValidationError('Связанная привычка может быть только с признаком приятной привычки!')


class TimeHabitValidator:
    '''Время выполнения привычки не должно быть больше 120 секунд'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        complete_time = dict(value).get(self.field)
        seconds = complete_time.hour * 3600 + complete_time.minute * 60 + complete_time.second
        if seconds > 120:
            raise ValidationError('Время выполнения не должно превышать 120 сек!')


class PeriodicityHabitValidator:
    '''Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
