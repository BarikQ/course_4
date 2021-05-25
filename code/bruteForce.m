function [bruteX, bruteY] = bruteForce(imageGS)
    pxW = 752;
    pxH = 752;

    columns = pxW;
    rows = pxH;
    
    coloredX = [];
    coloredY = [];
    
    isFlag = false;
    isFlag2 = false;

    for  i = 1 : columns
        for j = 1 : rows
            if(imageGS(j, i) ~= 0)      
                
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
       bruteX = 0;
       bruteY = 0;
       return;
    end
    
    bruteX = ceil(sum(coloredX) / length(coloredX));
    bruteY = ceil(sum(coloredY) / length(coloredY));
end