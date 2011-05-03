from Products.ATContentTypes.criteria import LIST_INDICES, registerCriterion
from Products.ATContentTypes.criteria.selection import \
    ATSelectionCriterionSchema, ATSelectionCriterion
from Products.ATContentTypes.interfaces import IATTopicSearchCriterion
from Products.Archetypes.atapi import DisplayList
from Products.CMFCore.utils import getToolByName
from rer.groupware.core.interfaces import IATGroupwareSelectionCriteria
from zope.interface import implements
from rer.groupware.core import groupwarecoreMessageFactory as _

CompareOperators = DisplayList((
                    ('and', _(u'and'))
                  , ('or', _(u'or'))
    ))


class ATGroupwareSelectionCriterion(ATSelectionCriterion):
    """A selection criterion"""
    
    implements(IATGroupwareSelectionCriteria)
    __implements__ = ATSelectionCriterion.__implements__ + (IATTopicSearchCriterion, )
    schema         = ATSelectionCriterionSchema
    meta_type      = 'ATGroupwareSelectionCriterion'
    archetype_name = 'Groupware Selection Criterion'
    shortDesc      = 'Select values from list filtered by room'

    def getCurrentValues(self):
        
        options = self.getFilteredSubjects()
        # AT is currently broken, and does not accept ints as
        # DisplayList keys though it is supposed to (it should
        # probably accept Booleans as well) so we only accept strings
        # for now
        options = [(o.lower(),o) for o in options if isinstance(o, basestring)]
        options.sort()
        return [o[1] for o in options]

    def getFilteredSubjects(self):
        """
        Return a list of keywords for the current room
        """
        catalog = getToolByName(self, 'portal_catalog')
        room=None
        for elem in self.aq_chain:
            if getattr(elem,'portal_type','') == 'GroupRoom':
                room = elem
        if not room:
            return catalog.uniqueValuesFor(self.Field())
        room_elements=catalog(path='/'.join(room.getPhysicalPath()))
        subjects=set()
        for brain in room_elements:
            subjects.update(getattr(brain,self.Field(),()))
        return tuple(subjects)
        
registerCriterion(ATGroupwareSelectionCriterion, LIST_INDICES)
