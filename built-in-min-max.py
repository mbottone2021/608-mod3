
def maximum(value1, value2, value3):
    """Return the maximun of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value
value1 = 12
value2 = 27
value3 = 36
print(maximum(value1, value2, value3))
print(max(value1, value2, value3))
36
36
def minimum(value1, value2, value3, value4):
    """Return the minimum of four values"""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4
    return min_value
value1 = 15
value2 = 9
value3 = 27
value4 = 14
print(minimum(value1, value2, value3, value4))
print(min(value1, value2, value3, value4))
9
9
