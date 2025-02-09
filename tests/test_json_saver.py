import json
from unittest.mock import mock_open, patch

import pytest

from src.json_saver import JSONSaver
from src.utils import dict_to_vac
from src.vacancy import Vacancy
from tests.conftest import first_vacancy, second_vacancy


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(
    [{"name": "Программист", "alternate_url": "https://hh.ru/vacancy/93353083", "salary": "100000 - 120000",
      "snippet": {
          "requirement": None,
          "responsibility": "Оценивать вид из окна"
      }}]))
def test_read_data(mock_file):
    json_saver_for_test = JSONSaver("data/test_json_saver.json")
    result = json_saver_for_test.read_data()
    assert len(result) == 1
    assert result[0].vacancy_name == "Программист"
    assert result[0].vacancy_url == "https://hh.ru/vacancy/93353083"
    assert result[0].salary == "100000 - 120000"
    assert result[0].description == "Обязанности: Оценивать вид из окна"


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(
    [{"name": "Программист", "alternate_url": "https://hh.ru/vacancy/93353083", "salary": "100000 - 120000",
      "snippet": {"requirement": None, "responsibility": "Оценивать вид из окна"}}]))
def test_read_data_invalid_json(mock_file, capsys):
    json_saver_for_test = JSONSaver("data/test_json_saver.json")
    mock_file.return_value.read.side_effect = "invalid json"
    json_saver_for_test.read_data()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Ошибка декодирования JSON в файле data/test_json_saver.json. Убедитесь, что файл содержит корректный JSON."


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_data_file_not_found(mock_file, capsys):
    json_saver_for_test = JSONSaver("data/test_json_saver.json")
    json_saver_for_test.read_data()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Файл data/test_json_saver.json не найден"


def test_setter_filename(json_saver_for_test):
    json_saver_for_test.filename = 'data/test_json_saver.json'
    assert json_saver_for_test.filename == 'data/test_json_saver.json'


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(
    [{"name": "Программист", "alternate_url": "https://hh.ru/vacancy/93353083", "salary": "100000 - 120000",
      "snippet": {
          "requirement": None,
          "responsibility": "Оценивать вид из окна"
      }}]))
def test_add_vacancy(mock_file, second_vacancy):
    json_saver = JSONSaver("data/test.json")
    json_saver.add_vacancy(second_vacancy)
    assert len(json_saver.vacancies_list) == 2
    assert json_saver.vacancies_list[0]['name'] == "Программист"
    assert json_saver.vacancies_list[1]['name'] == "Java Developer"
