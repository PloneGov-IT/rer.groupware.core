# -*- coding: utf-8 -*-
"""
@author: andrea cecchi
"""
from Products.CMFCore.utils import getToolByName
from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES

def Handlers(context):
    if context.readDataFile('rer.groupware.core_various.txt') is None:
        return
    portal=context.getSite()
    addGroupProperty(portal)
    setVersionedTypes(portal)

def addGroupProperty(portal):
    """
    insert some properties
    """
    group_properties = getToolByName(portal, 'portal_groupdata')
    if not group_properties.hasProperty('roomgroup'):
        group_properties.manage_addProperty('roomgroup','False','boolean')
        
# put your custom types in this list
TYPES_TO_VERSION = ('File',)

def setVersionedTypes(portal):
    portal_repository = getToolByName(portal, 'portal_repository')
    versionable_types = list(portal_repository.getVersionableContentTypes())
    for type_id in TYPES_TO_VERSION:
        if type_id not in versionable_types:
            # use append() to make sure we don't overwrite any
            # content-types which may already be under version control
            versionable_types.append(type_id)
            # Add default versioning policies to the versioned type
            for policy_id in DEFAULT_POLICIES:
                portal_repository.addPolicyForContentType(type_id, policy_id)
    portal_repository.setVersionableContentTypes(versionable_types)