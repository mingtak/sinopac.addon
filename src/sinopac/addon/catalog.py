# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
#from zope.interface import Interface
#from Products.CMFPlone.utils import safe_unicode
from sinopac.addon.interfaces import IPlayer


@indexer(IPlayer)
def players_indexer(obj):
    emailList = []
    for player in obj.players:
        emailList.append(player.split()[1])
    return emailList
