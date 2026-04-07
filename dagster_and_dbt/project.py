from pathlib import Path
from dagster_dbt import DbtProject


dbt_project = DbtProject(
    project_dir=Path(__file__).parent.joinpath("analytics").resolve(),
)
print(f"Using dbt project at {dbt_project.project_dir}")
dbt_project.prepare_if_dev()
