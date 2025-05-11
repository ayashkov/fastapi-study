import subprocess
from typing import Any, Sequence

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        if self.target_name != 'wheel':
            return

        self.run(["npm", "ci"])
        self.run(["npm", "run", "build"])

    def run(self, args: Sequence[str]) -> None:
        process = subprocess.run(args, cwd=self.config.get("src"))

        if process.returncode:
            raise Exception("Error running SPA build")
