# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

class View(BrowserView):
    '''
    A view that return a dict of contents created by an user, splitted by Room
    '''
    def __call__(self):
        '''
        '''
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        room=None
        for elem in self.context.aq_chain:
            if getattr(elem,'portal_type','') == 'GroupRoom':
                room = elem
        if not room:
            return portal_catalog.uniqueValuesFor('Subject')
        room_elements=portal_catalog(path='/'.join(room.getPhysicalPath()),
                                     portal_type=self.context.portal_type)
        subjects=set()
        for brain in room_elements:
            subjects.update(brain.Subject)
        return tuple(subjects)
