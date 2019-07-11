import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_program_funding_source_response
from marqeta.errors import MarqetaError


class TestFundingSourcesProgramCreate(unittest.TestCase):
    """Tests for the funding_sources.program.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_program_create(self):
        """Creates a program funding source."""

        program_funding_source_request = FundingSources.get_program_source_funding_request()

        program = self.client.funding_sources.program.create(
            program_funding_source_request)

        verify_program_funding_source_response(
            self, program, program_funding_source_request)

    def test_program_create_bad_request(self):
        """Tests error handling when the request is missing required fields."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.program.create({})
