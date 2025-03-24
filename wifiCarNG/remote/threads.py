import threading
import time
import random

class DataStore:
    """
    A thread-safe data store for holding results.
    """
    def __init__(self):
        self._lock = threading.Lock()
        self.data = {}

    def update(self, key, value):
        """
        Store the processed value with a given key, ensuring
        thread-safe access to self.data.
        """
        with self._lock:
            self.data[key] = value

    def read(self, key):
        """
        Return the stored value for the given key, or None if
        it doesn't exist, in a thread-safe manner.
        """
        with self._lock:
            return self.data.get(key, None)

def worker_task(data_store, thread_id):
    """
    A sample worker function that simulates data processing
    by sleeping for a random time, then storing a random result.
    """
    print(f"[Thread {thread_id}] Starting processing.")
    # Simulate a longer or shorter task
    time.sleep(random.uniform(0.5, 3.0))

    # Simulate some computed result
    result = random.randint(1, 100)
    data_store.update(thread_id, result)

    print(f"[Thread {thread_id}] Finished processing. Stored: {result}")

def main():
    # Create a shared DataStore instance
    shared_store = DataStore()
    
    # Create and start multiple worker threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker_task, args=(shared_store, i))
        threads.append(t)
        t.start()

    # While threads are running, we can periodically read the shared data
    while any(t.is_alive() for t in threads):
        print("\n--- Intermediate Read of Shared Data ---")
        with shared_store._lock:
            print(shared_store.data)
        time.sleep(0.3)

    # Make sure all threads have finished
    for t in threads:
        t.join()

    # Final state of the shared data after all threads have completed
    print("\n--- Final Shared Data ---")
    print(shared_store.data)

if __name__ == "__main__":
    main()
