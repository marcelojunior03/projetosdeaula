#include <stdio.h>
#include <string.h>
#include <locale.h>

void main(){
    char nome[100];
    char genero[100];
    setlocale(LC_ALL, "Portuguese");

    printf("Ol�, qual o seu nome?\n");
    fflush(stdin);
    scanf("%[^\n]", &nome);
    fflush(stdin);
    printf("Certo, %s. Me diga seu g�nero musical favorito:\n", nome);
    scanf("%s", &genero);

    if(strcmp(genero, "pop") == 0){
        printf("Que legal, %s! O meu favorito tamb�m � %s!", nome, genero);
    } else if (strcmp(genero, "rock") == 0) {
        printf("UAU! %s, voc� parece uma pessoa el�trica!", nome);
    } else if (strcmp(genero, "sertanejo") == 0) {
        printf("Uhu! Tamb�m sou f� de uma sofr�ncia, %s!", nome);
    } else {
        printf("Que interessante, %s. Vou tentar ficar mais por dentro desse g�nero!", nome);
    }

}
