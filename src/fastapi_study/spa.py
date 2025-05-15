import os

from fastapi.staticfiles import StaticFiles
from starlette.staticfiles import PathLike


class SinglePageApplication(StaticFiles):
    def __init__(
        self,
        directory: PathLike | None = None,
        packages: list[str | tuple[str, str]] | None = None,
        index='index.html'
    ) -> None:
        super().__init__(directory=directory, packages=packages,
            html=True, check_dir=True)
        self.index = index

    def lookup_path(self, path: str) -> tuple[str, os.stat_result]:
        full_path, stat_result = super().lookup_path(path)

        if stat_result is None:
            return super().lookup_path(self.index)

        return full_path, stat_result
