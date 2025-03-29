
def barr(x,y,COL):
    if y%2:
        return COL*(y+1)-1-x
    return COL*y+x 