from datetime import date

from unittest import TestCase
from unittest.mock import patch

from utils import day_of_week


@patch('utils.date')
class TestDayOfWeek(TestCase):

    """Test utils.day_of_week function"""

    def test_sunday(self, fake_date):
        fake_date.today.return_value = date(2014, 10, 26)
        assert day_of_week() == "Sunday"

    def test_friday(self, fake_date):
        fake_date.today.return_value = date(2014, 10, 31)
        assert day_of_week() == "Friday"

    def test_saturday(self, fake_date):
        fake_date.today.return_value = date(2014, 10, 25)
        assert day_of_week() == "Saturday"
