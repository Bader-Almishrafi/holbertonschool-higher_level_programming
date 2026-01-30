#!/usr/bin/python3


class CountedIterator:
    """
    Iterator wrapper that keeps track of
    how many items have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and the counter
        """
        # Create an iterator from the iterable
        self.iterator = iter(iterable)
        # Counter to track number of items fetched
        self.count = 0

    def __next__(self):
        """
        Return the next item and increment the counter.
        Raises StopIteration when there are no more items.
        """
        # Get the next item from the original iterator
        item = next(self.iterator)
        # Increment the counter after successfully fetching an item
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over
        """
        return self.count
