import unittest

from marqeta.errors import MarqetaError
from tests.lib.client import get_client


class TestUsersNotesSave(unittest.TestCase):
    """Tests for the users.notes.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in the class."""
        cls.client = get_client()

    def verify_user_note(self, response, verify):
        """

        Verifies a user note matches the expected values.

        Parameters:
        response (CardholderNoteResponseModel): The response to verify.

        verify (Dictionary): The values that should be in the response.

        """

        # Verify the correct class is being tested
        actual = response.__class__.__name__
        expected = "CardholderNoteResponseModel"

        self.assertEqual(actual, expected, "Unexpected response found")

        # Verify the expected attributes are defined
        expected_attributes = [
            "token",
            "description",
            "created_by",
            "private",
            "created_time",
            "last_modified_time",
        ]

        for attribute in expected_attributes:
            with self.subTest(f"{attribute} is not defined"):
                self.assertIsNotNone(getattr(response, attribute))

        # Verify values match expected values
        match_attributes = list(verify.keys())

        for attribute in match_attributes:
            with self.subTest(f"{attribute} does not match the expected value"):
                self.assertEqual(getattr(response, attribute), verify[attribute])

    def test_notes_save(self):
        """Update a note."""

        user = self.client.users.create({})

        note_request = {
            "description": "B Sharp",
            "created_by": "Piano Man",
            "created_by_user_role": "USER",
        }

        note = self.client.users(user.token).notes.create(note_request)

        updated_note_request = {"description": "A Flat"}
        updated_note = self.client.users(user.token).notes.save(
            note.token, updated_note_request
        )

        self.verify_user_note(updated_note, updated_note_request)

    def test_notes_save_no_info(self):
        """Update a note with no information."""

        user = self.client.users.create({})

        note_request = {
            "description": "B Sharp",
            "created_by": "Piano Man",
            "created_by_user_role": "USER",
        }

        note = self.client.users(user.token).notes.create(note_request)

        updated_note = {}

        with self.assertRaises(MarqetaError):
            self.client.users(user.token).notes.save(note.token, updated_note)
