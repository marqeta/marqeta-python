import unittest
from tests.lib.client import get_client
from tests.lib.card_product_verifications import (
    verify_card_product_response,
    verify_transaction_controls,
)
from tests.lib.utilities import Utilities


class TestCardProductsCreate(unittest.TestCase):
    """Tests creating card products."""

    def setUp(self):
        """Setup each test."""

        self.client = get_client()
        self.times = Utilities.get_current_time_all_formats()

    def xtest_create_all_start_date_formats(self):
        """Creates a card product with all the start date formats."""

        for time in self.times:
            product_details = {"name": "Start Date Card Product", "start_date": time}

            card_product = self.client.card_products.create(product_details)
            verify_card_product_response(self, card_product, product_details)

    def xtest_create_all_end_date_formats(self):
        """Creates a card product with all the end date formats."""

        for time in self.times:
            product_details = {
                "name": "End Date Card Product",
                "start_date": self.times[0],
                "end_date": time,
            }

            card_product = self.client.card_products.create(product_details)

            verify_card_product_response(self, card_product, product_details)

    def test_create_verify_default_transaction_controls(self):
        """Verifies the default transaction controls for a card product."""

        product_details = {
            "name": "Default transaction card product",
            "start_date": self.times[0],
        }

        card_product = self.client.card_products.create(product_details)

        verify_card_product_response(self, card_product, product_details)

        transaction_controls = card_product.config.transaction_controls

        transaction_controls_defaults = {
            "accepted_countries_token": "accept_us_only",
            "always_require_pin": False,
            "always_require_icc": False,
            "allow_gpa_auth": True,
            "require_card_not_present_card_security_code": False,
            "allow_mcc_group_authorization_controls": True,
            "allow_first_pin_set_via_financial_transaction": False,
            "ignore_card_suspended_state": False,
            "allow_chip_fallback": True,
            "allow_network_load": False,
            "allow_network_load_card_activation": False,
            "allow_quasi_cash": False,
            "enable_partial_auth_approval": True,
        }

        verify_transaction_controls(
            self, transaction_controls, transaction_controls_defaults
        )

    def test_create_allow_chip_fallback_false(self):
        """Verifies can set allow chip fallback to false."""

        transaction_controls_settings = {"allow_chip_fallback": False}

        product_details = {
            "name": "Chip fallback false",
            "start_date": self.times[0],
            "config": {"transaction_controls": transaction_controls_settings},
        }

        card_product = self.client.card_products.create(product_details)

        verify_card_product_response(self, card_product, product_details)
