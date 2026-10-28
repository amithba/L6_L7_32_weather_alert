
import pytest

from weather_alert import (
    wind_alert,
    rain_alert,
    heat_alert,
    overall_alert,
)


@pytest.mark.parametrize("speed, expected", [
    (38, "none"),
    (39, "advisory"),
    (61, "advisory"),
    (62, "watch"),
    (88, "watch"),
    (89, "warning"),
])
def test_wind_branches(speed, expected):
    assert wind_alert(speed) == expected


@pytest.mark.parametrize("rainfall, storm, expected", [
    (9, False, "none"),
    (9, True, "none"),
    (10, False, "advisory"),
    (10, True, "watch"),
    (49, False, "advisory"),
    (49, True, "watch"),
    (50, False, "watch"),
    (50, True, "warning"),
])
def test_rain_branches(rainfall, storm, expected):
    assert rain_alert(rainfall, storm) == expected


@pytest.mark.parametrize("temperature, humidity, expected", [
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
def test_heat_branches(temperature, humidity, expected):
    assert heat_alert(temperature, humidity) == expected


def test_overall_alert_empty():
    assert overall_alert([]) == "none"


def test_overall_alert_highest_severity():
    assert overall_alert(["warning", "watch", "advisory"]) == "warning"


def test_overall_alert_lower_severity():
    assert overall_alert(["advisory", "watch"]) == "watch"


def test_overall_alert_unknown_type():
    with pytest.raises(ValueError):
        overall_alert(["unknown"])