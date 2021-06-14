close all;
clear all;
clc;

% параметры устройства
d = 0.0003;     % диаметр отверстия
t = 100e-6;     % толщина отверстия
h = 0.0007;     % высота отверстия

format long
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

filename = './tables/compare_last.xlsx';

fileData = [
    "Brute X", "Brute Y", "time", ...
    "Quad X", "Quad Y", "time", ...
    "Breadth X", "Breadth Y", "time", ...
    "Brute", "Rand", "Double", "Breadth", "Round", "Round&Double"...
 ];

writematrix(fileData, filename, 'sheet', 1, 'Range', "F1");

format short g
totalBruteDef = 0;
totalQuadro = 0;
totalBreadth = 0;

totalBruteSpot = 0;
totalRandSpot = 0;
totalBreadthSpot = 0;
totalDoubleSpot = 0;
totalRoundSpot = 0;
totalRoundDoubleSpot = 0;

for iii = 1 : 500
    % чтение картинки и перевод в ч-б
    [image, colorMap] = imread(strcat("./images/circle_", num2str(iii), ".png"));
    imageGS = rgb2gray(image);

    [rows, columns, numberOfColorChannels] = size(image);

    x = 1:columns;
    y = 1:rows;

    imageProcessed = zeros(rows, columns, 3);

    %% brute force default
%     tic
    [bruteX, bruteY] = bruteForce(imageGS);
%     timeBruteDef = round(toc, 4);
    
    %% brute spot
%     tic
    [spotX, spotY] = bruteSpot(imageGS);
%     timeBruteSpot = round(toc, 4);
    
    %% rand spot
%     tic
    [spotX, spotY] = randSpot(imageGS);
%     timeRandSpot = round(toc, 4);
    
    %% quad center
%     tic
    [quadX, quadY] = randPick(imageGS, spotX, spotY);
%     timeQuadro = round(toc, 4);
    
    %% breadth search
%     tic
    [breadthX, breadthY] = breadthSearch(imageGS, spotX, spotY);
%     timeBreadth = round(toc, 4);
    
    %% double spot
%     tic
    [doubleY, doubleX] = doubleSpot(imageGS);
%     timeDoubleSpot = round(toc, 4);
    
    %% round spot
%     tic
    [roundX, roundY] = roundSpot(imageGS);
%     timeRoundSpot = round(toc, 4);
    
    %% breadth spot
%     tic
%     [breadthSpotX, breadthSpotY] = breadthSpot(imageGS, pxW / 2, pxH / 2);
%     timeBreadthSpot = round(toc, 4);
    
    %% round double spot
%     tic
    [roundDoubleX, roundDoubleY] = roundDoubleSpot(imageGS);
%     timeRoundDoubleSpot = round(toc, 4);
    
    format short g
%     totalBruteDef = totalBruteDef + timeBruteDef;
%     totalQuadro = totalQuadro + timeQuadro;
%     totalBreadth = totalBreadth + timeBreadth;
    
%     totalBruteSpot = totalBruteSpot + timeBruteSpot;
%     totalRandSpot = totalRandSpot + timeRandSpot;
%     totalBreadthSpot = totalBreadthSpot + timeBreadthSpot;
%     totalDoubleSpot = totalDoubleSpot + timeDoubleSpot;
%     totalRoundSpot = totalRoundSpot + timeRoundSpot;
%     totalRoundDoubleSpot = totalRoundDoubleSpot + timeRoundDoubleSpot;
          
    fileData = {
        bruteX, bruteY, timeBruteDef,...
        quadX, quadY, timeQuadro,...
        breadthX, breadthY, timeBreadth,...
        "", timeBruteSpot, "", timeRandSpot, "", timeDoubleSpot, ...
        "", timeBreadthSpot, "", timeRoundSpot, "", timeRoundDoubleSpot ...
    };

    writecell(fileData, filename, 'sheet', 1, 'Range', strcat("F" + num2str(iii + 1)));

    iii
end

% totalBruteDef = round(totalBruteDef, 4);
% totalQuadro = round(totalQuadro, 4);
% totalBreadth = round(totalBreadth, 4);

% totalBruteSpot = round(totalBruteSpot, 4);
% totalRandSpot = round(totalRandSpot, 4);
% totalBreadthSpot = round(totalBreadthSpot, 4);
% totalDoubleSpot = round(totalDoubleSpot, 4);
% totalRoundSpot = round(totalRoundSpot, 4);
% totalRoundDoubleSpot = round(totalRoundDoubleSpot, 4);

fileData = [
    "Brute X", "Brute Y", totalBruteDef, ...
    "Quad X", "Quad Y", totalQuadro, ...
    "Breadth X", "Breadth Y", totalBreadth, ...
    "Brute:", totalBruteSpot, "Rand:", totalRandSpot, "Double", totalDoubleSpot, ...
    "Breadth:", totalBreadthSpot, "Round:", totalRoundSpot, "Ro | Do", totalRoundDoubleSpot...
 ];

writematrix(fileData, filename, 'sheet', 1, 'Range', "F1");



















