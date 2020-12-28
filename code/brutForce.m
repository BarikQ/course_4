function [brutX, brutY] = brutForce(imageGS)
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

    columns = 752;
    rows = 480;
    x = 1:columns;
    y = 1:rows;
    
    coloredX = [];
    coloredY = [];

    isFlag = false;
    isFlag2 = false;

    for  i = 1 : columns
        for j = 1 : rows
            if(squeeze(imageGS(j, i, :)) ~= 0)
                coloredX(end + 1) = i;
                coloredY(end + 1) = j;
                isFlag2 = true;
                if (length(coloredX) == 1) 
                   isFlag = true; 
                end
            end
        end
        if (isFlag)
            if (~isFlag2)
               break; 
            end
        end
        isFlag2 = false;
    end

    if (length(coloredX) == 0 || length(coloredY) == 0)
       brutX = 0;
       brutY = 0;
       return;
    end
        brutX = ceil(sum(coloredX) / length(coloredX));
        brutY = ceil(sum(coloredY) / length(coloredY));
end