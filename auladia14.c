#include <stdio.h>

void main(){
    char nome[100];
    char estilo[100];

    printf("Olá, qual o seu nome?\n");
    fflush(stdin);
    scanf("%s", &nome);
    printf("Certo, %s. Me diga seu estilo musical favorito:\n", nome);
    scanf("%e", &estilo);

    if (estilo == pop) {
        printf("Que legal, %s! O meu favorito também é %e!", nome, estilo);
    } else if (estilo == rock) {
        printf("UAU! %s, você parece uma pessoa elétrica!", nome);
    } else if (estilo == sertanejo) {
        printf("Uhu! Também sou fã de uma sofrência, %s!", nome);
    } else {
        printf("Que interessante, %s. Vou tentar ficar mais por dentro desse estilo!", nome);
    }

}