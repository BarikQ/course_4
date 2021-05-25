close all;
clear all;
clc;

% параметры устройства
d = 0.0003;     % диаметр отверстия
t = 100e-6;     % толщина отверстия
h = 0.0007;     % высота отверстия

format long
% height = 4.51e-3;    % Размеры матрицы
% width = 2.88e-3;
height = 4e-3;
width = 4e-3;

pxW = 752;
pxH = 752;
pxSize = width / pxW;

angle = deg2rad(0 : 359);                      % вспомогательный массив углов
defCircleX = (d/2) * cos(angle);               % координата x контура пятна
defCircleY = (d/2) * sin(angle);               % координата y контура пятна
xPx = ceil((defCircleX + width/2) / pxSize);   % x - контур пятна в пикселях
yPx = ceil((defCircleY + height/2) / pxSize);  % y - контур пятна в пикселях
defPxRadius = ceil((max(xPx) - min(xPx)) / 2);

filename = './tables/compare_new.xlsx';

fileData = {"BruteFoce X", "BruteFoce Y", "Rand X", "Rand Y", "Breadth X", "Breadth Y"};
writecell(fileData, filename, 'sheet', 1, 'Range', "H1");

for iii = 1 : 500
    % чтение картинки и перевод в ч-б
    [image, colorMap] = imread(strcat("./images/circle_", num2str(iii), ".png"));
    imageGS = rgb2gray(image);
%     if (iii == 4) 
%         writematrix(imageGS, "file.txt");
%     end
    % figure, imshow(image);

    % figure, imshow(imageGS);

    [rows, columns, numberOfColorChannels] = size(image);

    x = 1:columns;
    y = 1:rows;

    imageProcessed = zeros(rows, columns, 3);

    %% поиск цветных пикселей перебором всех пикселей матрицы
    [bruteY, bruteX] = bruteForce(imageGS);

    [spotX, spotY] = randSpot(imageGS);
    %% поиск рандомом
    [randY, randX] = randPick(imageGS, spotX, spotY);
    
    %% breadth search
    [breadthY, breadthX] = breadthSearch(imageGS, spotX, spotY);
    
    fileData = {bruteY, bruteX, randY, randX, breadthY, breadthX};
    writecell(fileData, filename, 'sheet', 1, 'Range', strcat("H" + num2str(iii + 1) + ":M" + num2str(iii + 1)));
    strcat("H" + num2str(iii + 1) + ":M" + num2str(iii + 1));
    
    iii
end




















