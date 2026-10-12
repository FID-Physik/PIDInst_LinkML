"""Data model package for PIDInst_LinkML."""

from pathlib import Path
from .pidinst_linkml import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "pidinst_linkml.yaml"
