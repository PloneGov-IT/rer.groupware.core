# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

from plone.app.discussion.interfaces import IComment
from Products.Ploneboard.interfaces import IComment as IPloneboardComment

class RoomActivityView(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        request.set('disable_border', True)

    def _get_users_info(self, users):
        """Given a list of userids, return all informations about users"""
        users_info = []
        acl_users = getToolByName(self.context, 'acl_users')
        pm = getToolByName(self.context, 'portal_membership')
        for userid in users:
            user = acl_users.getUserById(userid)
            if user:
                users_info.append({'userid': userid,
                                   'portrait': pm.getPersonalPortrait(userid),
                                   'email': user.getProperty('email'),
                                   'fullname': user.getProperty('fullname')})
        return users_info

    def room_activity(self):
        context = self.context
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(path='/'.join(context.getPhysicalPath()),
                          object_provides=[IComment.__identifier__,
                                           IPloneboardComment.__identifier__,])
        users = []
        for brain in results:
            users.append(brain.Creator)
        
        active_users = self._get_users_info(tuple(set(users)))
        
        return active_users
