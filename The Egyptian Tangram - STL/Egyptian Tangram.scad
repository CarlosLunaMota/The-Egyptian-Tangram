H =  3;
X = 25;
Y = X-10-(X%10);


T1 = [[0.0*X,6.0*X], [2.0*X,6.0*X], [2.0*X,5.0*X]];
T4 = [[4.0*X,0.0*X], [6.0*X,0.0*X], [6.0*X,4.0*X]];
T5 = [[4.5*X,3.0*X], [3.5*X,1.0*X], [0.5*X,5.0*X]];
T6 = [[0.0*X,0.0*X], [3.0*X,0.0*X], [0.0*X,4.0*X]];
Q4 = [[3.0*X,6.0*X], [3.0*X,5.0*X], [5.0*X,4.0*X], [6.0*X,6.0*X]];


color("red")    translate([-0.0*Y,-2*Y,0]) linear_extrude(H) polygon(T1);
color("blue")   translate([-1.0*Y,-0*Y,0]) linear_extrude(H) polygon(T4);
color("green")  translate([-0.5*Y,-1*Y,0]) linear_extrude(H) polygon(T5);
color("orange") translate([-1.0*Y,-2*Y,0]) linear_extrude(H) polygon(Q4);
difference() {
    color("yellow") translate([-0.0*Y,-0*Y,0]) linear_extrude(H) polygon(T6);
    translate([2.95,2.55,H-0.5]) scale([0.1,0.1,1]) linear_extrude(2) import("Logo_Vertical.svg");
}