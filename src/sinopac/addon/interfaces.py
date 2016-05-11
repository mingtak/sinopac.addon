# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from sinopac.addon import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ISinopacAddonLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IConst(Interface):

    title = schema.TextLine(
        title=_(u"Constellation"),
        required=True,
    )

    const_1 = schema.Int(
        title=_(u"const_1"),
        default=0,
        required=True,
    )

    const_2 = schema.Int(
        title=_(u"const_2"),
        default=0,
        required=True,
    )

    const_3 = schema.Int(
        title=_(u"const_3"),
        default=0,
        required=True,
    )

    const_4 = schema.Int(
        title=_(u"const_4"),
        default=0,
        required=True,
    )

    const_5 = schema.Int(
        title=_(u"const_5"),
        default=0,
        required=True,
    )

    const_6 = schema.Int(
        title=_(u"const_6"),
        default=0,
        required=True,
    )

    const_7 = schema.Int(
        title=_(u"const_7"),
        default=0,
       required=True,
    )

    const_8 = schema.Int(
        title=_(u"const_8"),
        default=0,
        required=True,
    )

    const_9 = schema.Int(
        title=_(u"const_9"),
        default=0,
        required=True,
    )

    const_10 = schema.Int(
        title=_(u"const_10"),
        default=0,
        required=True,
    )

    const_11 = schema.Int(
        title=_(u"const_11"),
        default=0,
        required=True,
    )

    const_12 = schema.Int(
        title=_(u"const_12"),
        default=0,
        required=True,
    )


class IPlayer(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    players = schema.List(
        title=_(u"Players"),
        value_type = schema.TextLine(title=_(u"Players"),),
        required=False,
    )


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
