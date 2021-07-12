from core.exceptions.validation_exceptions import *


class Validator:

    @staticmethod
    def validate(data, config_object):
        Validator._validate_title(data['title'])
        Validator._validate_description(data['description'])
        Validator._validate_icon(data['icon'], config_object)
        Validator._validate_time(data['time'])


    @staticmethod
    def _validate_title(title) -> bool:
        if len(title) == 0:
            raise TitleValidationException('small')
        elif len(title) > 30:
            raise TitleValidationException('long')
        return True

    @staticmethod
    def _validate_description(desc) -> bool:
        if len(desc) == 0:
            raise DescriptionValidationException('small')
        elif len(desc) > 50:
            raise DescriptionValidationException('long')
        return True

    @staticmethod
    def _validate_icon(icon, config_object) -> bool:
        if icon == config_object.base_icon:
            raise IconValidationException()
        return True

    @staticmethod
    def _validate_time(time) -> bool:
        if time == 0:
            raise TimeValidationException()
        return True



