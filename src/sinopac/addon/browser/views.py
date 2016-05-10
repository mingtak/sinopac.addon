# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api
import random
from DateTime import DateTime
import transaction
from zope.lifecycleevent import ObjectModifiedEvent
from zope.event import notify


class Computing(BrowserView):
    """ Computing
    """

    def __call__(self):
        context = self.context
        request = self.request
        response = request.response
        cookies = request.cookies
        catalog = context.portal_catalog

        portal = api.portal.get()
        qStr = cookies.get("qStr")
        result = portal['resource']['result']
        players = portal['resource']['players']
        const = request.get('const')
        name = request.get('name')
        email = request.get('email')

        if not (const and name and email):
            response.redirect('/')
            return

        self.scope = 0
        for q in qStr.split():
            if q.split(':')[1] == 'R':
                self.scope += 100

        if const == 'const_1':
            result.const_1 += self.scope
        elif const == 'const_2':
            result.const_2 += self.scope
        elif const == 'const_3':
            result.const_3 += self.scope
        elif const == 'const_4':
            result.const_4 += self.scope
        elif const == 'const_5':
            result.const_5 += self.scope
        elif const == 'const_6':
            result.const_6 += self.scope
        elif const == 'const_7':
            result.const_7 += self.scope
        elif const == 'const_8':
            result.const_8 += self.scope
        elif const == 'const_9':
            result.const_9 += self.scope
        elif const == 'const_10':
            result.const_10 += self.scope
        elif const == 'const_11':
            result.const_11 += self.scope
        elif const == 'const_12':
            result.const_12 += self.scope

        played = 'F'

        for player in players.players:
            if email == player.split()[1]:
                """ 顯示已參加過 """
                played = 'T'
                break

        if played == 'F':
            with api.env.adopt_roles(['Manager']):
                players.players.append('%s %s' % (name, email))
#                players.reindexObject()
                notify(ObjectModifiedEvent(players))
                transaction.commit()

        response.redirect('/@@result?played=%s&scope=%s' % (played, self.scope))
        return


class Questions(BrowserView):
    """ Questions View
    """

    index = ViewPageTemplateFile('template/questions.pt')

    def __call__(self):
        context = self.context
        request = self.request
        response = request.response
        cookies = request.cookies
        catalog = context.portal_catalog

        if not (request.get('HTTP_REFERER', '').endswith('questions-start') != request.get('HTTP_REFERER', '').endswith('questions')):
            response.redirect('/')
            return

        if request.get('HTTP_REFERER', '').endswith('questions-start'):
            # qStr format: 'UID_1:C UID_2:C ...', C: 'N' for not answer yet, 'R' for Right, and 'W' for Wrong.
            qStr = ''
            for keyword in ['A', 'B', 'C', 'D', 'E']:
                q = random.choice(catalog({'Type':'Question', 'Subject':keyword}))
                qStr += '%s:N ' % q.UID
            response.setCookie('qStr', qStr)
            question = qStr.split()[0] # question format is UID:N
            self.num = 1
        else:
            qStr = cookies.get("qStr")
            question = None
            self.num = 0
            for q in qStr.split():
                self.num += 1
                if q.endswith('N'):
                    question = q
                    break
            if question is None:
                response.redirect('/@@leaving')
                return

        self.qBrain = catalog(UID=question.split(':')[0])
        self.answer = self.qBrain[0].getObject().rightAns
        return self.index()


class CheckAnswer(BrowserView):
    """ Check Answer
    """

    index = ViewPageTemplateFile('template/check_answer.pt')

    def __call__(self):
        context = self.context
        request = self.request
        response = request.response
        cookies = request.cookies
#        catalog = context.portal_catalog

        ans = request.get('ans', 1)
        ra = request.get('ra', 0)
        if ans == ra:
            self.result = True
        else:
            self.result = False

        qStr = cookies.get("qStr")
        self.num = 0
        new_qStr = ''
        writed = False
        for q in qStr.split():
            if q.split(':')[1] == 'N' and not writed:
                new_qStr += '%s:%s ' % (q.split(':')[0], 'R' if self.result else 'W')
                writed = True
            else:
                new_qStr += '%s ' % q

        response.setCookie('qStr', new_qStr)
        return self.index()


class QuestionsConfirm(BrowserView):
    """ Questions-confirm View
    """

class QuestionsCorrect(BrowserView):
    """ Questions-correct View
    """

class QuestionsStart(BrowserView):
    """ Questions-start View
    """

class QuestionsWrong(BrowserView):
    """ Questions-wrong View
    """

class Result(BrowserView):
    """ Result View
    """

    index = ViewPageTemplateFile('template/result.pt')

    def __call__(self):

        portal = api.portal.get()
        self.result = portal['resource']['result']
        return self.index()



class TermsAndAgreements(BrowserView):
    """ Terms-and-agreements View
    """

class SinopacMacro(BrowserView):
    """ Sinopac Macro View
    """

class Index(BrowserView):
    """ Index View
    """

class Leaving(BrowserView):
    """ Leaving View
    """

class Measures(BrowserView):
    """ Measures View
    """

class PlayerView(BrowserView):
    """ PlayerView
    """
