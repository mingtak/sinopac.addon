# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinopac.addon


class SinopacAddonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=sinopac.addon)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinopac.addon:default')


SINOPAC_ADDON_FIXTURE = SinopacAddonLayer()


SINOPAC_ADDON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINOPAC_ADDON_FIXTURE,),
    name='SinopacAddonLayer:IntegrationTesting'
)


SINOPAC_ADDON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINOPAC_ADDON_FIXTURE,),
    name='SinopacAddonLayer:FunctionalTesting'
)


SINOPAC_ADDON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINOPAC_ADDON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SinopacAddonLayer:AcceptanceTesting'
)
