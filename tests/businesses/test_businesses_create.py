import unittest

from tests.lib.client import get_client
from tests.lib.business_card_holder_response import verify_business_card_holder_response
from tests.lib.utilities import Utilities


class TestBusinessesCreate(unittest.TestCase):
    """Tests for the businesses.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""

        cls.client = get_client()

    def test_business_create_empty(self):
        """Creates a business with an empty card holder model."""

        business_card_holder_model = {}

        business = self.client.businesses.create(business_card_holder_model)

        verify_business_card_holder_response(self, business, business_card_holder_model)

    def test_business_create_basic(self):
        """Creates a business with basic information."""

        business_card_holder_model = {
            "business_name_legal": "qe_test_company",
            "office_location": {
                "address1": "3200 Grand Ave.",
                "city": "Oakland",
                "state": "CA",
                "zip": "94612",
            },
        }

        business = self.client.businesses.create(business_card_holder_model)

        verify_business_card_holder_response(self, business, business_card_holder_model)

    def xtest_business_create_in_current_location_since_formats(self):
        """Creates businesses with in_current_location_since set to all the date formats."""

        times = Utilities.get_current_time_all_formats()

        for time in times:
            business_card_holder_model = {"in_current_location_since": time}

            business = self.client.businesses.create(business_card_holder_model)

            verify_business_card_holder_response(
                self, business, business_card_holder_model
            )

    def xtest_business_create_date_established_formats(self):
        """Creates businesses with date_established set to all the date formats."""

        times = Utilities.get_current_time_all_formats()

        for time in times:
            business_card_holder_model = {"date_established": time}

            business = self.client.businesses.create(business_card_holder_model)

            verify_business_card_holder_response(
                self, business, business_card_holder_model
            )
