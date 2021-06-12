function [spotX, spotY] = randSpot(imageGS)
    % анонимная функция для последовательного вызова (){}
    subindex = @(A, r) A{r};
    
    pxW = 752;
    pxH = 752;

    columns = 752;
    rows = 752;

    flag = false;
    
    spotX = 0;
    spotY = 0;
    
    randRows = randperm(rows, rows);
    randCols = randperm(columns, columns);
    
    for y = randRows
        for x = randCols

            if (imageGS(y, x) ~= 0)
              spotX = x;
              spotY = y;
              flag = true;
              break;
            end
        end
        if (flag)
            break;
        end
    end
end