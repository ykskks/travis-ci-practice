import pytest
import main


def test_count_carbons():
    glucose = "OC[C@@H](O1)[C@@H](O)[C@H](O)[C@@H](O)[C@@H](O)"
    nicotine = "CN1CCC[C@H]1c2cccnc2"
    carbons_in_glucose = main.count_carbons(glucose)
    carbons_in_nicotine = main.count_carbons(nicotine)
    assert carbons_in_glucose == 6
    assert carbons_in_nicotine == 10


def test_count_nitrogens():
    glucose = "OC[C@@H](O1)[C@@H](O)[C@H](O)[C@@H](O)[C@@H](O)"
    nicotine = "CN1CCC[C@H]1c2cccnc2"
    nitrogens_in_glucose = main.count_nitrogens(glucose)
    nitrogens_in_nicotine = main.count_nitrogens(nicotine)
    assert nitrogens_in_glucose == 0
    assert nitrogens_in_nicotine == 2


if __name__ == "__main__":
    pytest.main(["-v", __file__])
