def find(list, item, low=0, high=None):
    if high == None:
        high = len(list) - 1
    if low > high:
        return False
    mid = int(low + ((high - low / 2)))
    # print(f"low: {low} high: {high} mid: {mid}")
    if item == list[mid]:
        return True
    elif item < list[mid]:
        high = mid - 1
    elif item > list[mid]:
        low = mid + 1
    return find(list, item, low, high)


list = [2, 5, 8, 9]
print("these should all be false:")
print(find(list, 3))
print(find(list, -2))
print(find(list, 11))
print(find(list, 7))

print("these should all be true:")
print(find(list, 2))
print(find(list, 5))
print(find(list, 8))
print(find(list, 9))
