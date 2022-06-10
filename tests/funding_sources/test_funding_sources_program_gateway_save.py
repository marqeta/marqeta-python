import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import (
    verify_gateway_program_funding_source_response,
)
from marqeta.errors import MarqetaError


class TestFundingSourcesProgramGatewaySave(unittest.TestCase):
    """Tests for the funding_sources.program_gateway.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_program_gateway_save_success(self):
        """Successfully updates a program gateway."""

        request = FundingSources.get_program_gateway_funding_request()

        source = self.client.funding_sources.program_gateway.create(request)

        request["url"] = "https://qe_updated.marqeta.com"

        updated = self.client.funding_sources.program_gateway.save(
            source.token, request
        )

        verify_gateway_program_funding_source_response(self, updated, request)

    def test_program_gateway_save_empty_request(self):
        """Checks behavior when the update request is empty."""

        request = FundingSources.get_program_gateway_funding_request()

        source = self.client.funding_sources.program_gateway.create(request)

        updated = self.client.funding_sources.program_gateway.save(source.token, {})

        verify_gateway_program_funding_source_response(self, updated, request)

    def test_program_gateway_save_unknown_gateway(self):
        """Checks behavior when the program gateway can not be found."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.program_gateway.save(
                "Not a program gateway token", {}
            )
