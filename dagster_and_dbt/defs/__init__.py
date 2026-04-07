import dagster as dg
from dagster_and_dbt.defs.jobs import (
    trip_update_job,
    weekly_update_job,
    adhoc_request_job,
)
from dagster_and_dbt.defs.assets.dbt import dbt_analytics
from dagster_and_dbt.defs.assets.metrics import trips_by_week
from dagster_and_dbt.defs.assets.requests import adhoc_request
from dagster_and_dbt.defs.resources import dbt_resource, database_resource
from dagster_and_dbt.defs.schedules import trip_update_schedule, weekly_update_schedule
from dagster_and_dbt.defs.sensors import adhoc_request_sensor

defs = dg.Definitions(
    assets=[dbt_analytics, trips_by_week, adhoc_request],
    jobs=[trip_update_job, weekly_update_job, adhoc_request_job],
    resources={
        "dbt": dbt_resource,
        "database": database_resource,
    },
    schedules=[trip_update_schedule, weekly_update_schedule],
    sensors=[adhoc_request_sensor],
)
