from enum import Enum

new_tupl = [1, 2]

some_value = 10

extra_tupl = [new_tupl[0], new_tupl[1]] + [3, 4] + [some_value]

extra_tupl = extra_tupl + [len(extra_tupl)]

print(extra_tupl, len(extra_tupl))

print(extra_tupl[-1])


class LogLevel(Enum):
    INFO = "INFO"
    ERROR = "ERROR"
    WARNING = "WARNING"

    @classmethod
    def all(cls):
        return (
            cls.INFO.value,
            cls.ERROR.value,
            cls.WARNING.value,
        )

    @classmethod
    def get_bracket_value(cls, var_name = None):
        if var_name and var_name in LogLevel.all():
            return '[{}] '.format(getattr(cls, var_name).value)
        return 'Missing'


print(LogLevel.INFO.value)

print(LogLevel.INFO.value in LogLevel.all())

print(LogLevel.get_bracket_value('MISS'))

print(LogLevel.get_bracket_value('INFO'))

print(LogLevel.get_bracket_value({'des':'val'}))

print(LogLevel.get_bracket_value(['something']))

print(LogLevel.get_bracket_value('something'))
print(LogLevel.get_bracket_value(('something')))
print(LogLevel.get_bracket_value(False))
print(LogLevel.get_bracket_value(True))