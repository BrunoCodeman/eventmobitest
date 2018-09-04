directions = {"N":1, "E": 2, "S": 3, "W": 4}                   
turns=[(0,1),(1,0),(0,-1),(-1,0)] 

def turn_left(x: int, y: int, direction: str) -> float:
    coord = direction - 1 + 4
    return x, y, coord % 4

def turn_right(x: int, y:int , direction: str) -> float:
    coord = direction + 1
    return x, y, coord % 4

def move(x: int, y: int, direction: str) -> float:
    return x + turns[direction][0], y + turns[direction][1], direction - 1

movements = {"r": turn_right, "l": turn_left, "m": move}

def main():
    try:
        upper_right = input()
        while True:
            params = input().split(" ") 
            x, y, direction = (int(params[0]), int(params[1]), directions[params[2].upper()])
            instructions = input().lower() 
            for i in instructions: 
                x, y, direction = movements[i](x, y, direction)
            print("{0} {1} {2}".format(x, y, params[2]))
    except Exception as ex:
        print(str(ex))
    
    

if __name__ == '__main__':
    main()
