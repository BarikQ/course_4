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

theta = deg2rad(67);      % �������� ���� ������� ��������� �����
phi = deg2rad(30);      % ������������ ���� ������� ��������� �����

angle = deg2rad(0 : 359);   % ��������������� ������ �����
x = (d/2) * cos(angle);             % ���������� x ������� �����
y = (d/2) * sin(angle);             % ���������� y ������� �����

xcopy = x;
ycopy = y;

slength = size(y);
for i = 1 : slength(2)
    if(abs(y(i)) >= ((t * tan(theta)) / 2))
        if(y(i) > 0)
            y(i) = y(i) - ((t * tan(theta)) / 2);            
        else
            y(i) = y(i) + ((t * tan(theta)) / 2);            
        end
    else
        % ��� ������������ ��������
        y(i) = 15;
        x(i) = 15;
    end
    clc;
end

% �������� �� ������ �����
x(x == 15) = [];
y(y == 15) = [];
x = x + W/2;
y = y + H/2;
xcopy = xcopy + W/2;
ycopy = ycopy + H/2;

screenSize = get(0,'screensize');       % ��������� ������� ������
plotSize = 500;                         % ��������� ������� ������(������� ��������)
figure('Position', [(screenSize(3) - plotSize)/2 (screenSize(4) - plotSize)/2 plotSize plotSize]);
scatter(xcopy, ycopy, 'b');
hold on;
scatter(x, y, 'r');
xlim([0 W]);
ylim([0 H]);

% �������

image = zeros(pxH, pxW, 3);

pxX = zeros(1, 360);
pxY = zeros(1, 360);
pxXcopy = zeros(1, 360);
pxYcopy = zeros(1, 360);

pxX = ceil((x) / pxSize);
pxY = ceil((y) / pxSize);
pxXcopy = ceil((xcopy) / pxSize);
pxYcopy = ceil((ycopy) / pxSize);

image(100, 10, 1) = 1;

for it = 1 : length(pxX)
   image(pxY(it), pxX(it), [1 1 1]) = 1; 
end

for it = 1 : length(pxXcopy)
   image(pxYcopy(it), pxXcopy(it), [2 2 2]) = 1; 
end


%% ������� �����������
M = [cos(phi) -sin(phi); sin(phi) cos(phi)];
v = [x - W/2; y - H/2];
vrot = (v' * M)';
hold on;
scatter(vrot(1, :) + W/2, vrot(2, :) + H/2, 'g');

pxXrot = ceil((vrot(1, :) + W/2) / pxSize);
pxYrot = ceil((vrot(2, :) + H/2) / pxSize);

itj = length(pxXrot);
for it = 1 : length(pxXrot)
   image(pxYrot(it), pxXrot(it), [3 3 3]) = 1; 
   itj = itj - 1;
end

%% ��������

r = tan(theta) * h;
vrot(1, :) = vrot(1, :) + (r * cos(phi));
vrot(2, :) = vrot(2, :) + (r * sin(phi));
figure('Position', [(screenSize(3) - plotSize)/2 (screenSize(4) - plotSize)/2 plotSize plotSize]);
scatter(vrot(1, :), vrot(2, :), '+')
xlim([-H/2 H/2]);
ylim([-W/2 W/2]);

pxXbias = ceil((vrot(1, :) + H/2) / pxSize);
pxYbias = ceil((vrot(2, :) + W/2) / pxSize);

for it = 1 : length(pxXrot)
   image(pxXbias(it), pxYbias(it), [1 2 1]) = 1; 
end

imshow(image);