# -*- coding: utf-8 -*-
"""
@author: andrea cecchi
"""
from Products.CMFCore.utils import getToolByName

def Handlers(context):
    if context.readDataFile('rer.groupware.core_various.txt') is None:
        return
    addGroupProperty(context)
    

def addGroupProperty(context):
    """
    insert some properties
    """
    portal=context.getSite()
    group_properties = getToolByName(portal, 'portal_groupdata')
    if not group_properties.hasProperty('roomgroup'):
        group_properties.manage_addProperty('roomgroup','False','boolean')
        import pdb;pdb.set_trace()
        

