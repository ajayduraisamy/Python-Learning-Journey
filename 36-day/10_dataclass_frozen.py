# 10_dataclass_frozen.py
# Frozen dataclass makes object immutable

from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    app_name: str
    version: str

cfg = Config("MyApp", "1.0")
print(cfg)

# cfg.version = "2.0"  # This will raise FrozenInstanceError
