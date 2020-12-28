function [randX, randY] = randPick(imageGS)
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

    coloredX2 = [];
    coloredY2 = [];

    currentX = 0;
    currentY = 0;

    find = false;
    repeat = zeros(pxH, pxW);
    
    % поиск первой точки пятна
    iter = 1;
    while(find == 0)
        if (iter > 10000) 
            break;
        end
        randX = randi(columns, 1);
        randY = randi(rows, 1);
        
        if (repeat(randY, randX) == 1)
            if (any(repeat(:) == 0))
            continue;
            else break;
            end
        end
        
        repeat(randY, randX) = 1;
        
        if(squeeze(imageGS(randY, randX, :)) ~= 0)
            coloredX2(end + 1) = randX;
            coloredY2(end + 1) = randY;
            find = true;
        end
        iter = iter + 1;
    end
    
    if (length(coloredX2) == 0 || length(coloredY2) == 0) 
        randX = 0;
        ranY = 0;
        return;
    end
    % Т.К. ПОЛУЧЕННОЕ ПЯТНО 100% МЕНЬШЕ ЧЕМ ТО, ЧТО ПОЛУЧАЕТСЯ БЕЗ НАКЛОНА
    % МАТРИЦЫ МОЖНО ПОИСКАТЬ ПИКСЕЛИ В ПРЕДЕЛАХ ДИАМЕТРА НЕИЗМЕННЁНОГО КРУГА
    % В 4 КВАДРАНТАХ

    % левый верхний квадрат граница
    leftTopX = coloredX2(1) - defPxRadius *  2;
    leftTopY = coloredY2(1) - defPxRadius * 2;
    % левый нижний квадрат граница
    leftBottomX = coloredX2(1) - defPxRadius * 2;
    leftBottomY = coloredY2(1) + defPxRadius * 2;
    % правый верхний квадрат граница
    rightTopX = coloredX2(1) + defPxRadius * 2;
    rightTopY = coloredY2(1) - defPxRadius * 2;
    % правый нижний квадрат
    rightBottomX = coloredX2(1) + defPxRadius * 2;
    rightBottomY = coloredY2(1) + defPxRadius * 2;

    quadroPositionsX = [leftTopX, rightTopX, rightBottomX, leftBottomX];
    quadroPositionsY = [leftTopY, rightTopY, rightBottomY, leftBottomY];

    % проверка не выходят ли координаты за границы матрицы, если выходят ставим
    % = размер матрицы или 0
    for i = 1 : 4
       if (quadroPositionsX(i) <= 0)
          quadroPositionsX(i) = 1; 
       else
           if (quadroPositionsX(i) > pxW)
               quadroPositionsX(i) = pxW;
           end
       end
       if (quadroPositionsY(i) <= 0)
          quadroPositionsY(i) = 1; 
       else
           if (quadroPositionsY(i) > pxH)
               quadroPositionsY(i) = pxH;
           end
       end
    end

    isFlag = false;
    isFlag2 = false;
    
    for i = quadroPositionsX(1) : quadroPositionsX(3)
       for j = quadroPositionsY(1) : quadroPositionsY(3)
           if (i <= 0 || j <= 0)
              continue; 
           end
            if(squeeze(imageGS(j, i, :)) ~= 0)
                coloredX2(end + 1) = i;
                coloredY2(end + 1) = j;
                isFlag2 = true;
                if (length(coloredX2) == 2)
                   isFlag = true; 
                end
            end
       end
       if (isFlag)
          if (~isFlag2)
            break;
          end
       end
    end
    
    randX = ceil(sum(coloredX2) / length(coloredX2));
    randY = ceil(sum(coloredY2) / length(coloredY2));
end