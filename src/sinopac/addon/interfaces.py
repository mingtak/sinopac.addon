# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from sinopac.addon import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ISinopacAddonLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IQuestion(Interface):

    title = schema.TextLine(
        title=_(u"Title (Question) "),
        required=True,
    )

    answer_1 = schema.TextLine(
        title=_(u"Answer"),
        required=True,
    )

    answer_2 = schema.TextLine(
        title=_(u"Answer"),
        required=True,
    )

    answer_3 = schema.TextLine(
        title=_(u"Answer"),
        required=True,
    )

    answer_4 = schema.TextLine(
        title=_(u"Answer"),
        required=True,
    )

    rightAns = schema.Int(
        title=_(u"Right Answer"),
        required=True,
        min=1,
        max=4,
    )
