function [spotX, spotY] = roundSpot(imageGS)
    pxH = length(imageGS);
    pxW = length(imageGS(1, :));

    imgCenterX = pxW / 2;
    imgCenterY = pxH / 2;
    
    spotX = 0;
    spotY = 0;
    
    isFlag = false;
    
    for  rad = 0 : imgCenterX
        topLeftX = imgCenterX - rad + 1;
        topLeftY = imgCenterY - rad + 1;
        topRightX = imgCenterX + rad;
        topRightY = imgCenterY - rad + 1;
        bottomRightX = imgCenterX + rad;
        bottomRightY = imgCenterY + rad;
        bottomLeftX = imgCenterX - rad + 1;
        bottomLeftY = imgCenterY + rad;
        
        for x = topLeftX : topRightX
            if(imageGS(topLeftY, x) ~= 0)
                spotX = x;
                spotY = topLeftY;
                isFlag = true;
                break;
            end
        end
        
        for x = bottomLeftX : bottomRightX
            if(imageGS(bottomLeftY, x) ~= 0)
                spotX = x;
                spotY = bottomLeftY;
                isFlag = true;
                break;
            end
        end
        
        for y = topLeftY : bottomLeftY
            if(imageGS(y, topLeftX) ~= 0)
                spotX = topLeftX;
                spotY = y;
                isFlag = true;
                break;
            end
        end
        
        for x = topRightY : bottomRightY            
            if(imageGS(topRightX, x) ~= 0)
                spotX = x;
                spotY = topRightX;
                isFlag = true;
                break;
            end
        end
        
        if (isFlag)
            break;
        end
    end
end