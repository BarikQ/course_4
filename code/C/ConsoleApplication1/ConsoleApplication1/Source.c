#include <stdio.h>
#include <string.h> 
#include <math.h>

#define PI 3.14159265
#define RAD2DEG 0.017453
#define DEG2RAD 57.295780

double deg2rad(double degree);
double rad2deg(double radian);
int getSize(double* array) {
    return (int)(sizeof(array) / sizeof(array[0]));
}

int main(void)
{
    const double d = 3e-4;
    const double t = 100e-6;
    const double h = 7e-4;

    printf("d = %lf\nt = %lf\nh = %lf\n", d, t, h);

    const double height = 4.0e-3;
    const double width = 4.0e-3;

    const int pxW = 752;
    const int pxH = 752;

    const double pxSize = width / pxW;

    double angle[360];

    printf("angle = %lf\n", angle[i]);
    for (int i = 0; i < getSize(angle); i++) {
        angle[i] = deg2rad(i);
        printf("angle = %lf\n", angle[i]);
    }

    //long double x[360];
    //long double y[360];
    //memset(x, 0, 360); // заполнение массивов 0
    //memset(y, 0, 360); //

    //const int pxH = 1000;
    //const int pxW = 1000;
    //const pxSize = W / pxW;

    //const double theta_src = 65; // исходный зенитный угол
    //const double phi_src = 0;        // исходный азимутальный угол

    //const double theta = deg2rad(90) - deg2rad(theta_src);
    //const double phi = deg2rad(phi_src);
    //const double dC = h * tan(PI / 2 - theta);

    //printf("%lf\n", dC);
    return 0;
}

double deg2rad(double degree) {
    return degree * PI / 180.;
}

double rad2deg(double radian) {
    return radian * 180. / PI;
}

//int hello() {
//    const double d = 600e-6;
//    const double t = 100e-6;
//    const double h = 0.81e-3;
//
//    printf("d = %lf\nt = %lf\nh = %lf\n", d, t, h);
//
//    const double H = 4.0e-3;
//    const double W = 4.0e-3;
//    long double x[360];
//    long double y[360];
//    memset(x, 0, 360); // заполнение массивов 0
//    memset(y, 0, 360); //
//
//    const int pxH = 1000;
//    const int pxW = 1000;
//    const pxSize = W / pxW;
//
//    const double theta_src = 65; // исходный зенитный угол
//    const double phi_src = 0;        // исходный азимутальный угол
//
//    const double theta = deg2rad(90) - deg2rad(theta_src);
//    const double phi = deg2rad(phi_src);
//    const double dC = h * tan(PI / 2 - theta);
//}