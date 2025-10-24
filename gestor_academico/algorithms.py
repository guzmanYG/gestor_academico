def quicksort_students(students, key_fn):
    """Ordena lista de objetos usando Quicksort por la clave proporcionada (descendente)."""
    if len(students) <= 1:
        return students[:]
    pivot = students[len(students) // 2]
    pivot_key = key_fn(pivot)
    left = [x for x in students if key_fn(x) > pivot_key]
    middle = [x for x in students if key_fn(x) == pivot_key]
    right = [x for x in students if key_fn(x) < pivot_key]
    return quicksort_students(left, key_fn) + middle + quicksort_students(right, key_fn)

def binary_search_by_matricula(sorted_students, matricula):
    low, high = 0, len(sorted_students) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_key = sorted_students[mid].matricula
        if mid_key == matricula:
            return sorted_students[mid]
        if matricula < mid_key:
            high = mid - 1
        else:
            low = mid + 1
    return None
