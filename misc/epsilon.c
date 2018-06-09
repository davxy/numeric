#include <gmp.h>
#include <stdio.h>

#define PREC    1024

int main(void)
{
    mpf_t e, c, t, one;

    printf("Default precision: %u\n", mpf_get_default_prec());
    printf("Setting to %d\n", PREC);
    mpf_set_default_prec(PREC);

    mpf_inits(e, c, t, one, NULL);
    mpf_set_d(e, 1.0);
    mpf_set_d(c, 0.5);
    mpf_set_d(one, 1.0);

    while (1) {
        mpf_mul(t, c, e);
        mpf_add(t, one, t);
        if (mpf_cmp(t, one) == 0)
            break;
        mpf_mul(e, c, e);
    }

    ////////////gmp_printf("%.100Ff\n", e);
    gmp_printf("%.100Fe\n", e);
    printf("\n");

    mpf_clears(e, c, t, one, NULL);
    return 0;
}
