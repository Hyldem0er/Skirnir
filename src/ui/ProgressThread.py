from PyQt5.QtCore import QThread, pyqtSignal
import time
class ProgressThread(QThread):
    reportProgress = pyqtSignal(int)
    calculationFinished = pyqtSignal()

    def __init__(self, size):
        """
        Initialize the CalculationWorker instance.

        Args:
        size (int): The size of the calculation.

        Returns:
        None
        """
        super().__init__()
        self.size = size


def run(self) -> None:
    """
    Run the calculation process and emit progress updates.

    Returns:
        None
    """
    # Setting up a loop to set the value of the progress bar
    for i in range(101):
        # Slowing down the loop
        time.sleep(100 / self.size)

        # Setting the value of the progress bar
        self.reportProgress.emit(i)

    # Emitting the signal to indicate the calculation is finished
    self.calculationFinished.emit()
