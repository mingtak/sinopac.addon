# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api
import random
from DateTime import DateTime
import transaction


class Computing(BrowserView):
    """ Compugint view
    """

    index = ViewPageTemplateFile('template/computing.pt')

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

        scope = 0
        for q in qStr.split():
            if q.split(':')[1] == 'R':
                scope += 100

        if const == 'const_1':
            result.const_1 += scope
        elif const == 'const_2':
            result.const_2 += scope
        elif const == 'const_3':
            result.const_3 += scope
        elif const == 'const_4':
            result.const_4 += scope
        elif const == 'const_5':
            result.const_5 += scope
        elif const == 'const_6':
            result.const_6 += scope
        elif const == 'const_7':
            result.const_7 += scope
        elif const == 'const_8':
            result.const_8 += scope
        elif const == 'const_9':
            result.const_9 += scope
        elif const == 'const_10':
            result.const_10 += scope
        elif const == 'const_11':
            result.const_11 += scope
        elif const == 'const_12':
            result.const_12 += scope

        if catalog(players=email):
            """ 顯示已參加過 """
            response.redirect('/')
            return self.index()
        else:
            """ 寫入，再顯示感謝您參加本遊戲 """
            response.redirect('/@@result')
            return self.index()
        """ 1,計算應得分數(1個R 100分)，
2,透過cookie找到星座
3.把分數寫到星座(在qStr)
4.透過cookie得到 姓名 email
5.catalog email看有沒有玩過
6.有完過回應有參加過了，回首頁
7.沒玩過，把 姓名 email 寫到 portal['resource']['players'], 跳到星座榮譽榜
"""



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

