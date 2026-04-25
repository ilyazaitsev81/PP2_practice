import os

class ScoreManager:
    def __init__(self, path="highscore.txt"):
        self.path = path
        self.current = 0
        self.high = self._load()

    def _load(self):
        if not os.path.exists(self.path):
            return 0
        try:
            with open(self.path) as f:
                return int(f.read().strip() or 0)
        except ValueError:
            return 0

    def _save(self):
        with open(self.path, "w") as f:
            f.write(str(self.high))

    def add(self, points):
        self.current += 1
        if self.current > self.high:
            self.high = self.current
            self._save()

    def reset(self):
        self.current = 0