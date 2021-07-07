import json

from core.configuration.configuration_object import ConfigurationObject


class Parser:

    @staticmethod
    def parse(file):
        config_data = json.load(file)
        return config_data


class Serializer:

    @staticmethod
    def serialize(config_data: dict) -> ConfigurationObject:
        audio = config_data.get('audio')[0]
        icon = config_data.get('icon')[0]
        base = config_data.get('base')[0]
        return ConfigurationObject(icon, audio, base)
