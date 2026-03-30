from dsa.queue import Queue
def test_queue_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(5)
    assert queue.dequeue() == 5