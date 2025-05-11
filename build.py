import subprocess
from typing import Any, Sequence

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from packaging.version import Version


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        if self.target_name != 'wheel':
            return

        self.run(["npm", "version", self.version, "--no-git-tag-version",
            "--allow-same-version"])
        self.run(["npm", "ci"])
        self.run(["npm", "run", "build"])

    def run(self, args: Sequence[str]) -> None:
        process = subprocess.run(args, cwd=self.config.get("src"))

        if process.returncode:
            raise Exception("Error running SPA build")

    @property
    def version(self) -> str:
        version = Version(self.metadata.version)
        suffix = f"-dev.{version.dev}" if version.dev is not None else ""

        return f"{version.major}.{version.minor}.{version.micro}{suffix}"
