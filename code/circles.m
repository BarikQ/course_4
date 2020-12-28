height = 752;
width = 480;
matrix_height = 0;
gamma = 0;
fi = 0;

[columns, rows] = meshgrid(1:width, 1:height);
centerX = width / 2;
centerY = height / 2;
radX = 100;
radY = 100;
pixels = (rows - centerY).^2 ./ radY^2 ...
    + (columns - centerX).^2 ./ radX^2 <= 1;

image(pixels);
colormap([0 0 0; 1 1 1]);

image = zeros(height, width, 3); %initialize
image(50:342, 100:380, 1) = 0.5;   %Red (dark red)
 
figure, imshow(image)