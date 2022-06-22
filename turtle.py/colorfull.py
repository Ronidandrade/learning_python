# Importing all needed modules.
import turtle as t;
from random import randint;

class Draw:
    def __init__(self:object):
        self.t = t;
        pass;
    def turtleColor(self:object):
        '''Convert the RGB color to hexadecimal collors'''
        r,g,b = randint( 0, 255), randint( 0, 255), randint( 0, 255);
        R1, R2, B1, B2, G1, G2 =r // 16, r % 16, b // 16, b % 16, g // 16, g % 16;
        T = { 0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'a', 11 : 'b', 12 : 'c', 13 : 'd', 14 : 'e', 15 : 'f' };
        return '#' + T[R1]+T[R2]+T[G1]+T[G2]+T[B1]+T[B2]
    def drawingPolygon(self:object, n_faces:int = 6, size_face:int = 50):
        for i in range(n_faces + 1):
            self.t.fd(size_face);
            self.t.lt(360/n_faces);
            pass;
        pass;
    def drawingArt(self:object, limit: int = 700):
        i = 0;
        while True:
            self.t.speed("fastest");
            self.t.color(self.turtleColor());
            self.t.fd(100-i);
            self.t.lt(59);
            i += 1;
            limit -= 1
            if limit < 0:
                self.t.color("white");
                break;
            pass;
        pass;
    def drawingHeart(self:object, limit: int = 5):
        i = 1;
        self.t.speed("fastest");
        while True:
            self.t.pensize(6);
            self.t.color(self.turtleColor());
            self.t.lt(135);
            self.t.circle(30*i,180);
            self.t.fd(60*i);
            self.t.lt(90);
            self.t.fd(60*i);
            self.t.circle(30*i,180);
            self.t.rt(135);
            self.t.pu();
            self.t.fd(30+i);
            self.t.pd();
            self.t.rt(90);
            i += 1;
            limit -= 1;
            if limit < 0:
                self.t.color("white");
                break;
            pass;
        pass;
    pass;
if __name__ == "__main__":
    d = Draw();
    #d.drawingPolygon();
    pass;
