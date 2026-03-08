#!/usr/bin/python3
"""Klass instansiyasını lüğətə çevirən modul."""


def class_to_json(obj):
    """Obyektin bütün atributlarını lüğət şəklində qaytarır."""
    return obj.__dict__
