# ##################################################################################################
#   MIT License                                                                                    #
#                                                                                                  #
#   Copyright (c) 2023 Jon Duea                                                                    #
#                                                                                                  #
#   Permission is hereby granted, free of charge, to any person obtaining a copy                   #
#   of this software and associated documentation files (the "Software"), to deal                  #
#   in the Software without restriction, including without limitation the rights                   #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                      #
#   copies of the Software, and to permit persons to whom the Software is                          #
#   furnished to do so, subject to the following conditions:                                       #
#                                                                                                  #
#   The above copyright notice and this permission notice shall be included in all                 #
#   copies or substantial portions of the Software.                                                #
#                                                                                                  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                     #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                       #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                    #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                         #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                  #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                  #
#   SOFTWARE.                                                                                      #
# ##################################################################################################
import time
import uuid

from PySide6.QtCore import QRunnable, Slot

from modules.concurrent.worker_signals import WorkerSignals


class Worker(QRunnable):
    """
    Worker Thread

    Inherits from QRunnable to handle worker thread setup, signals, and wrap-up.

    Parameters
    ----------
    *args : tuple
     0 or more positional arguments to make available to the run code

    **kwargs : dict, optional
     Keywords arguments to make available to the run code

    Attributes
    ----------
    worker_id : uuid.uuid4()
     Unique identifier for the worker thread.

    signals : WorkerSignals
     0 or more signals to make available to the run code

    See Also
    --------
    modules.concurrent.worker_signals.WorkerSignals
     class that holds signals to make avaialable to workers.

    Returns
    -------
    result : any
     May return any value that is returned by the run method.

    Raises
    ------
    exception : str
     May raise any exception that is raised by the run method.
    """

    def __init__(self):
        super().__init__()
        self.worker_id = uuid.uuid4().hex
        self.signals = WorkerSignals()
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        """Initialize the worker thread with passed self.args, self.kwargs."""
        try:
            for _ in range(self.iterations):
                time.sleep(0.01)
        except Exception as e:
            self.signals.error.emit(e)
        else:
            self.signals.finished.emit()
            self.signals.result.emit(self.result)
        pass
