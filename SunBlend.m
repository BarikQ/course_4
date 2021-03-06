close all;
clear all;
clc;

d = 500e-6;     % ������� ���������
t = 100e-6;     % ������� ���������
h = 0.0007;      % ������ ���������

format long
% H = 4.51e-3;    % ������� �������
% W = 2.88e-3;
H = 4e-3;    % ������� �������
W = 4e-3;
x = zeros(1, 360);
y = zeros(1, 360);

pxH = 752;
% pxW = 480;
pxW = 752;
pxSize = W / pxW;

theta_src = 60;     % �������� �������� ����
phi_src = 57;       % �������� ������������ ����

theta = deg2rad(90) - deg2rad(theta_src);      % �������� ���� ������� ��������� �����
phi = deg2rad(phi_src);                        % ������������ ���� ������� ��������� �����
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

x0Px = ceil((x0 + W/2 + x) / pxSize); % x0Px - ������ ���������� ����� (��� ����� ��������� �����) � ��������
y0Px = ceil((y0 + H/2 + y) / pxSize); % y0Px - ������ ���������� ����� (��� ����� ��������� �����) � ��������

% ���������� ����� �� ��������� � ���������
image2 = zeros(pxW, pxH);
for i = 1 : length(x0Px)
    image2(xPx(i), yPx(i), [3 3 3]) = 1;
%     image2(x1Px(i), y1Px(i), [1 2 1]) = 1;
%     image2(x0Px(i), y0Px(i), [1 1 1]) = 1;
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

squareActualPx = 0;
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
            squareActualPx = squareActualPx + 1;
        end
    end
end

squareAllPx = pxH * pxW;
squareRatio = squareActualPx / squareAllPx;
square = squareRatio * (H * W)

% ������������ ����� �������
for i = 1 : length(x_)
    image2(x_(i), y_(i), [2 2 2]) = 1;
end

imshow(image2);
imwrite(image2, 'circles.png');
