import pytest
import allure
from selenium import webdriver
from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")

        browser = webdriver.Chrome()
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"),
                    DataProvider().get_api_key(),
                    DataProvider().get_token())


@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "", "")


@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi(ConfigProvider().get("api", "base_url"),
                   DataProvider().get_api_key(),
                   DataProvider().get_token())

    with allure.step("Предварительно создать доску"):
        resp = api.create_board("Board to be deleted").get("id")
        return resp


@pytest.fixture
def delete_board() -> str:
    dictionary = {"board_id": ""}
    yield dictionary

    with allure.step("Удалит доску после теста"):
        api = BoardApi(ConfigProvider().get("api", "base_url"),
                       DataProvider().get_api_key(),
                       DataProvider().get_token())
        api.delete_board_by_id(dictionary.get("board_id"))


@pytest.fixture
def test_data():
    return DataProvider()
