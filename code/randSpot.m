function [spotX, spotY] = randSpot(imageGS)
    pxW = 752;
    pxH = 752;

    columns = 752;
    rows = 752;

    coloredX2 = [];
    coloredY2 = [];

    find = false;
    repeat = zeros(pxH, pxW);
    
    matrix = [];
    
    newColoredX = [];
    newColoredY = [];
    
%     for i = 1:rows
%         matrix{end + 1} = 1:columns;
%     end
    mapColoredX = [];
    mapColoredY = [];

    matrixCurrentKeys = 1:rows;
    matrixValues = {};
    for i = 1:columns
        matrixValues{end + 1} = 1:columns;
    end
    map = containers.Map(matrixCurrentKeys, matrixValues);
    matrixCurrentKeys = keys(map);
    
    % поиск первой точки пятна
    iter = 1;
    while(find == 0)
        if (mod(iter, 10) == 0) 
%            close all 
        end
        
        if (iter > columns * rows) 
            break;
        end

        if (length(map) == 0)
           break; 
        end
        
        randMapKeyIndex = randi(length(matrixCurrentKeys), 1);
        currentKey = matrixCurrentKeys(randMapKeyIndex);
        currentY = currentKey{1};
        currentRow = map(currentY);
        currentRowIndex = randi(length(currentRow), 1);
        currentX = currentRow(currentRowIndex);
        
        if (imageGS(currentY, currentX) ~= 0)
            mapColoredX(end + 1) = currentX;
            mapColoredY(end + 1) = currentY;
            find = true;
        end
        
        currentRow(currentRowIndex) = [];
        map(currentY) = currentRow;
        if (length(currentRow) == 0)
           remove(map, currentY); 
           matrixCurrentKeys = keys(map);
        end
        [length(map), length(currentRow)];
        
%  ============================================================================
%         randRowIndex = randi(length(matrix), 1);
%         randRow = matrix{randRowIndex};
%         randColumnIndex = randi(length(matrix{randRowIndex}), 1);
%         randColumn = randRow(randColumnIndex);
%         
%         if (imageGS(randRow, randColumn) ~= 0)
%             newColoredX(end + 1) = randColumn;
%             newColoredY(end + 1) = randRow;
%             find = true;
%         end
%         
%         matrix{randRow}(randColumn) = [];
%         if (length(matrix{randRow}) == 0)
%            matrix(randRow, :) = []; 
%         end
%         length(matrix);
%         length(matrix{randRow});
        
%  ============================================================================

%         randX = randi(columns, 1);
%         randY = randi(rows, 1);
        
%         if (repeat(randY, randX) == 1)
%             if (any(repeat(:) == 0))
%                 continue;
%             else
%                 break;
%             end
%         end
        
%         repeat(randY, randX) = 1;
%         
%         if(squeeze(imageGS(randY, randX, :)) ~= 0)
%             coloredX2(end + 1) = randX;
%             coloredY2(end + 1) = randY;
%             find = true;
%         end

        iter = iter + 1;
        
%         imageGS(randRow, randColumn) = 226;
%         figure, imshow(imageGS);
    end
    
    if (length(mapColoredX) ~= 0 || length(mapColoredY) ~= 0)
        spotX = mapColoredX(end);
        spotY = mapColoredY(end);
        return;
    else
        spotX = 0;
        spotY = 0;
        return;
    end
    
%     if (length(newColoredX) ~= 0 || length(newColoredY) ~= 0)
%         spotX = newColoredX(end);
%         spotY = newColoredY(end);
%         return;
%     end
        
    
%     if (length(coloredX2) == 0 || length(coloredY2) == 0) 
%         randX = 0;
%         randY = 0;
%         spotX = randX;
%         spotY = randY;
%         return;
%     end
    
%     spotX = randX;
%     spotY = randY;
end