def reverse_singly_linked_list(head):
  """Reverses a singly linked list.

  Args:
    head: The head of the linked list.

  Returns:
    The head of the reversed linked list.
  """

  previous = None
  current = head
  next = None
  while current is not None:
    next = current.next
    current.next = previous
    previous = current
    current = next

  return previous


