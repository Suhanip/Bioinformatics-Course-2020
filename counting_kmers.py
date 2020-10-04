def patternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)):
        if(Text[i:i+len(Pattern)] == Pattern):
            count = count+1
    return count


result = patternCount('CGATATATCCATAG', 'ATAT')

print(result)