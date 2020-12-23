close all;
clear all;
clc;

d = 0.0004;     % ������� ���������
t = 0.0001;     % ������� ���������
h = 0.001;      % ������ ���������

format long
H = 4.51 * 10^(-3);    % ������� �������
W = 2.88 * 10^(-3);
x = zeros(1, 360);
y = zeros(1, 360);

pxH = 752;
pxW = 480;
pxSize = W / pxW;

theta = deg2rad(90) - deg2rad(45);      % �������� ���� ������� ��������� �����
phi = deg2rad(-45);      % ������������ ���� ������� ��������� �����
dC = h * tan(pi/2 - theta);

angle = deg2rad(0 : 359);   % ��������������� ������ �����
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
    image2(x1Px(i), y1Px(i), [1 2 1]) = 1;
    image2(x0Px(i), y0Px(i), [1 1 1]) = 1;
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

x_ = []; % ���������� ���������� � ������������� � ���������� �����
y_ = []; % ���������� ���������� � ������������� � ���������� �����
% ����� ����������� ���� �����������
for i = minX : maxX
    for j = minY : maxY
        in = inpolygon(i, j, x0Px, y0Px);
        in2 = inpolygon(i, j, x1Px, y1Px);
        if (in ~= 0 && in2 ~= 0)
%             image2(i, j, [2 2 2]) = 1; 
            x_(end + 1) = i;
            y_(end + 1) = j;
        end
    end
end
for i = 1 : length(x_)
    image2(x_(i), y_(i), [2 2 2]) = 1;
end

imshow(image2);
imwrite(image2, "circles.png");
