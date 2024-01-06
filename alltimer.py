import time
from datetime import datetime as dt


class Timer:
    def __init__(self, timer: tuple[int, int, int], rest: bool = False) -> None:
        """Timer Class. Iniciates the timer with the indicated timer
        hours, minutes and seconds.

        Args:
            timer (tuple[int, int, int]): hours, minutes and seconds as integers
            rest (bool, optional): rest between timers. Defaults to False.
        """
        self.time = time.time()
        self.timer_seconds = timer[0] * 3600 + timer[1] * 60 + timer[2]
        self.rest = rest
        self.timer = {
            "hours": timer[0],
            "minutes": timer[1],
            "seconds": timer[2],
        }

        self.starting_time = dt.utcfromtimestamp(self.time)
        self.current_time = dt.utcfromtimestamp(self._get_current())
        print(
            f'Timer object created at {self.starting_time.strftime("%H:%M:%S")}'
        )  # %f for ms
        print(
            f'Timer set for {self.timer["hours"]:02d}:{self.timer["minutes"]:02d}:{self.timer["seconds"]:02d}'
        )  # f"{number:02d}" to 01 instead of 1

    def _get_current(self):
        return time.time()

    def get_diff(self):
        """Gets the difference between starting time and current time.
        In seconds.

        Returns:
            time_difference (float): time difference in seconds.
        """
        self.current_time = dt.utcfromtimestamp(self._get_current())
        time_difference = self.current_time - self.starting_time
        time_difference = time_difference.total_seconds()
        return time_difference

    def update_countdown(self):
        """Calculates hours, minutes and seconds from time difference.

        Returns:
            hours, minutes, seconds (float): hours, minutes, seconds.
        """
        hours, reminder = divmod(self.get_diff(), 3600)
        minutes, seconds = divmod(reminder, 60)
        # return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        return hours, minutes, seconds

    def pause_timer(self):
        # function to stop timer, pending
        pass


def main():
    timer = Timer((0, 0, 61))

    print(
        f"{int(timer.update_countdown()[0]):02d}:{int(timer.update_countdown()[1]):02d}:{int(timer.update_countdown()[2]):02d}"
    )
    while timer.get_diff() <= timer.timer_seconds:
        # print(int(timer.get_diff()))
        time.sleep(1)
        h, m, s = timer.update_countdown()
        print(f"{int(h):02d}:{int(m):02d}:{int(s):02d}")


if __name__ == "__main__":
    main()
