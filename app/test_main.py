from unittest import mock
from app.main import outdated_products
import pytest
from typing import Any
import datetime


@mock.patch("datetime.date")
@pytest.mark.parametrize(
    "products, expected_result, datetime_value",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            [],
            datetime.date(2022, 1, 1),
            id="no one is expired"
        ),

        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            [],
            datetime.date(2022, 2, 1),
            id="no one is expired for today"
        ),

        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            [
                "duck"
            ],
            datetime.date(2022, 2, 2),
            id="1 expired product"
        )
    ]
)
def test_outdated_products(
        mocked_date_today: Any,
        products: list,
        expected_result: list,
        datetime_value: datetime.date
) -> None:
    mocked_date_today.today.return_value = datetime_value
    mocked_date_today.side_effect = \
        lambda *args, **kw: datetime.date(*args, **kw)
    assert outdated_products(products) == expected_result
