# Test Times File

from times import compute_overlap_time
from times import time_range
import datetime

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2,3600/2)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)    
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00'), ('2010-01-12 11:15:00', '2010-01-12 10:37:00'), ('2010-01-12 11:15:00', '2010-01-12 10:45:00')]
    assert result == expected