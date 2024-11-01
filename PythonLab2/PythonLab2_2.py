def MultiTool(anything):
    anythingType = type(anything)
    isinstance(anything,int)
    if anythingType == int:
        while anything > 0:
            print(anything%10,end = '')
            anything = int(anything/10)
        print('')

    elif anythingType == str:
        summ = 0
        for ch in anything:
            if ch.isdigit():
                summ += int(ch)
      
        if summ != 0 : print(summ)
    elif anythingType == list:
        for item in anything:
            if type(item) == str:
                count = 0
                for ch in item:
                    count += 1
                print(item + ' - ' + str(count) + ' letters')
    
    elif anythingType == tuple:
        numbers = 0
        characters = 0
        for item in anything:
            if type(item) == int or type(item) == float or type(item) == complex:
                numbers += 1
            elif type(item) == str:
                for ch in item:
                    characters += 1
        print('Numbers count: ' + str(numbers) + ' Characters: ' + str(characters))

MultiTool(52)
MultiTool("wasd123")
MultiTool([123,"asda", "wegadvsdg", "bebebe"])
MultiTool(("qweqw",123))