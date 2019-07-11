import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_gateway_program_funding_source_response
from marqeta.errors import MarqetaError


class TestFundingSourceProgramGatewayCreate(unittest.TestCase):
    """Tests for the funding_source.program_gateway.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_program_gateway_create_success(self):
        """Creates a program gateway funding source."""

        funding_request = FundingSources.get_program_gateway_funding_request()

        source = self.client.funding_sources.program_gateway.create(
            funding_request)

        verify_gateway_program_funding_source_response(
            self, source, funding_request)

    def test_program_gateway_create_fail(self):
        """Tests behavior when funding request is bad."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.program_gateway.create({})
