#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	char nome[30];
	char endereco[30];
	int telefone;
	
	printf("Por favor, digite seu nome: \n");
	scanf("%s", &nome);
	
	printf("Agora digite seu endere�o: \n");
	scanf("%s", &endereco);
	
	printf("E por fim, digite seu telefone: \n");
	scanf("%d", &telefone);
	
	printf("\n Nome cadastrado: %s", nome);
	printf("\n Endere�o cadastrado: %s", endereco);
	printf("\n Telefone cadastrado: %d", telefone);

	return 0;
}
