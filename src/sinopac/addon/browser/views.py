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
        catalog = context.portal_catalog

        if not (request.get('HTTP_REFERER', '').endswith('questions-start') != request.get('HTTP_REFERER', '').endswith('questions')):
            response.redirect('/')
            return

        self.questions = []
        for keyword in ['A', 'B', 'C', 'D', 'E']:
            self.questions.append(random.choice(catalog({'Type':'Question', 'Subject':keyword})))

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
