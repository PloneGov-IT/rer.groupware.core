# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory
from logging import getLogger

groupwarecoreMessageFactory = MessageFactory('rer.groupware.core')
logger = getLogger('rer.groupware.core')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
