% Read the image
img = imread('parrot.bmp');
if size(img, 3) == 3
    % Convert to grayscale if it's RGB
    img = rgb2gray(img);
end

% Get the dimensions of the image
[M, N] = size(img);

% Part 1: Forced Histogram

% Given pixel counts for each intensity level
forced_counts = [50; 100; 100; 50; 200; 100; 300; 100];

% Define original gray levels
original_gray_levels = (0:7)';

% Calculate total pixels and PDF
total_forced = sum(forced_counts);
forced_pdf = forced_counts / total_forced;

% Calculate CDF
forced_cdf = zeros(8,1);
forced_cdf(1) = forced_pdf(1);
for i = 2:8
    forced_cdf(i) = forced_cdf(i-1) + forced_pdf(i);
end

% Scale CDF and define new gray levels
forced_cdf_scaled = round(forced_cdf * 7);
forced_new_gray = forced_cdf_scaled;

% Create table for forced histogram processing
Table1_forced = table( ...
    original_gray_levels, ...
    forced_counts, ...
    forced_pdf, ...
    forced_cdf, ...
    forced_cdf_scaled, ...
    forced_new_gray, ...
    'VariableNames', ...
    {'OriginalGrayLevel', 'PixelsPerIntensity', 'pdf', 'cdf', 'cdfTimes7', 'NewGrayLevel'} ...
);

% Display table
fprintf('Table 1 Histogram processing numerical\n');
disp(Table1_forced);

% Calculate new pixel intensity distribution
forced_new_pixel_intensity = zeros(8,1);
for val = 1:8
    forced_new_pixel_intensity(val) = sum(forced_counts(forced_new_gray == (val - 1)));
end

% Create table for new pixel intensity distribution
Table2_forced = table( ...
    original_gray_levels, ...
    forced_new_pixel_intensity, ...
    'VariableNames', ...
    {'GrayLevel', 'PixelsPerIntensity'} ...
);

% Display table
fprintf('Table 2 New Pixel Intensity Dist\n');
disp(Table2_forced);

% Part 2: Histogram Equalization

% Initialize histogram counts
hist_counts = zeros(256, 1);

% Count pixel intensities in the original image
for i = 1:M
    for j = 1:N
        intensity = img(i, j) + 1;
        hist_counts(intensity) = hist_counts(intensity) + 1;
    end
end

% Calculate PDF and CDF
pdf = hist_counts / (M * N);
cdf_val = cumsum(pdf);

% Scale CDF to get new gray levels
scaled_cdf = round(cdf_val * 255);
new_gray_levels = scaled_cdf;

% Apply histogram equalization
output_img = img;
for i = 1:M
    for j = 1:N
        old_intensity = img(i, j) + 1;
        output_img(i, j) = new_gray_levels(old_intensity);
    end
end

% Count pixel intensities in the equalized image
hist_eq_counts = zeros(256,1);
for i = 1:M
    for j = 1:N
        eq_intensity = output_img(i, j) + 1;
        hist_eq_counts(eq_intensity) = hist_eq_counts(eq_intensity) + 1;
    end
end

% Display images and histograms
figure;
subplot(2,2,1); 
imshow(img); 
title('Original Image');

subplot(2,2,2); 
imshow(output_img); 
title('Histogram Equalized Image');

subplot(2,2,3);
bar(0:255, hist_counts, 1, 'FaceColor','b','EdgeColor','none');
xlabel('Gray level');
ylabel('Pixel Count / gray level');
title('Histogram of Original Image');

subplot(2,2,4);
bar(0:255, hist_eq_counts, 1, 'FaceColor','b','EdgeColor','none');
xlabel('Gray level');
ylabel('Pixel Count / gray level');
title('Histogram of Equalized Image');
