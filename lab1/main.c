/* COMPILER-DEPENDANT BEHAVIOR */
#ifdef _MSC_VER
    #define FILENAME "output/msvc_results.csv"
#elif __GNUC__
    /*
        GCC on Windows uses msvctr.dll by default, which uses Microsoft's
        implementation of printf. That implementation doesn't expect a long double
        argument which causes problems. This preprocessor directive forces the compiler
        to use MINGW's implementation.
    */
    #define __USE_MINGW_ANSI_STDIO 1
    #define FILENAME "output/gcc_results.csv"
#else
    #define FILENAME "output/unknown_results.csv"
#endif

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

    FILE* file = fopen(FILENAME, "w");
    if (!file) {
        printf("Error: couldn't open file.\n");
        return 1;
    }

    // File header
    fprintf(file, "x0,variant,k,float_val,double_val,long_double_val,delta_fd,delta_dl\n");

    const int x_0_count = 3;
    const long double x_0s[] = { 0.1L, 0.1000001L, 0.1000000000000001L };

    for (int i = 0; i < x_0_count; ++i) {
        data_t data     = initialize_data(x_0s[i]);
        data_t alt_data = initialize_data(x_0s[i]);
        const long double x_0 = x_0s[i];

        for (int k = 0; k < K_MAX; ++k) {
            fprintf(file, "%.21Lf,basic,%d,%.21f,%.21f,%.21Lf,%.21Le,%.21Le\n", 
                    x_0, k, data.fx, data.dx, data.ldx, 
                    fabsl((long double) data.fx - data.dx), 
                    fabsl((long double) data.dx - data.ldx));
            step(&data);
        }

        for (int k = 0; k < K_MAX; ++k) {
            fprintf(file, "%.21Lf,alt,%d,%.21f,%.21f,%.21Lf,%.21Le,%.21Le\n", 
                    x_0, k, alt_data.fx, alt_data.dx, alt_data.ldx, 
                    fabsl((long double) alt_data.fx - alt_data.dx), 
                    fabsl((long double) alt_data.dx - alt_data.ldx));
            alt_step(&alt_data);
        }
    }

    fclose(file);
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
