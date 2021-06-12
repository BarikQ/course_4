function [breadthX, breadthY] = breadthSearch(imageGS, spotX, spotY)
    if (spotX == 0 || spotY == 0)
       breadthX = 0;
       breadthY = 0;
       return;
    end

    pxH = length(imageGS);
    pxW = length(imageGS(1, :));
    
    breadthX = spotX;
    breadthY = spotY;
    
    sumY = breadthX;
    sumX = breadthY;
    sizeX = 1;
    sizeY = 1;
    
    frontier = CQueue();
    frontier.push([breadthX, breadthY]);
    maxReached = [imageGS];
    maxReached(breadthY, breadthX) = 0;

    while (frontier.size() ~= 0) 
        isOkay = boolean([1 1 1 1]);
        current = frontier.pop();
        
        % определение соседей текущей клетки
        neighboor_r = [current(1) + 1, current(2)];
        neighboor_l = [current(1) - 1, current(2)];
        neighboor_t = [current(1), current(2) + 1];
        neighboor_b = [current(1), current(2) - 1];
        neighboors = [neighboor_r; neighboor_l; neighboor_t; neighboor_b];
        
        % проверка, чтобы соседи не выходили за матрицу
        for i = 1 : length(neighboors)
%             neighboors(i, :)
            if (neighboors(i, 1) > pxW || neighboors(i, 1) <= 0)
                isOkay(i) = boolean(0);
                neighboors(i, 1) = -1;
            end
            
            if (neighboors(i, 2) > pxH || neighboors(i, 2) <= 0)
                isOkay(i) = boolean(0);
                neighboors(i, 1) = -1;
            end
%             neighboors(i, :)
%             isOkay(i)
        end
        
        for i = 1 : length(neighboors)
            if (~isOkay(i))
               continue; 
            end
           
            if (maxReached(neighboors(i, 2), neighboors(i, 1)) ~= 0)
               if (imageGS(neighboors(i, 2), neighboors(i, 1)) == 0)
                   continue;
               end
               
               sumY = sumY + neighboors(i, 2);
               sumX = sumX + neighboors(i, 1);
         
               sizeX = sizeX + 1;
               sizeY = sizeY + 1;
               
               frontier.push(neighboors(i, :));
               maxReached(neighboors(i, 2), neighboors(i, 1)) = 0;
           end
        end
    end
    
    breadthX = ceil(sumX / sizeX);
    breadthY = ceil(sumY / sizeY);

end