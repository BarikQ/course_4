function [spotX, spotY] = bruteSpot(imageGS)
    pxH = length(imageGS);
    pxW = length(imageGS(1, :));

    columns = pxH;
    rows = pxW;
    
    spotX = 0;
    spotY = 0;
    
    isFlag = false;
    
    for  y = 1 : rows
        for x = 1 : columns
            if(imageGS(y, x) ~= 0)      
                spotX = x;
                spotY = y;
                
                isFlag = true; 
            end
        end
        if (isFlag)
            break;
        end
    end
end