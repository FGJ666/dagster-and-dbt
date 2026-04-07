# dagster_and_dbt/__init__.py
from dagster_and_dbt.definitions import defs

# Экспортируем defs, чтобы Dagster мог его найти при импорте пакета
__all__ = ["defs"]
