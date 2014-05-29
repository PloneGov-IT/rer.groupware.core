# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
try:
    from zope.app.component.hooks import getSite
except ImportError:
    from zope.component.hooks import getSite
from rer.groupware.core import groupwarecoreMessageFactory as _
from zope.i18n import translate

def notifyChangeState(obj,event):
    wtool = getToolByName(obj, 'portal_workflow')
    review_state = wtool.getInfoFor(obj,'review_state')
    if review_state != 'visible':
        return
    sendMail(obj)

        
def sendMail(obj):
    pm = getToolByName(obj, 'portal_membership')
    logged_user=pm.getAuthenticatedMember()
    logged_userid=logged_user.getId()
    author_id=obj.Creator()
    #If the creator is the current user, don't send the mail
    if logged_userid == author_id:
        return
    putils=getToolByName(obj, "plone_utils")
    portal = obj.portal_url.getPortalObject()
    manager_mail=portal.email_from_address
    if not manager_mail:
        message=_('server_not_set',default=u'Impossible sending the notification. Mailserver not set in the portal.')
        putils.addPortalMessage(message, type='error')
        return
    
    author=pm.getMemberById(author_id)
    author_mail=author.getProperty('email','')
    if not author_mail:
        return
    encoding = portal.getProperty('email_charset')
    
    mail_template=portal.restrictedTraverse('unlock_mail_notification')
    if not mail_template:
        message=_('mailtemplate_not_set',default=u'Impossible sending the notification. Mail template not set.')
        return
    
    #get the names
    modifier_name=logged_user.getProperty('fullname','')
    if not modifier_name:
        modifier_name=logged_userid
    author_name=author.getProperty('fullname','')
    if not author_name:
        author_name=author_id
    mail_text = mail_template(mfrom=manager_mail,
                              mto=author_mail,
                              obj=obj,
                              obj_parent=getObjRoom(obj),
                              modifier_name=modifier_name,
                              author_name=author_name,
                              charset=encoding,
                              request=obj.REQUEST)
    try:
        host = portal.MailHost
        host.send(mail_text.encode(encoding))
        obj.plone_log("Email di conferma pubblicazione spedita all'autore")
        
    except Exception, err:
        obj.plone_log('Impossibile spedire il messsaggio: %s'%err)
            
def getObjRoom(obj):
    for parent in obj.aq_chain:
        if getattr(parent,'portal_type','') == 'GroupRoom':
            return parent.Title()
    return ''
