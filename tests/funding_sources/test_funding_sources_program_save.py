import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import (
    verify_program_funding_source_response,
)
from marqeta.errors import MarqetaError


class TestFundingSourcesProgramSave(unittest.TestCase):
    """Tests for the funding_sources.program.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_program_save_name(self):
        """Changes the name of a program."""

        program_funding_source_request = (
            FundingSources.get_program_source_funding_request()
        )

        program = self.client.funding_sources.program.create(
            program_funding_source_request
        )

        change_request = {"name": "changed_" + program_funding_source_request["name"]}

        updated = self.client.funding_sources.program.save(
            program.token, change_request
        )

        verify_program_funding_source_response(self, updated, change_request)

    def test_program_save_active(self):
        """Deactivates a program."""

        program_funding_source_request = (
            FundingSources.get_program_source_funding_request()
        )

        program = self.client.funding_sources.program.create(
            program_funding_source_request
        )

        change_request = {"active": False}

        updated = self.client.funding_sources.program.save(
            program.token, change_request
        )

        verify_program_funding_source_response(self, updated, change_request)

    def test_program_save_both(self):
        """Changes the name of a program and deactivates it."""

        program_funding_source_request = (
            FundingSources.get_program_source_funding_request()
        )

        program = self.client.funding_sources.program.create(
            program_funding_source_request
        )

        change_request = {
            "name": "deactivated_" + program_funding_source_request["name"],
            "active": False,
        }

        updated = self.client.funding_sources.program.save(
            program.token, change_request
        )

        verify_program_funding_source_response(self, updated, change_request)

    def test_program_save_empty(self):
        """Updates a program with an empty record."""

        program_funding_source_request = (
            FundingSources.get_program_source_funding_request()
        )
        program_funding_source_request["active"] = True

        program = self.client.funding_sources.program.create(
            program_funding_source_request
        )

        updated = self.client.funding_sources.program.save(program.token, {})

        verify = FundingSources.get_funding_source_verify(program)

        verify_program_funding_source_response(self, updated, verify)

    def test_program_save_unknown_program(self):
        """Verifies behavior when program is unknown."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.program.save("Not a program token", {})
