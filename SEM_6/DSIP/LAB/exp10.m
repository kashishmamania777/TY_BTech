clc; clear; close all;

% Read image
img = imread('parrot.bmp');
if size(img, 3) == 3
    img = 0.2989 * img(:, :, 1) + 0.5870 * img(:, :, 2) + 0.1140 * img(:, :, 3);
end
img = double(img);

[rows, cols] = size(img);

% Padding
padded_img = zeros(rows + 2, cols + 2);
padded_img(2:end-1, 2:end-1) = img;
padded_img(1, 2:end-1) = img(1, :);
padded_img(end, 2:end-1) = img(end, :);
padded_img(2:end-1, 1) = img(:, 1);
padded_img(2:end-1, end) = img(:, end);
padded_img(1, 1) = img(1, 1);
padded_img(1, end) = img(1, end);
padded_img(end, 1) = img(end, 1);
padded_img(end, end) = img(end, end);

% Masks
sobel_x = [-1 0 1; -2 0 2; -1 0 1];
sobel_y = [-1 -2 -1; 0 0 0; 1 2 1];
roberts_x = [1 0; 0 -1];
roberts_y = [0 1; -1 0];

% Initialize
grad_x = zeros(rows, cols);
grad_y = zeros(rows, cols);
grad_mag = zeros(rows, cols);
roberts_grad_x = zeros(rows, cols);
roberts_grad_y = zeros(rows, cols);
roberts_mag = zeros(rows, cols);
roberts_theta = zeros(rows, cols);

% Sobel Operator
for i = 2:rows+1
    for j = 2:cols+1
        region = padded_img(i-1:i+1, j-1:j+1);
        sum_x = 0;
        sum_y = 0;
        for m = 1:3
            for n = 1:3
                sum_x = sum_x + region(m, n) * sobel_x(m, n);
                sum_y = sum_y + region(m, n) * sobel_y(m, n);
            end
        end
        grad_x(i-1, j-1) = sum_x;
        grad_y(i-1, j-1) = sum_y;
    end
end

% Roberts Operator
for i = 1:rows-1
    for j = 1:cols-1
        roberts_grad_x(i, j) = img(i, j) * roberts_x(1,1) + img(i, j+1) * roberts_x(1,2) + ...
                               img(i+1, j) * roberts_x(2,1) + img(i+1, j+1) * roberts_x(2,2);
        roberts_grad_y(i, j) = img(i, j) * roberts_y(1,1) + img(i, j+1) * roberts_y(1,2) + ...
                               img(i+1, j) * roberts_y(2,1) + img(i+1, j+1) * roberts_y(2,2);
    end
end

% Gradient Magnitude and Direction
for i = 1:rows
    for j = 1:cols
        grad_mag(i, j) = sqrt(grad_x(i, j)^2 + grad_y(i, j)^2);
        roberts_mag(i, j) = abs(roberts_grad_x(i, j)) + abs(roberts_grad_y(i, j));
        roberts_theta(i, j) = atan(roberts_grad_y(i, j) / roberts_grad_x(i, j)) - (3 * pi / 4);
    end
end

% Normalize
max_val = max(grad_mag(:));
max_val_roberts = max(roberts_mag(:));
for i = 1:rows
    for j = 1:cols
        grad_mag(i, j) = (grad_mag(i, j) / max_val) * 255;
        roberts_mag(i, j) = (roberts_mag(i, j) / max_val_roberts) * 255;
    end
end

% Convert to uint8
grad_mag = uint8(grad_mag);
roberts_mag = uint8(roberts_mag);
grad_x = uint8(abs(grad_x));
roberts_grad_x = uint8(abs(roberts_grad_x));

% Display
figure;
subplot(2, 3, 1);
imshow(uint8(img)), title('Original Image');
subplot(2, 3, 2);
imshow(grad_x), title('Sobel X');
subplot(2, 3, 3);
imshow(grad_mag), title('Sobel Gradient Magnitude');
subplot(2, 3, 4);
imshow(roberts_grad_x), title('Roberts X');
subplot(2, 3, 5);
imshow(uint8(abs(roberts_grad_y))), title('Roberts Y');
subplot(2, 3, 6);
imshow(roberts_mag), title('Roberts Gradient Magnitude');
