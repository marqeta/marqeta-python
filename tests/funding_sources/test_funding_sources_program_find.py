import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_program_funding_source_response
from marqeta.errors import MarqetaError


class TestFundingSourcesProgramFind(unittest.TestCase):
    """Tests for the funding_sources.program.find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_program_find(self):
        """Tests searching for a program."""

        program_funding_source_request = FundingSources.get_program_source_funding_request()

        program = self.client.funding_sources.program.create(
            program_funding_source_request)

        found = self.client.funding_sources.program.find(program.token)

        verify = FundingSources.get_funding_source_verify(program)

        verify_program_funding_source_response(self, found, verify)

    def test_program_find_unknown_program(self):
        """Tests looking for a program that doesn't exist."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.program.find('Not a program token')
