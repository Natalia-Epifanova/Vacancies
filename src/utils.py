def type_of_salary(vacancy: dict) -> str:
    salary_str = "Зарплата не указана"

    if isinstance(vacancy.get("salary"), dict) and vacancy.get("salary") is not None:
        salary = vacancy.get("salary")
        if salary.get("from") is not None and salary.get("to") is not None:
            salary_str = f"{salary.get('from')} - {salary.get('to')}"
        elif salary.get("from") is not None:
            salary_str = f"{salary.get('from')}"
        elif salary.get("to") is not None:
            salary_str = f"{salary.get('to')}"
    elif isinstance(vacancy.get("salary"), str):
        salary_str = vacancy.get("salary")
    return salary_str


def type_of_description(vacancy: dict) -> str:
    description_str = "Нет информации о требованиях и обязанностях"
    if isinstance(vacancy.get("snippet"), dict) and vacancy.get("snippet") is not None:
        description = vacancy.get("snippet")
        if description.get("requirement") is not None and description.get("responsibility") is not None:
            description_str = (
                f"Требования: {description.get('requirement')}. \n" f"Обязанности: {description.get('responsibility')}"
            )
        elif description.get("requirement") is not None:
            description_str = f"Требования: {description.get('requirement')}."
        elif description.get("responsibility") is not None:
            description_str = f"Обязанности: {description.get('responsibility')}"
    elif isinstance(vacancy.get("snippet"), str):
        description_str = vacancy.get("snippet")

    return description_str

