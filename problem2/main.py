def draw_xyz(N):
    pattern = ""
    k=1
    for i in range (1,N+1):
        for j in range (1,N+1):
            if k%3==0:
                pattern+= 'X '
            elif k%2==0:
                pattern+= 'Z '
            else:
                pattern+= 'Y '
            k+=1
        pattern +='\n'
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """