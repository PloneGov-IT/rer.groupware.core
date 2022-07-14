# -*- coding: utf-8 -*-

from plone import api
from rer.groupware.core import groupwarecoreMessageFactory as _


def notifyChangeState(obj,event):
    """ """
    wtool = api.portal.get_tool('portal_workflow')
    review_state = wtool.getInfoFor(obj,'review_state')
    if review_state != 'visible':
        return
    sendMail(obj)


def sendMail(obj):
    """ """
    logged_user = api.user.get_current()
    logged_userid = logged_user.getId()
    author_id = obj.Creator()
    #If the creator is the current user, don't send the mail
    if logged_userid == author_id:
        return

    portal = api.portal.get()

    manager_mail = api.portal.get_registry_record('plone.email_from_address')
    if not manager_mail:
        message = _('server_not_set',default=u'Impossible sending the notification. Mailserver not set in the portal.')
        api.portal.show_message(message, obj.REQUEST, type='error')
        return

    author = api.user.get(author_id)
    author_mail = author.getProperty('email','')
    if not author_mail:
        return

    encoding = api.portal.get_registry_record('plone.email_charset')
    mail_template = portal.restrictedTraverse('unlock_mail_notification')
    if not mail_template:
        message = _('mailtemplate_not_set',default=u'Impossible sending the notification. Mail template not set.')
        api.portal.show_message(message, obj.REQUEST, type='error')
        return

    #get the names
    modifier_name = logged_user.getProperty('fullname','')
    if not modifier_name:
        modifier_name = logged_userid

    author_name = author.getProperty('fullname','')
    if not author_name:
        author_name = author_id

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
        host.send(mail_text, immediate=True)
        api.portal.show_message("Email di conferma pubblicazione spedita all'autore", obj.REQUEST, type='info')
    except Exception as err:
        api.portal.show_message('Impossibile spedire il messsaggio: %s' % err, obj.REQUEST, type='error')


def getObjRoom(obj):
    for parent in obj.aq_chain:
        if getattr(parent,'portal_type','') == 'GroupRoom':
            return parent.Title()
    return ''
