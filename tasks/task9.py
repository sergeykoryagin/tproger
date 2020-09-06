def convert(seconds):
    minutes, seconds = seconds // 60, seconds % 60
    hours, minutes = minutes // 60, minutes % 60
    days, hours = hours // 24, hours % 24
    return (days, hours, minutes, seconds)

res  = convert(100000)

print(res)