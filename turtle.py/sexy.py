# Importing modules.
import turtle as t;

# Define an class Draw
class Draw:
    def __init__(self:object):
        self.t = t;
        pass;
    def dick(self:object):
        self.t.color("White");
        self.t.goto(-200, -200);
        self.t.color('brown');
        self.t.circle(50);
        self.t.color("White");
        self.t.goto(-100, -200);
        self.t.color('brown');
        self.t.circle(50);
        self.t.color("white");
        self.t.goto(-100, -100);
        self.t.color("black");
        self.t.left(90);
        self.t.fd(200);
        self.t.color("red");
        self.t.right(90);
        self.t.fd(5);
        self.t.left(90);
        self.t.circle(55,180);
        self.t.left(90);
        self.t.fd(105);
        self.t.bk(50);
        self.t.color('white');
        self.t.left(90);
        self.t.fd(30);
        self.t.color('red');
        self.t.fd(25);
        self.t.color('white');
        self.t.goto(-200,100);
        self.t.color('black');
        self.t.right(90);
        self.t.goto(-200,-106);
        pass;
    def butt(self:object):
        self.t.color("white");
        self.t.goto(-150,200);
        self.t.color("black");
        self.t.right(90);
        self.t.circle(50, 180);
        self.t.color("white");
        self.t.goto(-250,200);
        self.t.color("black");
        self.t.left(180);
        self.t.circle(50, 180);
        self.t.fd(10);
        self.t.fd(-20);
        pass;
    pass;
if __name__ == "__main__":
    d = Draw();
    pass;
