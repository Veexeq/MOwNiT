/*
    GCC on Windows uses msvctr.dll by default, which uses Microsoft's
    implementation of printf. That implementation doesn't expect a long double
    argument which causes problems. This preprocessor directive forces the compiler
    to use MINGW's implementation.
*/
#define __USE_MINGW_ANSI_STDIO 1

#include <stdio.h>
#include <math.h>

#define K_MAX 100

typedef struct T_sequence_element {
    float fx;
    double dx;
    long double ldx;
} data_t;

data_t initialize_data(long double);
void step(data_t*);
void alt_step(data_t*);
void print_data(data_t*, int);

int main(void) {

    // const long double x_0 = 0.1000001;
    // const int precision = 7;
    const long double x_0 = 0.1000000000000001;
    const int precision = 16;

    data_t data = initialize_data(x_0);
    data_t alt_data = initialize_data(x_0);
    for (int i = 0; i < K_MAX; ++i) {
        print_data(&alt_data, precision);
        
        step(&data);
        alt_step(&alt_data);
    }

    return 0;
}

data_t initialize_data(long double x_0) {
    return (data_t) { .fx = x_0, .dx = x_0, .ldx = x_0 };
}

void step(data_t* data) {
    data->fx  = data->fx  + 3.0f * data->fx  * (1.0f - data->fx);
    data->dx  = data->dx  + 3.0  * data->dx  * (1.0 - data->dx);
    data->ldx = data->ldx + 3.0L * data->ldx * (1.0L - data->ldx);
}

void alt_step(data_t* data) {
    data->fx  = 4.0f * data->fx  - 3.0f * data->fx  * data->fx;
    data->dx  = 4.0  * data->dx  - 3.0  * data->dx  * data->dx;
    data->ldx = 4.0L * data->ldx - 3.0L * data->ldx * data->ldx;
}

void print_data(data_t* data, int precision) {
    printf("(float): %0.*f, ", precision, data->fx);
    printf("(f-d diff): %.*lf, ", precision, fabs(data->dx - data->fx));
    printf("(double): %0.*lf, ", precision, data->dx);
    printf("(d-l diff): %0.*Lf, ", precision, fabsl(data->ldx - data->dx));
    printf("(long double): %0.*Lf\n", precision, data->ldx);
}