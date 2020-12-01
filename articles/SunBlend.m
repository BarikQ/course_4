close all;
clear all;
clc;
d = 0.0004;     % диаметр отверстия
t = 0.0001;     % толщина отверстия

alpha = deg2rad(50);      % падения солнечных лучей

angle = deg2rad(0 : 359);   % вспомогательный массив углов
x = (d/2) * cos(angle);             % координата x контура пятна
y = (d/2) * sin(angle);             % координата y контура пятна

xcopy = x;
ycopy = y;

length = size(y);
for i = 1 : length(2)
    if(abs(y(i)) >= ((t * tan(alpha)) / 2))
        if(y(i) > 0)
            y(i) = y(i) - ((t * tan(alpha)) / 2);            
        else
            y(i) = y(i) + ((t * tan(alpha)) / 2);            
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
xlim([(-d * 0.6) (d * 0.6)]);
ylim([(-d * 0.6) (d * 0.6)]);