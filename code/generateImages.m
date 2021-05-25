
close all;
clear all;
clc;
 
d = 0.0003;     % диаметр отверстия
t = 100e-6;     % толщина отверстия
h = 0.0007;     % высота отверстия

format long
% H = 4.51e-3;    % Размеры матрицы
% W = 2.88e-3;
H = 4e-3;    % Размеры матрицы
W = 4e-3;

x = zeros(1, 360);
y = zeros(1, 360);

pxH = 752;
% pxW = 480;
pxW = 752;
pxSize = W / pxW;

randMinTh = 1;
randMaxTh = 70;
randMinPhi = -180;
randMaxPhi = 180;
 
% ЗАПИСЬ В ТАБЛИЦУ
filename = './tables/compare_new.xlsx';
fileData = {"Theta", "Phi", "Центр пятна X", "Центр пятна Y"};
writecell(fileData, filename, 'sheet', 1, 'Range', "D1");
dataArray = [];
xArray = [];
yArray = [];
thetaArray = [];
phiArray = [];
 
for iii = 1 : 500
%     theta_src = 55;     % исходный зенитный угол
%     phi_src = 58;       % исходный азимутальный угол
    theta_src = randMinTh + rand(1, 1) * (randMaxTh - randMinTh);     % СЛУЧАЙНЫЙ зенитный угол
    phi_src = randMinPhi + rand(1, 1) * (randMaxPhi - randMinPhi);       % СЛУЧАЙНЫЙ азимутальный угол
    
    theta = deg2rad(90) - deg2rad(theta_src);      % зенитный угол падения солнечных лучей
    phi = deg2rad(phi_src);      % азимутальный угол падения солнечных лучей
    dC = h * tan(pi/2 - theta);
    angle = deg2rad(0 : 359);           % вспомогательный массив углов
    x = (d/2) * cos(angle);             % координата x контура пятна
    y = (d/2) * sin(angle);             % координата y контура пятна
    xPx = ceil((x + W/2) / pxSize);  % x - контур пятна в пикселях
    yPx = ceil((y + H/2) / pxSize);  % y - контур пятна в пикселях
    x1 = dC * cos(phi + pi); % x1
    y1 = dC * sin(phi + pi); % y1 
    x1Px = ceil((x1 + W/2 + x) / pxSize); % x1 px
    y1Px = ceil((y1 + H/2 + y) / pxSize); % y1 px
    
    x0 = (t + h) * tan(pi/2 - theta) * cos(phi + pi); % контур смещённого пятна (без учёта обрезания круга)
    y0 = (t + h) * tan(pi/2 - theta) * sin(phi + pi); % контур смещённого пятна (без учёта обрезания круга)
 
    psY = ceil((y1/2 + y0/2 + H/2) / pxSize);
    psX = ceil((x1/2 + x0/2 + W/2) / pxSize);
    
    x0Px = ceil((x0 + W/2 + x) / pxSize); % x0Px - контур смещённого пятна (без учёта обрезания круга) в пикселях
    y0Px = ceil((y0 + H/2 + y) / pxSize); % y0Px - контур смещённого пятна (без учёта обрезания круга) в пикселях
 
    % рисование смешённого и повёрнутого пятна
    image = zeros(pxW, pxH, 3);
 
    % круги вокруг пятна и в центре матрицы.
    for i = 1 : length(x0Px)
    %     image(xPx(i), yPx(i), [3 3 3]) = 1;
    %     image(x1Px(i), y1Px(i), [1 2 1]) = 1;
    %     image(x0Px(i), y0Px(i), [1 1 1]) = 1;
    end
 
    % найти максимумы / минимумы из двух смещённых окружностей
    minX = min(x0Px);
    minY = min(y0Px);
    maxX = max(x1Px);
    maxY = max(x1Px);
 
    if (minX > min(x1Px))
       minX = min(x1Px);
    end
    if (minY > min(x1Px))
       minY = min(x1Px);
    end
    if (maxX < max(x0Px))
       maxX = max(x0Px);
    end
    if (maxY < max(y0Px))
       maxY = max(y0Px);
    end
 
    % можно оптимизировать
    x_ = []; % координата усечённого и перемещённого и повёрнутого круга
    y_ = []; % координата усечённого и перемещённого и повёрнутого круга
 
    % найти пересечение двух окружностей
    for i = minX : maxX
        for j = minY : maxY
 
            if (i <= 0 || i > pxW)
                continue;
            end
            if (j <= 0 || j > pxH)
                continue;
            end
 
            in = inpolygon(i, j, x0Px, y0Px);
            in2 = inpolygon(i, j, x1Px, y1Px);
            if (in ~= 0 && in2 ~= 0)
    %             image2(i, j, [2 2 2]) = 1; 
                x_(end + 1) = i;
                y_(end + 1) = j;
            end
        end
    end
 
    % Закрашивание общей области
    for i = 1 : length(x_)
    %     image(x_(i), y_(i), [1 1 3]) = 1;
     image(x_(i), y_(i), 1) = 1;    %Red 
     image(x_(i), y_(i), 2) = 1;  %Green
     image(x_(i), y_(i), 3) = 0;  %Blue
    end
    
%     imshow(image);
    imwrite(image, strcat("./images/circle_", num2str(iii), ".png"));
    
    fileData = {rad2deg(theta), rad2deg(phi), psY, psX};
    writecell(fileData, filename, 'sheet', 1, 'Range', strcat("D" + num2str(iii + 1) + ":G" + num2str(iii + 1)));
    strcat("D" + num2str(iii + 1) + ":G" + num2str(iii + 1));
   
    iii
end
  
