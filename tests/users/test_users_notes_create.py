import unittest

from marqeta.errors import MarqetaError
from tests.lib.client import get_client


class TestUsersNotesCreate(unittest.TestCase):
    """Tests for the users.notes.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""

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

    def get_user(self):
        """Creates a user and verifies it has a token."""

        user = self.client.users.create({})

        self.assertIsNotNone(user.token, "Could not find user token")

        return user

    def get_note_request(self):
        """Returns a default note request."""

        return {"description": "B Sharp", "created_by": "Piano Man"}

    def test_notes_create_user_exists(self):
        """Create a note for an existing user."""

        user = self.get_user()

        note_request = self.get_note_request()

        note = self.client.users(user.token).notes.create(note_request)

        self.verify_user_note(note, note_request)

    def test_notes_create_user_does_not_exist(self):
        """Create a note for a user who doesn't exist."""

        with self.assertRaises(MarqetaError):
            self.client.users("Does not exist").notes.create(self.get_note_request())

    def test_notes_create_missing_all(self):
        """Create a note missing all the required fields."""

        user = self.get_user()

        note_request = {}

        with self.assertRaises(MarqetaError):
            self.client.users(user.token).notes.create(note_request)

    def test_notes_create_missing_description(self):
        """Create a note missing the description field."""

        user = self.get_user()

        note_request = {"created_by": "Piano Man"}

        with self.assertRaises(MarqetaError):
            self.client.users(user.token).notes.create(note_request)

    def test_notes_create_missing_created_by(self):
        """Create a note missing the created_by field."""

        user = self.get_user()

        note_request = {"description": "B Sharp"}

        with self.assertRaises(MarqetaError):
            self.client.users(user.token).notes.create(note_request)

    def test_notes_create_with_user_role(self):
        """Create a note with a user role."""

        user = self.get_user()

        note_request = {
            "description": "B Sharp",
            "created_by": "Piano Man",
            "created_by_user_role": "USER",
        }

        note = self.client.users(user.token).notes.create(note_request)

        self.verify_user_note(note, note_request)
