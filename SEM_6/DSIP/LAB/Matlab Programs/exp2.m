% Define the discrete time vector
n = 0:20; % Discrete time from 0 to 20

% Create a new figure
figure;

% Unit Step Signal
subplot(3, 2, 1);
u = (n >= 0);
stem(n, u);
title('Unit Step Signal');
xlabel('n');
ylabel('u[n]');
grid on;

% Unit Impulse Signal
subplot(3, 2, 2);
delta = [1, zeros(1, 20)];
stem(n, delta);
title('Unit Impulse Signal');
xlabel('n');
ylabel('δ[n]');
grid on;

% Ramp Signal
subplot(3, 2, 3);
ramp = n;
stem(n, ramp);
title('Ramp Signal');
xlabel('n');
ylabel('r[n]');
grid on;

% Exponential Signal
subplot(3, 2, 4);
a = 0.9;
x_exp = a.^n;
stem(n, x_exp);
title('Exponential Signal');
xlabel('n');
ylabel('x[n]');
grid on;

% Sine Signal
subplot(3, 2, 5);
f_sin = 0.1;
x_sin = sin(2 * pi * f_sin * n);
stem(n, x_sin);
title('Discrete-Time Sine Signal');
xlabel('n');
ylabel('x[n]');
grid on;

% Cosine Signal
subplot(3, 2, 6);
f_cos = 0.1;
x_cos = cos(2 * pi * f_cos * n);
stem(n, x_cos);
title('Discrete-Time Cosine Signal');
xlabel('n');
ylabel('x[n]');
grid on;
