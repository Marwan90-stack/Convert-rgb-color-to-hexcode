my_colors = {rgb(220, 50, 90) : "#DC325A"}

def rgb2hex(r, g, b):
    """ 
    Function to convert rgb color to hex code.
    Specify r, g, and b using integer numbers, ranging from 0 to 255.
    For example, red is specified with rgb(255, 0, 0) in rgb and converted to hex code as #FF0000.
    """
    for i in [r, b, b]:
        if not isinstance(i, int):
            raise Exception("`r`, `g` and `b` must be integers.")
    for i in [r, g, b]:
        if i < 0 or i > 255:
            raise Exception("`r`, `g` and `b` must range from 0 to 255.")
    red = ""
    green = ""
    blue = ""

    # Specify red components:
    if r < 10:
        red = red + str(0) + str(r)
    elif r < 16:
        match r:
            case 10:
                r = "A"
            case 11:
                r = "B"
            case 12:
                r = "C"
            case 13:
                r = "D"
            case 14:
                r = "E"
            case 15:
                r = "F"
        red = red + str(0) + r
    else:
        red1 = r // 16
        red2 = r % 16

        if red1 >= 10 and red1 <= 15:
            match red1:
                case 10:
                    red1 = "A"
                case 11:
                    red1 = "B"
                case 12:
                    red1 = "C"
                case 13:
                    red1 = "D"
                case 14:
                    red1 = "E"
                case 15:
                    red1 = "F"
        if red2 >= 10 and red2 <=15:
            match red2:
                case 10:
                    red2 = "A"
                case 11:
                    red2 = "B"
                case 12:
                    red2 = "C"
                case 13:
                    red2 = "D"
                case 14:
                    red2 = "E"
                case 15:
                    red2 = "F"
        red = red + str(red1) + str(red2)

    # Speficy green component:
    
    if g < 10:
        green = green + str(0) + str(g)
    elif g < 16:
        match g:
            case 10:
                g = "A"
            case 11:
                g = "B"
            case 12:
                g = "C"
            case 13:
                g = "D"
            case 14:
                g = "E"
            case 15:
                g = "F"
        green = green + str(0) + g
    else:
        green1 = g // 16
        green2 = g % 16

        if green1 >= 10 and green1 <= 15:
            match green1:
                case 10:
                    green1 = "A"
                case 11:
                    green1 = "B"
                case 12:
                    green1 = "C"
                case 13:
                    green1 = "D"
                case 14:
                    green1 = "E"
                case 15:
                    green1 = "F"
        if green2 >= 10 and green2 <= 15:
            match green2:
                case 10:
                    green2 =  "A"
                case 11:
                    green2 = "B"
                case 12:
                    green2 = "C"
                case 13:
                    green2 = "D"
                case 14:
                    green2 = "E"
                case 15:
                    green2 = "F"
        green = green + str(green1) + str(green2)
    
    # Specify blue component:
    if b < 10:
        blue = blue + str(0) + str(b)
    elif b < 16:
        match b:
            case 10:
                b =  "A"
            case 11:
                b = "B"
            case 12:
                b = "C"
            case 13:
                b = "D"
            case 14:
                b = "E"
            case 15:
                b = "F"
        blue = blue + str(0) + b
    else:
        blue1 = b // 16
        blue2 = b % 16

        if blue1 >= 10 and blue1 <= 15:
            match blue1:
                case 10:
                    blue1 = "A"
                case 11:
                    blue1 = "B"
                case 12:
                    blue1 = "C"
                case 13:
                    blue1 = "D"
                case 14:
                    blue1 = "E"
                case 15:
                    blue1 = "F"
        if blue2 >= 10 and blue2 <= 15:
            match blue2:
                case 10:
                    blue2 = "A"
                case 11:
                    blue2 = "B"
                case 12:
                    blue2 = "C"
                case 13:
                    blue2 = "D"
                case 14:
                    blue2 = "E"
                case 15:
                    blue2 = "F"
        blue = blue + str(blue1) + str(blue2)

    return "#"+red+green+blue
