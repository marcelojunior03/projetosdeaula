#include <stdio.h>
#include <string.h>
#include <locale.h>

void main(){
    char nome[100];
    char genero[100];
    setlocale(LC_ALL, "Portuguese");

    printf("Olá, qual o seu nome?\n");
    fflush(stdin);
    scanf("%[^\n]", &nome);
    fflush(stdin);
    printf("Certo, %s. Me diga seu gênero musical favorito:\n", nome);
    scanf("%s", &genero);

    if(strcmp(genero, "pop") == 0){
        printf("Que legal, %s! O meu favorito também é %s!", nome, genero);
    } else if (strcmp(genero, "rock") == 0) {
        printf("UAU! %s, você parece uma pessoa elétrica!", nome);
    } else if (strcmp(genero, "sertanejo") == 0) {
        printf("Uhu! Também sou fã de uma sofrência, %s!", nome);
    } else {
        printf("Que interessante, %s. Vou tentar ficar mais por dentro desse gênero!", nome);
    }

}
