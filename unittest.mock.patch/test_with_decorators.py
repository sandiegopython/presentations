from datetime import date

from unittest import TestCase
from unittest.mock import patch

from utils import day_of_week


class TestDayOfWeek(TestCase):

    """Test utils.day_of_week function"""

    @patch('utils.date')
    def test_sunday(self, fake_date):
        fake_date.today.return_value = date(2014, 10, 26)
        assert day_of_week() == "Monday"

    @patch('utils.date')
    def test_friday(self, fake_date):
        fake_date.today.return_value = date(2014, 10, 31)
        assert day_of_week() == "Friday"

    @patch('utils.date')
    def test_saturday(self, fake_date):
        fake_date.today.return_value = date(2014, 10, 25)
        assert day_of_week() == "Saturday"
