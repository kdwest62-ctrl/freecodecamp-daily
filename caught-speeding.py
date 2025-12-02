def speeding(speeds, limit):
	def vehicles(s, l):
		count = 0
        for item in s:
            if item > l:
                count += 1
        return count
    def average(s, l):
        list1 = []
        list2 = []
        for element in s:
            if element > l:
                list1.append(element)
        for element in list1:
            over_speed = element - l
            list2.append(over_speed)
        return sum(list2) / len(list2)
    if vehicles(speeds, limit) == 0:
        return [0, 0]
    else:
        return f"[{vehicles(speeds, limit)}, {average(speeds, limit)}]"
