# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class View(BrowserView):
    """
    View class for homepage topic view
    """
        
    def getFileType(self,brain):
        """
        If there is content_type info in the catalog, get the right mimetype name
        If there isn't, get the file extension
        """
        file_obj=brain.getObject()
        field = file_obj.getField('file',None)
        
        if not field:
            return ''
        content_type=field.getContentType(file_obj)
        mimetype_registry = getToolByName(self.context,'mimetypes_registry')
        try:
            name_type = mimetype_registry.lookup(content_type)
            mime_type=name_type[0]
            return mime_type.name()
        except:
            return content_type