function [spotX, spotY] = roundDoubleSpot(imageGS)
    subindex = @(A, r) A(r);

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
        
        for x = (topLeftX : 2 : topRightX)
            if(imageGS(topLeftY, x) ~= 0)
                spotX = x;
                spotY = topLeftY;
                isFlag = true;
                break;
            end
        end
        
        for x = (bottomLeftX : 2 : bottomRightX)
            if(imageGS(bottomLeftY, x) ~= 0)
                spotX = x;
                spotY = bottomLeftY;
                isFlag = true;
                break;
            end
        end
        
        for y = (topLeftY : 2 : bottomLeftY)
            if(imageGS(y, topLeftX) ~= 0)
                spotX = topLeftX;
                spotY = y;
                isFlag = true;
                break;
            end
        end
        
        for x = (topRightY : 2 : bottomRightY)
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