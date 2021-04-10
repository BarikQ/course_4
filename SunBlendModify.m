close all;
clear all;
clc;

d = 600e-6;     % диаметр отверсти€
t = 100e-6;     % толщина отверсти€
h = 0.81e-3;      % высота отверсти€

format long
H = 4.0e-3;    % –азмеры матрицы
W = 4.0e-3;
x = zeros(1, 360);
y = zeros(1, 360);

pxH = 1000;
pxW = 1000;
pxSize = W / pxW;


theta_src =65;     % исходный зенитный угол
phi_src = 0;       % исходный азимутальный угол
%     theta_src = randMinTh + rand(1, 1) * (randMaxTh - randMinTh);     % исходный зенитный угол
%     phi_src = randMinPhi + rand(1, 1) * (randMaxPhi - randMinPhi);       % исходный азимутальный угол

theta = deg2rad(90) - deg2rad(theta_src);      % зенитный угол падени€ солнечных лучей
phi = deg2rad(phi_src);      % азимутальный угол падени€ солнечных лучей
dC = h * tan(pi/2 - theta);

angle = deg2rad(0 : 359);           % вспомогательный массив углов
x = (d/2) * cos(angle);             % координата x контура п€тна
y = (d/2) * sin(angle);             % координата y контура п€тна
xPx = ceil((x + W/2) / pxSize);  % x - контур п€тна в пиксел€х
yPx = ceil((y + H/2) / pxSize);  % y - контур п€тна в пиксел€х
x1 = dC * cos(phi + pi); % x1
y1 = dC * sin(phi + pi); % y1
x1Px = ceil((x1 + W/2 + x) / pxSize); % x1 px
y1Px = ceil((y1 + H/2 + y) / pxSize); % y1 px
x0 = (t + h) * tan(pi/2 - theta) * cos(phi + pi); % контур смещЄнного п€тна (без учЄта обрезани€ круга)
y0 = (t + h) * tan(pi/2 - theta) * sin(phi + pi); % контур смещЄнного п€тна (без учЄта обрезани€ круга)
psY = ceil((y1/2 + y0/2 + H/2) / pxSize);
psX = ceil((x1/2 + x0/2 + W/2) / pxSize);
x0Px = ceil((x0 + W/2 + x) / pxSize); % x0Px - контур смещЄнного п€тна (без учЄта обрезани€ круга) в пиксел€х
y0Px = ceil((y0 + H/2 + y) / pxSize); % y0Px - контур смещЄнного п€тна (без учЄта обрезани€ круга) в пиксел€х
% нарисовать круги со смещением и поворотом
image = zeros(pxW, pxH, 3);
for i = 1 : length(x0Px)
    image(xPx(i), yPx(i), [3 3 3]) = 1;
    image(x1Px(i), y1Px(i), [1 1 1]) = 1;
    image(x0Px(i), y0Px(i), [1 1 1]) = 1;
end
% найти максимумы / минимумы из двух смещЄнных окружностей
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
% ≈сть потенциал дл€ оптимизации!!!
x_ = []; % координата усечЄнного и перемещЄнного и повЄрнутого круга
y_ = []; % координата усечЄнного и перемещЄнного и повЄрнутого круга
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
% «акрашивание общей области
for i = 1 : length(x_)
    %     image(x_(i), y_(i), [1 1 3]) = 1;
    image(x_(i), y_(i), 1) = 1;    %Red
    image(x_(i), y_(i), 2) = 1;  %Green
    image(x_(i), y_(i), 3) = 0;  %Blue
end

imshow(image);
imwrite(image, strcat(num2str(1), ".png"));


