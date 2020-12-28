clear all
close all;
clc;

line = 956;
% [origX, origY, brutX, brutY, randX, randY] = xlsread("compare.xlsx", 1, "F2:K3");
origX = xlsread("compare.xlsx", 1, "F2:F956");
origY = xlsread("compare.xlsx", 1, "G2:G956");
brutX = xlsread("compare.xlsx", 1, "H2:H956");
brutY = xlsread("compare.xlsx", 1, "I2:I956");
randX = xlsread("compare.xlsx", 1, "J2:J956");
randY = xlsread("compare.xlsx", 1, "K2:K956");


figure 
% compare(origX, brutX);
plot(1:length(origX), origX, 'b*');
hold on
plot(1:length(randY), randX, 'g*');
plot(1:length(brutX), brutX, 'c*');

sum(origX) / length(origX)
sum(origY) / length(origY)
sum(brutX) / length(brutX)
sum(brutY) / length(brutY)
sum(randX) / length(randX)
sum(randY) / length(randY)