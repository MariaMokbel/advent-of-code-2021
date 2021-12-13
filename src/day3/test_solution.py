from unittest import TestCase

from src.day3.solution import get_rate


class TestSolutionDay3(TestCase):

    def test_get_rate_returns_0_and_3_with_10_00_00_diagnostic_report(self):
        # Given
        diagnostic_report = ["10", "00", "00"]

        # When
        gamma, epsilon = get_rate(diagnostic_report)

        # Then
        self.assertEqual(gamma, 0)
        self.assertEqual(epsilon, 3)

    def test_get_rate_returns_5_and_2_with_100_101_111_diagnostic_report(self):
        # Given
        diagnostic_report = ["100", "101", "111"]

        # When
        gamma, epsilon = get_rate(diagnostic_report)

        # Then
        self.assertEqual(gamma, 5)
        self.assertEqual(epsilon, 2)

