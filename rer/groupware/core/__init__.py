# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
from rer.groupware.core import config
from Products.Archetypes import atapi
from Products.CMFCore import utils

groupwarecoreMessageFactory = MessageFactory('rer.groupware.core')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    import groupware_selection_criterion
    
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)