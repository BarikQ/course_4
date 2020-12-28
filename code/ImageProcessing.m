close all;
clear all;
clc;

% import queue_2.*
import Queue.*

% параметры устройства
d = 0.0003;     % диаметр отверстия
t = 0.00005;     % толщина отверстия
h = 0.0007;      % высота отверстия

format long
height = 4.51e-3;    % Размеры матрицы
width = 2.88e-3;
pxW = 752;
pxH = 480;
pxSize = width / pxW;

angle = deg2rad(0 : 359);           % вспомогательный массив углов
defCircleX = (d/2) * cos(angle);             % координата x контура пятна
defCircleY = (d/2) * sin(angle);             % координата y контура пятна
xPx = ceil((defCircleX + width/2) / pxSize);  % x - контур пятна в пикселях
yPx = ceil((defCircleY + height/2) / pxSize);  % y - контур пятна в пикселях
defPxRadius = ceil((max(xPx) - min(xPx)) / 2);

filename = 'compare.xlsx';

for iii = 1 : 1000
    % чтение картинки и перевод в ч-б
    [image, colorMap] = imread(strcat("./Images/circle_", num2str(iii), ".png"));
    imageGS = rgb2gray(image);

    % figure, imshow(image);

    % figure, imshow(imageGS);

    [rows, columns, numberOfColorChannels] = size(image);

    x = 1:columns;
    y = 1:rows;

    imageProcessed = zeros(rows, columns, 3);

    %% поиск цветных пикселей перебором всех пикселей матрицы
    [brutX, brutY] = brutForce(imageGS);

    %% поиск рандомом
    [randX, randY] = randPick(imageGS);
    
    fileData = {brutY, brutX, randY, randX};
%     writecell(fileData, filename, 'sheet', 1, 'Range', strcat("H" + iii + 1));
    writecell(fileData, filename, 'sheet', 1, 'Range', strcat("H" + num2str(iii + 1) + ":K" + num2str(iii + 1)));
    strcat("H" + num2str(iii + 1) + ":K" + num2str(iii + 1))
    
end




















