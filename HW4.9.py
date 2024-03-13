REVERSE(L):
  if (L.head == NULL OR L.head.next == NULL):
    return true  // No need to reverse if the list is empty or has a single element

  prev = NULL
  current = L.head
  while (current != NULL):
    next = current.next  // Save the next node
    current.next = prev  // Reverse the current node's pointer
    prev = current  // Move prev one step ahead
    current = next  // Move current one step ahead

  L.head = prev  // Update the head to the new first element
  return true
