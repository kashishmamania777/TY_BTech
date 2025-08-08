% MATLAB code for Low-pass, High-pass, and Median Filtering

% Read input image
img = imread('input_image.jpg');

% Convert to grayscale if image is RGB
if size(img,3) == 3
    img_gray = rgb2gray(img);
else
    img_gray = img;
end

% --- Low-Pass Filtering (Mean Filter) ---
lp_kernel = fspecial('average', [3 3]);
lowpass_img = imfilter(img_gray, lp_kernel, 'replicate');

% --- High-Pass Filtering (Edge Enhancement) ---
hp_kernel = [-1 -1 -1; -1 8 -1; -1 -1 -1];
highpass_img = imfilter(double(img_gray), hp_kernel, 'replicate');
highpass_img = uint8(mat2gray(highpass_img)*255);

% --- Median Filtering (Noise Reduction) ---
median_img = medfilt2(img_gray, [3 3]);

% --- Display Results ---
figure;

subplot(2,2,1);
imshow(img_gray);
title('Original Image');

subplot(2,2,2);
imshow(lowpass_img);
title('Low-pass Filtered Image');

subplot(2,2,3);
imshow(highpass_img);
title('High-pass Filtered Image');

subplot(2,2,4);
imshow(median_img);
title('Median Filtered Image');
