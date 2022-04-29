time_sec = int(input('insert time in second:  '))
hours = time_sec // 3600
minutes = (time_sec - hours * 3600) // 60
seconds = (time_sec - hours * 3600 - minutes * 60)
print(f"{hours}:{minutes}:{seconds}")


