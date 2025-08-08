% RLE Compression and Decompression for Binary Images
clc; clear; close all;

%% Compression
input_image = 'picture.bmp';
output_bin = 'compressed.bin';
output_txt = 'compressed.txt';

% Read and binarize image
img = imread(input_image);
if size(img, 3) > 1
    img = rgb2gray(img);
end
threshold = graythresh(img);         % Automatic thresholding
img_binary = imbinarize(img, threshold);

% Convert to 1D vector (column-wise)
img_vector = img_binary(:);

% Run-Length Encoding
values = [];
counts = [];
current_val = img_vector(1);
current_count = 1;

for i = 2:length(img_vector)
    if img_vector(i) == current_val && current_count < 255
        current_count = current_count + 1;
    else
        values = [values; current_val];
        counts = [counts; current_count];
        current_val = img_vector(i);
        current_count = 1;
    end
end
% Add last run
values = [values; current_val];
counts = [counts; current_count];

% Save to binary file (1 byte value, 1 byte count)
fid = fopen(output_bin, 'wb');
for i = 1:length(values)
    fwrite(fid, values(i), 'uint8');
    fwrite(fid, counts(i), 'uint8');
end
fclose(fid);

% Save to text file for verification
fid = fopen(output_txt, 'w');
fprintf(fid, '%d %d\n', [values'; counts']);
fclose(fid);

% Calculate compression metrics
original_size = numel(img_binary);
compressed_size = length(values) * 2; % 2 bytes per run
CR = original_size / compressed_size;
RD = 1 - (1/CR);

fprintf('Compression Ratio (CR): %.2f\n', CR);
fprintf('Redundancy (RD): %.2f\n', RD);

%% Decompression
output_image = 'decompressed.bmp';
image_size = size(img_binary);

% Read binary compressed file
fid = fopen(output_bin, 'rb');
data = fread(fid, [2, Inf], 'uint8');
fclose(fid);

% Reconstruct image vector
reconstructed = [];
for i = 1:size(data,2)
    reconstructed = [reconstructed; repmat(data(1,i), data(2,i), 1)];
end

% Reshape and save
img_reconstructed = reshape(reconstructed, image_size);
imwrite(img_reconstructed, output_image);

%% Verification
subplot(1,2,1), imshow(img_binary), title('Original Binary Image')
subplot(1,2,2), imshow(img_reconstructed), title('Decompressed Image')
