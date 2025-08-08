n = -10:10;

u = @(n) double(n >= 0);

x = @(n) 8*(0.5).^n .* (u(n+1) - u(n-3));

x_n = x(n);

Y_n = x(n - 3);

F_n = x(n + 1);

G_n = x(-n + 4);

figure;

subplot(4, 1, 1);
stem(n, x_n, 'filled');
title('Original Signal x(n)');
xlabel('n');
ylabel('Amplitude');

subplot(4, 1, 2);
stem(n, Y_n, 'filled');
title('Y(n) = x[n-3] (Right Shift by 3)');
xlabel('n');
ylabel('Amplitude');

subplot(4, 1, 3);
stem(n, F_n, 'filled');
title('F(n) = x[n+1] (Left Shift by 1)');
xlabel('n');
ylabel('Amplitude');

subplot(4, 1, 4);
stem(n, G_n, 'filled');
title('G(n) = x[-n+4] (Time Reversal and Right Shift by 4)');
xlabel('n');
ylabel('Amplitude');
