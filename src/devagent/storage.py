"""Simple storage service placeholder."""

from dataclasses import dataclass

@dataclass
class StorageService:
    """Mock storage service that prints upload actions."""

    def upload(self, source: str, destination: str) -> None:
        print(f"[Storage] Uploading {source} -> {destination}")
