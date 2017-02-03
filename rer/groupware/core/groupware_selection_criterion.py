from Products.CMFCore.utils import getToolByName
from rer.groupware.core import groupwarecoreMessageFactory as _



def getCurrentValues(context, row):
    options = getFilteredSubjects(context)

    options = [(o.lower(),o) for o in options if isinstance(o, basestring)]
    options.sort()

    res = [o[1] for o in options]
    return {row.index: {'query': res, }}


def getFilteredSubjects(context):
    """
    Return a list of keywords for the current room
    """
    catalog = getToolByName(context, 'portal_catalog')
    room = None

    for elem in context.aq_chain:
        if getattr(elem, 'portal_type', '') == 'GroupRoom':
            room = elem
    if not room:
        return catalog.uniqueValuesFor(context.Field())
    room_elements = catalog(path='/'.join(room.getPhysicalPath()))
    subjects = set()
    for brain in room_elements:
        subjects.update(getattr(brain, 'Subject', ()))

    return tuple(subjects)
