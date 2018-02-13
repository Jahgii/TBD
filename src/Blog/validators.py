from django.core.exceptions import ValidationError


def validate_author_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("¡No es un mail valido!")

def validate_algo(value):
    if "algo" in value:
        return value
    else:
        raise ValidationError("Este es el segundo error")
