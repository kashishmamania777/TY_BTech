% IDFT Image Processing in MATLAB (Using fft2 for accuracy)

% Step 1: Input the size of the DFT matrix (must be a power of 2)
n = input('Enter the size of the DFT matrix (must be a power of 2): ');

% Check if the input size is a power of 2
if mod(log2(n), 1) ~= 0
    error('The size of the DFT matrix must be a power of 2.');
end

% Step 2: Generate and Display the DFT matrix
dft_matrix = zeros(n, n);
for k = 0:n-1
    for l = 0:n-1
        dft_matrix(k+1, l+1) = exp(-2 * pi * 1i * k * l / n);  % DFT formula
    end
end

disp('DFT Matrix:');
disp(dft_matrix);

% Step 3: Select and read the image
[filename, pathname] = uigetfile({'*.jpg;*.png;*.bmp;*.tif', 'Image Files (*.jpg, *.png, *.bmp, *.tif)'}, ...
                                 'Select an image');
if filename == 0
    error('No image selected. Please select an image.');
end

% Read the image and convert it to grayscale (if it is a color image)
image_path = fullfile(pathname, filename);
image = imread(image_path);
if size(image, 3) == 3
    image = rgb2gray(image);  % Convert to grayscale if the image is RGB
end

% Resize the image to fit the selected DFT size
image_resized = imresize(image, [n, n]);
image_double = double(image_resized);  % Convert to double for processing

% Step 4: Apply DFT using MATLAB’s fft2 function
dft_image = fft2(image_double);

% Step 5: Apply IDFT using MATLAB’s ifft2 function
idft_image = ifft2(dft_image);  % This should reconstruct the original image

% Step 6: Ensure real values and convert to uint8
idft_image = real(idft_image);  % Remove any small imaginary parts
idft_image_uint8 = uint8(idft_image);  % Convert back to uint8 (0-255)

% Step 7: Display the original, DFT magnitude, and IDFT images
figure;
subplot(1, 3, 1);
imshow(image_resized, []);
title('Original Image');

subplot(1, 3, 2);
imshow(log(1 + abs(dft_image)), []);
title('DFT Magnitude');

subplot(1, 3, 3);
imshow(idft_image_uint8, []);
title('Reconstructed Image (IDFT)');

% Save the IDFT image
output_filename = fullfile(pathname, 'IDFT_Image.png');
imwrite(idft_image_uint8, output_filename);
disp(['IDFT image saved as: ', output_filename]);
