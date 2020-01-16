import pytest
import main


def test_count_carbons():
    glucose = "OC[C@@H](O1)[C@@H](O)[C@H](O)[C@@H](O)[C@@H](O)"
    carbons_in_glucose = main.count_carbons(glucose)
    assert carbons_in_glucose == 6


if __name__ == "__main__":
    pytest.main(["-v", __file__])
