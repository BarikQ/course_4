function [pointY, pointX] = doubleSpot(imageGS)
    pxH = length(imageGS);
    pxW = length(imageGS(1, :));

    columns = pxW;
    rows = pxH;
    
    pointX = 0;
    pointY = 0;
    
    for y = 0 : floor(rows / 2) - 1
        y = y * 2 + 1;
        for x = 0 : floor(columns / 2) - 1
            if(imageGS(y, x * 2 + 1) ~= 0)      
                
                pointX = x * 2 + 1;
                pointY = y;

                return;
            end
        end
    end

    rows = [1, pxH];
    cols = [1, pxW];
    
    for y = rows
        for x = 1 : floor(length(imageGS(y, :)) / 2)
            x = x * 2;
            
            if(imageGS(y, x) ~= 0)      
                pointX = x;
                pointY = y;
                return;
            end
        end
    end
    
    for x = cols
        for y = 1 : floor(length(imageGS) / 2)
            y = y * 2;
            
            if(imageGS(y, x) ~= 0)      
                pointX = x;
                pointY = y;
                return;
            end
        end
    end
end