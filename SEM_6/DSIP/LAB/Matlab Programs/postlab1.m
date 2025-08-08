even_numbers = 32:2:74; 
disp('Even numbers between 31 and 75:');
disp(even_numbers);

x = [2, 5, 1, 6];
x_plus_16 = x + 16;
disp('x + 16:');
disp(x_plus_16);

x_odd_index_plus_3 = x;
x_odd_index_plus_3(1:2:end) = x_odd_index_plus_3(1:2:end) + 3;
disp('Add 3 to odd-index elements:');
disp(x_odd_index_plus_3);

x_sqrt = sqrt(x);
disp('Square root of each element:');
disp(x_sqrt);

x_squared = x.^2;
disp('Square of each element:');
disp(x_squared);

x = [3; 2; 6; 8]; 
y = [4; 1; 3; 5]; 

y_sum_added = y + sum(x);
disp('y + sum(x):');
disp(y_sum_added);

x_powered = x .^ y;
disp('x raised to the power of corresponding elements in y:');
disp(x_powered);

y_divided_by_x = y ./ x;
disp('y divided by corresponding elements in x:');
disp(y_divided_by_x);

z = x .* y;
disp('Element-wise multiplication of x and y (z):');
disp(z);

w = sum(z);
disp('Sum of elements in z (w):');
disp(w);

result = (x' * y) - w;
disp('Result of (x'' * y) - w:');
disp(result);
fprintf('Interpretation: This value indicates how much extra value is contributed by direct multiplication compared to their combined linear interaction.\n');

n = 1:100; 
x = ((-1).^(n+1)) ./ (2*n - 1); 
sum_x = sum(x); 
disp('Sum of first 100 elements of xn:');
disp(sum_x);

A = [2, 4, 1; 
     6, 7, 2; 
     3, 5, 9];

x1 = A(1, :); 
disp('First row of A (x1):');
disp(x1);

y = A(2:end, :);
disp('Last two rows of A (y):');
disp(y);

column_sum = sum(A);
disp('Sum over columns of A:');
disp(column_sum);

row_sum = sum(A, 2); 
disp('Sum over rows of A:');
disp(row_sum);

sem_column = std(A) ./ sqrt(size(A, 1)); 
disp('Standard error of mean for each column of A:');
disp(sem_column);
