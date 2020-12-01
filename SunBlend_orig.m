close all;
clear all;
clc;
d = 0.0004;     % диаметр отверстия
t = 0.0001;     % толщина отверстия
h = 0.001;      % высота отверстия

H = 0.00451;    % Размеры матрицы
V = 0.00288;

theta = deg2rad(67);      % зенитный угол падения солнечных лучей
phi = deg2rad(30);      % азимутальный угол падения солнечных лучей

angle = deg2rad(0 : 359);   % вспомогательный массив углов
x = (d/2) * cos(angle);             % координата x контура пятна
y = (d/2) * sin(angle);             % координата y контура пятна

xcopy = x;
ycopy = y;

length = size(y);
for i = 1 : length(2)
    if(abs(y(i)) >= ((t * tan(theta)) / 2))
        if(y(i) > 0)
            y(i) = y(i) - ((t * tan(theta)) / 2);            
        else
            y(i) = y(i) + ((t * tan(theta)) / 2);            
        end
    else
        % для последующего удаления
        y(i) = 15;
        x(i) = 15;
    end;
    clc;
end

% удаление не лишних точек
x(x == 15) = [];
y(y == 15) = [];

screenSize = get(0,'screensize');       % получение размера экрана
plotSize = 500;                         % установка размера фигуры(сторона квадрата)
figure('Position', [(screenSize(3) - plotSize)/2 (screenSize(4) - plotSize)/2 plotSize plotSize]);
scatter(xcopy, ycopy, 'b');
hold on;
scatter(x, y, 'r');
xlim([-V V]);
ylim([-H H]);

%% Поворот изображения
M = [cos(phi) -sin(phi); sin(phi) cos(phi)];
v = [x; y];
vrot = (v' * M)';

hold on;
scatter(vrot(1, :), vrot(2, :), 'g');

%% Смещение

r = tan(theta) * h;
vrot(1, :) = vrot(1, :) + (r * cos(phi));
vrot(2, :) = vrot(2, :) + (r * sin(phi));
figure('Position', [(screenSize(3) - plotSize)/2 (screenSize(4) - plotSize)/2 plotSize plotSize]);
scatter(vrot(1, :), vrot(2, :), '+')
xlim([-H/2 H/2]);
ylim([-V/2 V/2]);