t = -10:0.5:10;

signal1 = sin(t);
signal2 = 0.5 * cos(t);

addition_result = signal1 + signal2;

subtraction_result = signal1 - signal2;

multiplication_result = signal1 .* signal2;

upscaling_factor = 2;
downscaling_factor = 0.5;

upscaled_signal = upscaling_factor * signal1;
downscaled_signal = downscaling_factor * signal1;

shift_amount = 2;

advanced_signal = circshift(signal1, shift_amount);
delayed_signal = circshift(signal1, -shift_amount);

folded_signal = fliplr(signal1);
subplot(3, 3, 1);
plot(t, signal1);
title('Signal 1');

subplot(3, 3, 2);
plot(t, signal2);
title('Signal 2');

subplot(3, 3, 3);
plot(t, addition_result);
title('Addition');

subplot(3, 3, 4);
plot(t, subtraction_result);
title('Subtraction');

subplot(3, 3, 5);
plot(t, multiplication_result);
title('Multiplication');

subplot(3, 3, 6);
plot(t, upscaled_signal);
title('Upscaling');

subplot(3, 3, 7);
plot(t, downscaled_signal);
title('Downscaling');

subplot(3, 3, 8);
plot(t, advanced_signal);
title('Advance/Right Shift');

subplot(3, 3, 9);
plot(t, delayed_signal);
title('Delay/Left Shift');
