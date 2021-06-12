function [bruteX, bruteY] = bruteForce(imageGS)
    pxH = length(imageGS);
    pxW = length(imageGS(1, :));

    columns = pxH;
    rows = pxW;
    
    coloredX = [];
    coloredY = [];
    
    isFlag = false;
    isFlag2 = false;
    
    for  y = 1 : rows
        columnFlag = false;
        for x = 1 : columns
            if(imageGS(y, x) ~= 0)      
                coloredX(end + 1) = x;
                coloredY(end + 1) = y;
                
                columnFlag = true;
                isFlag2 = true;
                
                if (length(coloredX) == 1) 
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
        isFlag2 = false;

    end

    if (length(coloredX) == 0 || length(coloredY) == 0)
       bruteX = 0;
       bruteY = 0;
       return;
    end
    
    bruteX = ceil(sum(coloredX) / length(coloredX));
    bruteY = ceil(sum(coloredY) / length(coloredY));
end