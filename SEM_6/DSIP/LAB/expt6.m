A = imread('C:\Users\kashi\OneDrive\Desktop\KJSCE\BTech\SEM VI\DSIP\LAB\parrot.bmp');
if size(A, 3) == 3
    A = rgb2gray(A);
end
A = double(A);

r1 = input('Enter the value for r1 (lower input range): ');
s1 = input('Enter the value for s1 (lower output range): ');
r2 = input('Enter the value for r2 (upper input range): ');
s2 = input('Enter the value for s2 (upper output range): ');

L = 256;

B = zeros(size(A), 'uint8');

% Contrast stretching parameters
alpha = s1 / r1;
beta = (s2 - s1) / (r2 - r1);
gamma = ((L - 1) - s2) / ((L - 1) - r2);

for i = 1:size(A, 1)
    for j = 1:size(A, 2)
        r = A(i, j);
        if r < r1
            B(i, j) = alpha * r;
        elseif r1 <= r && r <= r2
            B(i, j) = s1 + beta * (r - r1);
        else
            B(i, j) = s2 + gamma * (r - r2);
        end
    end
end

figure;

%Original Image
subplot(1, 2, 1);
imshow(uint8(A));
title('Original Image');

%Contrast Streched image
subplot(1, 2, 2);
imshow(B);
title(sprintf('Contrast Stretched\n(α=%.2f, β=%.2f, γ=%.2f)\n (r1=%.2f,r2=%.2f,s1=%.2f,s2=%.2f)', alpha, beta, gamma, r1,r2,s1,s2));