from archetypes.schemaextender.interfaces import ISchemaModifier
from bika.lims import bikaMessageFactory as _
from bika.lims.interfaces import IAnalysisRequest
from zope.component import adapts
from zope.interface import implements


class AnalysisRequestSchemaModifier(object):
    adapts(IAnalysisRequest)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        """
        """
        schema['SamplingDeviation'].required = True
        schema['ClientReference'].widget.label = _('Seal Number')
        schema['ResultsInterpretation'].widget.label = _('Comment')
        return schema
