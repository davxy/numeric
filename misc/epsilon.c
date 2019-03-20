/*
 * Machine precision using arbitrary precision floats.
 *
 * Depends on GMP library. On debian
 *
 *   $ sudo apt install libgmp-dev
 *
 * To build
 *
 *  $ gcc epsilon.c -lgmp
 */

#include <gmp.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    mpf_t e, c, t, one;
    int prec;

    if (argc < 2) {
        printf("Usage %s <precision-bits>\n", argv[0]);
        return 0;
    }
    prec = atoi(argv[1]);

    printf("Default precision: %u\n", mpf_get_default_prec());
    printf("Setting precision: %u\n", prec);
    mpf_set_default_prec(prec);

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

    gmp_printf("%.100Fe\n", e);
    printf("\n");

    mpf_clears(e, c, t, one, NULL);
    return 0;
}
