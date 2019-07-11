import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_gateway_program_funding_source_response
from marqeta.errors import MarqetaError


class TestFundingSourcesProgramGatewayFind(unittest.TestCase):
    """Tests for the funding_sources.program_gateway.find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup each for all tests in the class."""

        cls.client = get_client()

    def test_program_gateway_find_success(self):
        """Finds the program gateway it is searching for."""

        funding_request = FundingSources.get_program_gateway_funding_request()

        source = self.client.funding_sources.program_gateway.create(
            funding_request)

        found = self.client.funding_sources.program_gateway.find(source.token)

        verify = FundingSources.get_funding_source_verify(source)

        verify_gateway_program_funding_source_response(self, found, verify)

    def test_program_gateway_find_fail(self):
        """Tests behavior when program gateway can not be found."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.program_gateway.find(
                'Not a program gateway token')
