from dataclasses import dataclass


@dataclass
class GoalData:
    id: int
    parent_id: int
    start_timestamp: int
    days_repeat: int
    current_points: float
    max_points: float
    finished: bool = False

    def finish(self):
        self.finished = True
