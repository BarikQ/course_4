function [randX, randY] = randPick(imageGS, spotX, spotY)

    % параметры устройства
    d = 0.0003;     % диаметр отверстия

    format long
    height = 4e-3;
    width = 4e-3;

    pxH = length(imageGS);
    pxW = length(imageGS(1, :));
    pxSize = width / pxW;
    
    angle = deg2rad(0 : 359);           % вспомогательный массив углов
    defCircleX = (d/2) * cos(angle);             % координата x контура пятна
    defCircleY = (d/2) * sin(angle);             % координата y контура пятна
    xPx = ceil((defCircleX + width/2) / pxSize);  % x - контур пятна в пикселях
    yPx = ceil((defCircleY + height/2) / pxSize);  % y - контур пятна в пикселях
    defPxRadius = ceil((max(xPx) - min(xPx)) / 2);

    coloredX = [spotX];
    coloredY = [spotY];
    
    % Т.К. ПОЛУЧЕННОЕ ПЯТНО 100% МЕНЬШЕ ЧЕМ ТО, ЧТО ПОЛУЧАЕТСЯ БЕЗ НАКЛОНА
    % МАТРИЦЫ МОЖНО ПОИСКАТЬ ПИКСЕЛИ В ПРЕДЕЛАХ ДИАМЕТРА НЕИЗМЕННЁНОГО КРУГА
    % В 4 КВАДРАНТАХ

    % левый верхний квадрат граница
    leftTopX = coloredX(1) - defPxRadius *  2;
    leftTopY = coloredY(1) - defPxRadius * 2;
    % левый нижний квадрат граница
    leftBottomX = coloredX(1) - defPxRadius * 2;
    leftBottomY = coloredY(1) + defPxRadius * 2;
    % правый верхний квадрат граница
    rightTopX = coloredX(1) + defPxRadius * 2;
    rightTopY = coloredY(1) - defPxRadius * 2;
    % правый нижний квадрат
    rightBottomX = coloredX(1) + defPxRadius * 2;
    rightBottomY = coloredY(1) + defPxRadius * 2;

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
    coloredX = [];
    coloredY = [];
    
    for y = quadroPositionsY(1) : quadroPositionsY(3)
        columnFlag = false;
       for x = quadroPositionsX(1) : quadroPositionsX(3)
           if (y <= 0 || x <= 0)
              continue; 
           end
            if(imageGS(y, x) ~= 0)
                coloredX(end + 1) = x;
                coloredY(end + 1) = y;
                
                columnFlag = true;
                isFlag2 = true;
                
                if (length(coloredX) == 2)
                   isFlag = true; 
                end
            else
                if (columnFlag)
                   break; 
                end
            end
       end
       if (isFlag)
          if (~isFlag2)
            break;
          end
       end
    end
    
    randX = ceil(sum(coloredX) / length(coloredX));
    randY = ceil(sum(coloredY) / length(coloredY));
end