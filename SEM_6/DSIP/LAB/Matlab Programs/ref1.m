a=3;
disp(a);
A=[1 2;0 3];
disp(A);
x=3*sin(a);
disp(x);
B=[1 2 3; 4 5 6];
disp(B);
B(:,2)=[];
disp(B);
C=[1 2;3 4];
D=4;
which -all C
which -all D
which -all E
y=2e6;
disp(y);
z=3.8e-4;
disp(z);
F=[1 0 5;2 1 6;3 4 0];
disp(rank(F));
disp(det(F));
disp(inv(F));
disp(diag(F));
disp(ones(3));
disp(eye(3));

figure(1);
t=-2*pi:0.1*pi:2*pi;
z=t.*sin(t);
plot(t,z);
title('Plot of tsin(t) vs t');
xlabel('t');
ylabel('z');
grid on

figure(2);
x=0:pi/10:2*pi;
[X,Y,Z]=cylinder(4*cos(x));
subplot(2,2,1); mesh(X)
subplot(2,2,2); mesh(Y)
subplot(2,2,3); mesh(Z)
subplot(2,2,4); mesh(X,Y,Z)







a=6;
b=5;
if(a>b)
   disp('a is greater than b');
elseif(b>a)
   disp('b is greater tha a');
else
   disp('a is equal to b');
end
c=5;
for C=1:c
disp(C);
end
d=0;
while d<3
   d=d+1;
   disp(d);
end
