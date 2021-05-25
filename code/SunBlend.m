close all;
clear all;
clc;

d = 0.0003;     % ������� ���������
t = 0.00005;     % ������� ���������
h = 0.0007;      % ������ ���������

format long
H = 4.51e-3;    % ������� �������
W = 2.88e-3;
x = zeros(1, 360);
y = zeros(1, 360);

pxH = 752;
pxW = 480;
pxSize = W / pxW;

randMinTh = 1;
randMaxTh = 80;
randMinPhi = -180;
randMaxPhi = 180;

% ������ � �������
filename = './tables/compare_new.xlsx';
fileData = {"Theta", "Phi", "����� ����� X", "����� ����� Y"};
writecell(fileData, filename, 'sheet', 1, 'Range', "D1");
dataArray = [];
xArray = [];
yArray = [];
thetaArray = [];
phiArray = [];

for iii = 1 : 1 
    theta_src = 40;     % �������� �������� ����
    phi_src = 0;       % �������� ������������ ����
%     theta_src = randMinTh + rand(1, 1) * (randMaxTh - randMinTh);     % �������� �������� ����
%     phi_src = randMinPhi + rand(1, 1) * (randMaxPhi - randMinPhi);       % �������� ������������ ����
    
    theta = deg2rad(90) - deg2rad(theta_src);      % �������� ���� ������� ��������� �����
    phi = deg2rad(phi_src);      % ������������ ���� ������� ��������� �����
    dC = h * tan(pi/2 - theta);

    angle = deg2rad(0 : 359);           % ��������������� ������ �����
    x = (d/2) * cos(angle);             % ���������� x ������� �����
    y = (d/2) * sin(angle);             % ���������� y ������� �����
    xPx = ceil((x + W/2) / pxSize);  % x - ������ ����� � ��������
    yPx = ceil((y + H/2) / pxSize);  % y - ������ ����� � ��������
    x1 = dC * cos(phi + pi); % x1
    y1 = dC * sin(phi + pi); % y1 
    x1Px = ceil((x1 + W/2 + x) / pxSize); % x1 px
    y1Px = ceil((y1 + H/2 + y) / pxSize); % y1 px
    x0 = (t + h) * tan(pi/2 - theta) * cos(phi + pi); % ������ ���������� ����� (��� ����� ��������� �����)
    y0 = (t + h) * tan(pi/2 - theta) * sin(phi + pi); % ������ ���������� ����� (��� ����� ��������� �����)
    psY = ceil((y1/2 + y0/2 + H/2) / pxSize);
    psX = ceil((x1/2 + x0/2 + W/2) / pxSize);
    x0Px = ceil((x0 + W/2 + x) / pxSize); % x0Px - ������ ���������� ����� (��� ����� ��������� �����) � ��������
    y0Px = ceil((y0 + H/2 + y) / pxSize); % y0Px - ������ ���������� ����� (��� ����� ��������� �����) � ��������
    
    % ���������� ����� �� ��������� � ���������
    image = zeros(pxW, pxH, 3);
    for i = 1 : length(x0Px)
%         image(xPx(i), yPx(i), [3 3 3]) = 1;
%         image(x1Px(i), y1Px(i), [1 1 1]) = 1;
%         image(x0Px(i), y0Px(i), [1 1 1]) = 1;
    end
    
    % ����� ��������� / �������� �� ���� ��������� �����������
    minX = min(x0Px);
    minY = min(y0Px);
    maxX = max(x1Px);
    maxY = max(x1Px);
    if (minX > min(x1Px))
       minX = min(x1Px);
    end
    if (minY > min(x1Px))
       minY = min(x1Px);
    end
    if (maxX < max(x0Px))
       maxX = max(x0Px);
    end
    if (maxY < max(y0Px))
       maxY = max(y0Px);
    end
    
    % ���� ��������� ��� �����������!!!
    x_ = []; % ���������� ���������� � ������������� � ���������� �����
    y_ = []; % ���������� ���������� � ������������� � ���������� �����
    
    % ����� ����������� ���� �����������
    for i = minX : maxX
        for j = minY : maxY

            if (i <= 0 || i > pxW)
                continue;
            end
            if (j <= 0 || j > pxH)
                continue;
            end

            in = inpolygon(i, j, x0Px, y0Px);
            in2 = inpolygon(i, j, x1Px, y1Px);
            if (in ~= 0 && in2 ~= 0)
    %             image2(i, j, [2 2 2]) = 1; 
                x_(end + 1) = i;
                y_(end + 1) = j;
            end
        end
    end
    
    % ������������ ����� �������
    for i = 1 : length(x_)
    %     image(x_(i), y_(i), [1 1 3]) = 1;
     image(x_(i), y_(i), 1) = 1;    %Red 
     image(x_(i), y_(i), 2) = 1;  %Green
     image(x_(i), y_(i), 3) = 0;  %Blue
    end
    
    thetaArray(end + 1) = theta;
    phiArray(end + 1) = phi;
    xArray(end + 1) = psX;
    yArray(end + 1) = psY;
    imshow(image);
    imwrite(image, strcat("./images/circle_", num2str(iii), ".png"));
    
    fileData = {theta, phi, xArray, yArray};
    writecell(fileData, filename, 'sheet', 1, 'Range', strcat("D" + num2str(iii + 1) + ":G" + num2str(iii + 1)));
    strcat("D" + num2str(iii + 1) + ":G" + num2str(iii + 1))
end
% % %     range = sprintf('D2:D%d', numel(thetaArray));
    
%     fileData = {theta, phi, psX, psY};
% for i = 1:1000
%     xlswrite(filename, thetaArray(i), 1, strcat("D" + num2str(i + 1)));
%     xlswrite(filename, phiArray(i), 1, strcat("E" + num2str(i + 1)));
%     xlswrite(filename, xArray(i), 1, strcat("F" + num2str(i + 1)));
%     xlswrite(filename, yArray(i), 1,strcat("G" + num2str(i + 1)));
% end
%     writecell({thetaArray:thetaArray, phiArray, xArray, yArray}, filename, 'sheet', 1, 'Range', range);   

