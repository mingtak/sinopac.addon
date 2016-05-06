# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from sinopac.addon.testing import SINOPAC_ADDON_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that sinopac.addon is properly installed."""

    layer = SINOPAC_ADDON_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinopac.addon is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sinopac.addon'))

    def test_browserlayer(self):
        """Test that ISinopacAddonLayer is registered."""
        from sinopac.addon.interfaces import (
            ISinopacAddonLayer)
        from plone.browserlayer import utils
        self.assertIn(ISinopacAddonLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINOPAC_ADDON_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['sinopac.addon'])

    def test_product_uninstalled(self):
        """Test if sinopac.addon is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sinopac.addon'))

    def test_browserlayer_removed(self):
        """Test that ISinopacAddonLayer is removed."""
        from sinopac.addon.interfaces import ISinopacAddonLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISinopacAddonLayer, utils.registered_layers())
