
import pytest

from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


@pytest.mark.parametrize("speed, expected", [
    (0, "none"),
    (38, "none"),
    (39, "advisory"),
    (61, "advisory"),
    (62, "watch"),
    (88, "watch"),
    (89, "warning"),
    (100, "warning"),
])
def test_wind_alert(speed, expected):
    assert wind_alert(speed) == expected


@pytest.mark.parametrize("rain, saturated, expected", [
    (0, False, "none"),
    (9, True, "none"),
    (10, False, "advisory"),
    (10, True, "watch"),
    (49, False, "advisory"),
    (49, True, "watch"),
    (50, False, "watch"),
    (50, True, "warning"),
    (60, False, "watch"),
    (60, True, "warning"),
])
def test_rain_alert(rain, saturated, expected):
    assert rain_alert(rain, saturated) == expected


@pytest.mark.parametrize("temperature, humidity, expected", [
    (20, 40, "none"),
    (34, 40, "none"),
    (35, 40, "advisory"),
    (39, 40, "advisory"),
    (40, 40, "watch"),
    (44, 40, "watch"),
    (45, 40, "warning"),
    (30, 50, "none"),
    (34, 60, "advisory"),
    (39, 60, "watch"),
    (44, 60, "warning"),
])
def test_heat_alert(temperature, humidity, expected):
    assert heat_alert(temperature, humidity) == expected


def test_overall_empty():
    assert overall_alert([]) == "none"


def test_overall_severities():
    assert overall_alert(
        ["none", "advisory", "watch", "warning"]
    ) == "warning"


def test_overall_lower_severity():
    assert overall_alert(["watch", "advisory"]) == "watch"


def test_overall_unknown():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["storm"])
