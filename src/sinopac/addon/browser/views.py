from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api
import random
from DateTime import DateTime
import transaction


class Index(BrowserView):
    """ Index View
    """

class Leaving(BrowserView):
    """ Leaving View
    """

class Measures(BrowserView):
    """ Measures View
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

            if question is None:
                response.redirect('/@@leaving')
                return

        self.qBrain = catalog(UID=question.split(':')[0])
        return self.index()


#self.request.response.setCookie('itemInCart', itemInCart)
#self.request.cookies.get("cookie_name", "default_value_if_cookie_not_set")

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
