from rest_framework.serializers import ValidationError


class LinkValidator:
    def __init__(self,field):
        self.field = field

    def __call__(self,value):
        temp_value = dict(value).get(self.field)
        if not temp_value.startswith('https://www.youtube.com'):
            raise ValidationError(f'{self.field} ссылки только с ютуб')
        return value
