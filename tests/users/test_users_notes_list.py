import unittest

from tests.lib.client import get_client


class TestUsersNotesList(unittest.TestCase):
    """Tests for the users.notes.list endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in the class."""
        cls.client = get_client()

    def setUp(self):
        """Setup for each test."""

        self.user = self.client.users.create({})

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

    def test_notes_list_1(self):
        """Retrieve 1 note."""

        note_request = {
            "description": "B Sharp",
            "created_by": "Piano Man",
            "created_by_user_role": "USER",
        }

        self.client.users(self.user.token).notes.create(note_request)

        notes_list = self.client.users(self.user.token).notes.list()

        self.assertEqual(
            len(notes_list), 1, "Notes list has incorrect number of entries"
        )

        self.verify_user_note(notes_list[0], note_request)

    def test_notes_list_2(self):
        """Retrieve 2 notes."""

        first_note = {
            "description": "B Sharp",
            "created_by": "Piano Man",
            "created_by_user_role": "USER",
        }

        self.client.users(self.user.token).notes.create(first_note)

        second_note = {
            "description": "C Flat",
            "created_by": "Two Dimensional",
            "created_by_user_role": "ADMIN",
        }

        self.client.users(self.user.token).notes.create(second_note)

        notes_list = self.client.users(self.user.token).notes.list()

        self.assertEqual(
            len(notes_list), 2, "Notes list has incorrect number of entries"
        )

        note_one = notes_list[0]
        note_two = notes_list[1]

        # Can not assume the notes will be in the order created
        if note_one.description == first_note["description"]:
            self.verify_user_note(note_one, first_note)
            self.verify_user_note(note_two, second_note)
        elif note_one.description == second_note["description"]:
            self.verify_user_note(note_one, second_note)
            self.verify_user_note(note_two, first_note)
        else:
            self.fail("Note one description did not match any expected value")

    def test_notes_list_0(self):
        """Retrieve 0 notes."""

        notes_list = self.client.users(self.user.token).notes.list()

        self.assertEqual(
            len(notes_list), 0, "Notes list has incorrect number of entries"
        )
