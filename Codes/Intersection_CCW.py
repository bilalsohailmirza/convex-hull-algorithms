import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
line1 = []
line2 = []

def in_between(a,b,c):
   return ((b[0] <= max(a[0], c[0])) and (b[0] >= min(a[0], c[0])) and (b[1] <= max(a[1], c[1])) and (b[1] >= min(a[1], c[1])))

def CCW (x1,y1,x2,y2,x3,y3):
  area = (x1*y2) - (x1*y3) - (y1*x2) + (y1*x3) + (x2*y3) - (y2*x3)
  if area < 0:
    return -1
  elif area > 0:
    return 1
  else:
    return 0

def ccw_intersection(line1,line2):
    test1 = CCW(line1[0][0],line1[0][1], line1[1][0],line1[1][1], line2[0][0],line2[0][1])  
    test2 = CCW(line1[0][0],line1[0][1], line1[1][0],line1[1][1], line2[1][0],line2[1][1])
    test3 = CCW(line2[0][0],line2[0][1], line2[1][0],line2[1][1], line1[0][0],line1[0][1]) 
    test4 = CCW(line2[0][0],line2[0][1], line2[1][0],line2[1][1], line1[1][0],line1[1][1])
    
    if (test1 != test2) and (test3 != test4):
       return 1
    elif (test1 == 0 and in_between(line1[0], line2[0], line1[1])): 
        return 1 
    elif ((test2 == 0) and in_between(line1[0], line2[1], line1[1])): 
        return 1 
    elif ((test3 == 0) and in_between(line2[0], line1[0], line2[1])): 
        return 1
    elif (test4 == 0 and in_between(line2[0], line1[1], line2[1])):
        return 1
    else :
       return 0
    
def draw_point(x, y):
    ax.scatter(x, y, color='red')
    fig.canvas.draw()

def on_click(event):
    x, y = event.xdata, event.ydata
    if x is not None and y is not None:
        if len(line1) < 2:
            line1.append((x, y))
            # print(f"Clicked at: ({x}, {y}) for line1")
        elif len(line2) < 2:
            line2.append((x, y))
            # print(f"Clicked at: ({x}, {y}) for line2")

        draw_point(x, y)

        if len(line1) == 2:
            draw_line_segment(line1,'yellow')

        if len(line1) == 2 and len(line2) == 2:
            draw_line_segment(line2,'green')
            fig.canvas.mpl_disconnect(cid)
            if (ccw_intersection(line1,line2)):
                print('Entered lines are intersecting')
            else:
                print('Entered lines are not intersecting')

def draw_line_segment(line,setColor):
    line_segment = Line2D(*zip(line[0], line[1]), color = setColor)
    ax.add_line(line_segment)
    fig.canvas.draw()


if __name__ == '__main__':
    cid = fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
    