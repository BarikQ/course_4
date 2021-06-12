function [pointX, pointY] = breadthSpot(imageGS, spotX, spotY)
    if (spotX == 0 || spotY == 0)
       breadthX = 0;
       breadthY = 0;
       return;
    end

    pxH = length(imageGS);
    pxW = length(imageGS(1, :));
    
    breadthX = spotX;
    breadthY = spotY;
    pointX = 0;
    pointY = 0;
    
    flag = false;
    
    frontier = CQueue();
    frontier.push([breadthX, breadthY]);
    maxReached = [imageGS];
    maxReached(breadthY, breadthX) = 100;

    while (frontier.size() ~= 0) 
        if (flag)
            break;
        end
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
            if (neighboors(i, 1) > pxW || neighboors(i, 1) <= 0)
                isOkay(i) = boolean(0);
                neighboors(i, 1) = -1;
            end
            
            if (neighboors(i, 2) > pxH || neighboors(i, 2) <= 0)
                isOkay(i) = boolean(0);
                neighboors(i, 1) = -1;
            end
        end
        
        for i = 1 : length(neighboors)
            if (~isOkay(i))
               continue; 
            end
           
            if (maxReached(neighboors(i, 2), neighboors(i, 1)) ~= 100)
               if (imageGS(neighboors(i, 2), neighboors(i, 1)) == 0)                 
                   frontier.push(neighboors(i, :));
                   maxReached(neighboors(i, 2), neighboors(i, 1)) = 0;
               end
               if (imageGS(neighboors(i, 2), neighboors(i, 1)) == 226)
                   pointY = neighboors(i, 2);
                   pointX = neighboors(i, 1);
                   flag = true;
                   break;
               end
           end
        end
    end
end