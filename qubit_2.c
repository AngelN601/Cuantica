#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int generar_bit() {     // Da un numero random para generar el Qubit
    return rand() % 2;
}

int generar_base() {    // Da un numero random para generar la base
    return rand() % 2;
}

void generar_qubit(int bit, int base, char *bc, char *qubit) {      
    if (base == 0) {        // Se define la base en C o D
        *bc = 'C';
    } else {
        *bc = 'D';
    }

    if (bit == 0) {                 // Se define el qubit a utilizar dependiendo su base
        strcpy(qubit, "ketcero");       
    } else {
        strcpy(qubit, "ketmenos");
    }

    if (bit == 0 && base == 1) {
        strcpy(qubit, "ketmas");
    } else if (bit == 1 && base == 0) {
        strcpy(qubit, "ketuno");
    }
}

void generar_llave_qubits(int n, int eva_presente) {
    int llave_privada[n];           // Variable donde se guardara la llave privada
    char qubitAlice[n][10];
    char qubitBob[n][10];
    char qubitEva[n][10];
    int eva = 0;
    int contador_llave = 0; // Contador para la llave privada compartida

    for (int i = 0; i < n; i++) {
        int bit = generar_bit();
        int baseA = generar_base();
        int baseB = generar_base();
        int baseE = generar_base();
        
        char bcA, qubit[10], bcB, qubitB[10], bcE, qubitE[10];

        generar_qubit(bit, baseA, &bcA, qubit);
        generar_qubit(bit, baseB, &bcB, qubitB);
        generar_qubit(bit, baseE, &bcE, qubitE);

        if (bcA == bcB) {                       // Base de Alice y Bob Iguales
            llave_privada[contador_llave] = bit;
            strcpy(qubitAlice[i], qubit);
            strcpy(qubitBob[i], qubitB);
            contador_llave++;

            if (eva_presente) {                 // Eva Presente
                if (bcA != bcE && bcB == 'C') {     // Si la base de Alice es diferente a la de Eva (Base Bob = C)
                    char qubit_falso[10];
                    if (rand() % 2 == 0) {
                        strcpy(qubit_falso, "ketcero");
                    } else {
                        strcpy(qubit_falso, "ketuno");
                    }
                    printf("\n______________\nAlice\nBit: %d bc: %c qubit: %s\nBob\nbc: %c qubit: %s", bit, bcA, qubit, bcB, qubit_falso);

                    if (strcmp(qubit, qubit_falso) != 0) {      // Si el Qubit es de Bob y Alice es diferente
                        printf("\nEVA PRESENTE");           
                        eva++;
                    }
                } else if (bcA != bcE && bcB == 'D') {      // Si la base de Alice es diferente a la de Eva (Base Bob = D)
                    char qubit_falso[10];
                    if (rand() % 2 == 0) {
                        strcpy(qubit_falso, "ketmenos");
                    } else {
                        strcpy(qubit_falso, "ketmas");
                    }
                    printf("\n______________\nAlice\nBit: %d bc: %c qubit: %s\nBob\nbc: %c qubit: %s", bit, bcA, qubit, bcB, qubit_falso);

                    if (strcmp(qubit, qubit_falso) != 0) {      // Si el Qubit es de Bob y Alice es diferente
                        printf("\nEVA PRESENTE");
                        eva++;
                    }
                } else {
                    printf("\n______________\nAlice\nBit: %d bc: %c qubit: %s\nBob\nbc: %c qubit: %s", bit, bcA, qubit, bcB, qubitB);       // Qubit de Alice y Bob son iguales, eva pasa desapercibida
                }
            } else {
                printf("\n______________\nAlice\nBit: %d bc: %c qubit: %s\nBob\nbc: %c qubit: %s", bit, bcA, qubit, bcB, qubitB);       // Eva no esta presente
            }
        } else {
            strcpy(qubitAlice[i], qubit);
            strcpy(qubitBob[i], qubitB);
            printf("\n______________\nAlice\nBit: %d bc: %c qubit: %s\nBob\nbc: %c qubit: %s SE CANCELA", bit, bcA, qubit, bcB, qubitB);    // Diferentes bases se cancela
        }
    }

    if (eva >= 1) {
        printf("\nEl protocolo se cancelo debido a la interferencia de Eva %d veces.\n", eva);        // Se cancela con la presencia de Eva
    } else {
        printf("\nLa llave privada es: ");            // Generador de la llave privada
        for (int i = 0; i < contador_llave; i++) {
            printf("%d ", llave_privada[i]);
        }
        printf("\n");
    }
}

int main() {        // Funcion principal 
    printf("Protocolo BB84\n");
    printf("1. Con intervencion de Eva\n");
    printf("2. Sin intervencion de Eva\n");

    int opcion;
    printf("Seleccione una opcion (1/2): ");    // Seleccion con o sin Eva
    scanf("%d", &opcion);

    int eva_presente;           
    if (opcion == 1) {
        eva_presente = 1;
    } else if (opcion == 2) {
        eva_presente = 0;
    } else {
        printf("Opcion no valida. Ejecute nuevamente el programa.\n");
        return 1;
    }

    int n;
    printf("¿Cuantos Qubits seran?: ");     // Seleccion de Qubits
    scanf("%d", &n);

    srand(time(NULL));
    generar_llave_qubits(n, eva_presente);      // Llama la funcion de generar llave, ya sea con Eva o no

    return 0;
}
