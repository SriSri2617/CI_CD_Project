import pytest
from src.order import Order
from src.paymentgateway import PaymentGateway


@pytest.mark.integration
# successful payment
def test_payment_success(mocker):
    # products - name, price & qty
    products = [("soft toys", 100, 2),
                ("Toy cars", 250, 1)]

    order = Order(products)
    gateway = PaymentGateway()

    mocker.patch.object(gateway, "execute_payment", return_value=True)

    # spy on execute_payment
    spy = mocker.spy(gateway, "execute_payment")

    # make payment
    total = order.make_payment(gateway)

    assert total is True
    spy.assert_called_with(450)

    assert order.status == "paid"


@pytest.mark.integration
# unsuccessful payment
def test_payment_failure(mocker):
    # products - name, price & qty
    products = [("soft toys", 100, 2),
                ("Toy cars", 250, 1)]

    order = Order(products)
    gateway = PaymentGateway()

    # patch simulate failure
    mocker.patch.object(gateway, "execute_payment", return_value=False)

    # spy on execute_payment
    spy = mocker.spy(gateway, "execute_payment")

    result = order.make_payment(gateway)

    assert result is False
    spy.assert_called_with(450)
    assert order.status == "error" or order.status == "Unpaid"
