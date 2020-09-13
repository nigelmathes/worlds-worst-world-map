""" Test the world map """
import httpx

from worlds_worst_world_map.world_map import make_map


def test_make_map() -> None:
    """
    Test that the make_map() function works as expected
    """
    # Arrange - this is the Statue of Liberty
    test_event = {"body": {"lat": "40.6892", "lon": "-74.0445"}}

    expected_result = {
        "statusCode": 200,
        "body": {
            "Crown Cafe": "cafe",
            "Statue of Liberty Ferry Terminal": "ferry_terminal",
        },
        "headers": {"Access-Control-Allow-Origin": "*"},
    }

    # Act
    test_result = make_map(event=test_event, context=test_event)

    # Assert
    assert test_result == expected_result
