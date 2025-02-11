from unittest.mock import patch

from src.head_hunter_api import HeadHunterAPI


@patch("src.head_hunter_api.requests.get")
def test_head_hunter_api_connect(mock_get, two_vacs_from_hh):
    """Тест корректного ответа по API подключению"""
    mock_get.return_value.json.return_value = two_vacs_from_hh
    mock_get.return_value.status_code = 200
    hh_api_test = HeadHunterAPI()
    vacancies = hh_api_test.get_vacancies("Разработчик")
    mock_get.assert_called_once()

    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Java-разработчик"
    assert vacancies[1]["name"] == "Python-разработчик"


@patch("src.head_hunter_api.requests.get")
def test_head_hunter_api_connect_no_response(mock_get):
    """Тест ошибки при запросе по API"""
    mock_get.return_value.status_code = 400
    hh_api_test = HeadHunterAPI()
    vacancies = hh_api_test.get_vacancies("Разработчик")
    assert len(vacancies) == 0
